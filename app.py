import streamlit as st
import joblib
import copy
import folium
from streamlit_folium import st_folium
from critical_keywords import CRITICAL_KEYWORDS
from responder_logic import assign_responder, RESPONDERS as DEFAULT_RESPONDERS

SURGE_INCIDENTS = [
    {"message": "building collapsed people trapped inside need urgent rescue", "lat": 19.9975, "lng": 73.7898},
    {"message": "bhai jaldi aao ghar mein aag lag gayi bachao", "lat": 20.0059, "lng": 73.7910},
    {"message": "flood water entering house family stuck on roof", "lat": 19.9890, "lng": 73.7800},
    {"message": "small pothole on the road near market", "lat": 20.0100, "lng": 73.7950},
    {"message": "car accident on highway two people bleeding badly", "lat": 19.9930, "lng": 73.8010},
    {"message": "power outage in the area since morning", "lat": 20.0020, "lng": 73.7750},
    {"message": "gas cylinder blast in kitchen one burned badly", "lat": 19.9850, "lng": 73.7920},
    {"message": "traffic jam due to tree fall no injuries", "lat": 20.0080, "lng": 73.7860},
]

st.set_page_config(page_title="AI Emergency Triage", layout="wide")

@st.cache_resource
def load_model():
    model = joblib.load("model/severity_model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

if "incidents" not in st.session_state:
    st.session_state.incidents = []
if "pending_location" not in st.session_state:
    st.session_state.pending_location = None
if "responders" not in st.session_state:
    st.session_state.responders = copy.deepcopy(DEFAULT_RESPONDERS)

st.title("🚨 AI Emergency Triage & Response Routing")
st.caption("Classifies incoming emergency reports and routes them to the nearest available responder — instantly.")

severity_colors = {"critical": "red", "medium": "orange", "low": "green"}

def process_incident(message, lat, lng):
    text_vec = vectorizer.transform([message])
    prediction = model.predict(text_vec)[0]
    probabilities = model.predict_proba(text_vec)[0]
    confidence = max(probabilities)

    message_lower = message.lower()
    keyword_hit = any(word in message_lower for word in CRITICAL_KEYWORDS)
    final_severity = prediction
    override_applied = False
    if keyword_hit and prediction != "critical":
        final_severity = "critical"
        override_applied = True

    assignment = assign_responder(lat, lng, final_severity, responders=st.session_state.responders)

    st.session_state.incidents.append({
        "message": message,
        "severity": final_severity,
        "confidence": round(float(confidence), 2),
        "override": override_applied,
        "lat": lat,
        "lng": lng,
        "assignment": assignment,
    })

# ---- Report form (message only — location comes from map click below) ----
st.subheader("Report an Incident")
message = st.text_area("What's happening?", placeholder="e.g. building collapsed people trapped inside")
st.write("📍 Click anywhere on the map below to mark the incident's location (simulates automatic GPS detection from the caller's phone).")

# ---- Build ONE combined map: past incidents + responders + click capture ----
combined_map = folium.Map(location=[19.9975, 73.7898], zoom_start=13)
combined_map.get_root().html.add_child(folium.Element("""
<style>
.leaflet-container { cursor: crosshair !important; }
.leaflet-grab { cursor: crosshair !important; }
</style>
"""))

for incident in st.session_state.incidents:
    color = severity_colors.get(incident["severity"], "gray")
    folium.CircleMarker(
        location=[incident["lat"], incident["lng"]],
        radius=10,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.9,
        popup=f"{incident['severity'].upper()}: {incident['message'][:40]}",
    ).add_to(combined_map)

for r in st.session_state.responders:
    status = "Available" if r["available"] else "Busy"
    folium.Marker(
        location=[r["lat"], r["lng"]],
        popup=f"{r['id']} — {status}",
        icon=folium.Icon(color="blue", icon="ambulance", prefix="fa"),
    ).add_to(combined_map)

if st.session_state.pending_location:
    folium.Marker(
        location=[st.session_state.pending_location["lat"], st.session_state.pending_location["lng"]],
        popup="New incident location (not yet submitted)",
        icon=folium.Icon(color="black", icon="exclamation", prefix="fa"),
    ).add_to(combined_map)

map_output = st_folium(
    combined_map,
    height=550,
    width=1200,
    key="main_map",
    returned_objects=["last_clicked"]
)

if map_output and map_output.get("last_clicked"):
    st.session_state.pending_location = map_output["last_clicked"]

if st.session_state.pending_location:
    st.info(f"Selected location: {st.session_state.pending_location['lat']:.4f}, {st.session_state.pending_location['lng']:.4f}")
else:
    st.warning("No location selected yet — click on the map above.")

# ---- Buttons go BELOW the map ----
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
with btn_col1:
    submit_clicked = st.button("Submit Report", type="primary")
with btn_col2:
    surge_clicked = st.button("🚨 Simulate Disaster Surge (8 incidents)")
with btn_col3:
    reset_clicked = st.button("🔄 Reset Demo")

if submit_clicked:
    if not message.strip():
        st.error("Please describe what's happening.")
    elif not st.session_state.pending_location:
        st.error("Please click a location on the map first.")
    else:
        incident_lat = st.session_state.pending_location["lat"]
        incident_lng = st.session_state.pending_location["lng"]
        process_incident(message, incident_lat, incident_lng)
        st.session_state.pending_location = None
        st.success("Incident classified and routed — check the map and log below.")
        st.rerun()

if surge_clicked:
    for r in st.session_state.responders:
        r["available"] = True
    st.session_state.incidents = []

    for incident in SURGE_INCIDENTS:
        process_incident(incident["message"], incident["lat"], incident["lng"])

    st.success(f"Simulated {len(SURGE_INCIDENTS)} incoming incidents — see them classified and routed on the map below.")
    st.rerun()

if reset_clicked:
    st.session_state.incidents = []
    st.session_state.responders = copy.deepcopy(DEFAULT_RESPONDERS)
    st.session_state.pending_location = None
    st.rerun()

# ---- Analytics ----
st.subheader("Response Analytics")

if st.session_state.incidents:
    total = len(st.session_state.incidents)
    critical_count = sum(1 for i in st.session_state.incidents if i["severity"] == "critical")
    medium_count = sum(1 for i in st.session_state.incidents if i["severity"] == "medium")
    low_count = sum(1 for i in st.session_state.incidents if i["severity"] == "low")
    override_count = sum(1 for i in st.session_state.incidents if i["override"])

    etas = [i["assignment"]["eta_minutes"] for i in st.session_state.incidents if i["assignment"]]
    avg_eta = round(sum(etas) / len(etas), 1) if etas else 0

    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("Total Incidents", total)
    col_b.metric("Critical Cases", critical_count)
    col_c.metric("Avg ETA (min)", avg_eta)
    col_d.metric("Safety Overrides Triggered", override_count)

    st.caption(f"Breakdown — Critical: {critical_count} | Medium: {medium_count} | Low: {low_count}")
else:
    st.info("Submit incidents to see analytics here.")

st.divider()

# ---- Incident log ----
st.subheader("Incident Log")
for incident in reversed(st.session_state.incidents):
    with st.expander(f"{incident['severity'].upper()} — {incident['message'][:50]}"):
        st.write(f"**Confidence:** {incident['confidence']}")
        st.write(f"**Safety override applied:** {incident['override']}")
        if incident["assignment"]:
            st.write(f"**Assigned to:** {incident['assignment']['responder_id']} — ETA {incident['assignment']['eta_minutes']} min")
        else:
            st.write("⚠️ **No responder team available** — all teams currently busy")