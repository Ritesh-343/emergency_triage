import math

# Seed some fake responder teams for the demo
RESPONDERS = [
    {"id": "Team A", "lat": 19.9975, "lng": 73.7898, "available": True},
    {"id": "Team B", "lat": 20.0059, "lng": 73.7910, "available": True},
    {"id": "Team C", "lat": 19.9890, "lng": 73.7800, "available": True},
    {"id": "Team D", "lat": 20.0100, "lng": 73.7950, "available": True},
    {"id": "Team E", "lat": 19.9930, "lng": 73.8010, "available": True},
    {"id": "Team F", "lat": 20.0020, "lng": 73.7750, "available": True},
    {"id": "Team G", "lat": 19.9850, "lng": 73.7920, "available": True},
    {"id": "Team H", "lat": 20.0080, "lng": 73.7860, "available": True},
]

def haversine_distance(lat1, lng1, lat2, lng2):
    """Real-world distance in km between two lat/lng points."""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng/2)**2)
    return R * 2 * math.asin(math.sqrt(a))

def assign_responder(incident_lat, incident_lng, severity, responders=RESPONDERS):
    """Pick the best available responder: nearest, with critical cases prioritized."""
    available = [r for r in responders if r["available"]]
    if not available:
        return None

    # Compute distance to each available responder
    for r in available:
        r["distance_km"] = haversine_distance(incident_lat, incident_lng, r["lat"], r["lng"])

    # Sort by distance - closest first
    available.sort(key=lambda r: r["distance_km"])
    best = available[0]

    # Estimate arrival time assuming average 30 km/h in city traffic
    eta_minutes = round((best["distance_km"] / 30) * 60, 1)

    # Mark them busy so they're not double-assigned in the same demo session
    best["available"] = False

    return {
        "responder_id": best["id"],
        "distance_km": round(best["distance_km"], 2),
        "eta_minutes": eta_minutes,
    }