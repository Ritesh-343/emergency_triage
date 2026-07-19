🚨 AI Emergency Triage & Response Routing

Live App: https://emergencytriage-ne4j4dngchjzfja4jwebuq.streamlit.app/
GitHub Repo: https://github.com/Ritesh-343/emergency_triage
________________________________________
The Problem:
When a disaster strikes — a building collapse, a flood, a fire — dozens of panicked reports flood in within minutes. India's emergency system, ERSS-112, already receives these reports through multiple channels (voice, SMS, WhatsApp, app). But per the official ERSS-112 operating manual, the actual triage decision — reading a call, judging its severity, and deciding which category it falls into — is performed manually by a human "Call Attender" who classifies each report by hand.
This is the exact bottleneck this project addresses. I am not replacing 112 or building a new phone network. I am building the missing intelligence layer that sits on top of the existing intake system: something that instantly reads an incoming report, judges how serious it is, and decides who should respond — the two things a human dispatcher currently does manually, one call at a time, under pressure.
What This Project Actually Does
1.	Classifies incoming emergency reports by severity (critical / medium / low) using a trained machine learning model — not a scripted if/else, and not a call to an external LLM.
2.	Catches what the model misses using a safety-net layer built specifically for real-world Indian emergency phrasing — including Hindi code-switched terms ("bachao," "jaldi aao",”Uncle help karo”) and common phonetic misspellings.
3.	Routes the incident to the nearest available responder team using real distance calculations (the haversine formula) and estimates arrival time.
4.	Visualizes everything live on an interactive map, and handles the case where a surge of incidents exceeds available responder capacity — honestly, without pretending the problem doesn't exist.
Architecture
User types report → Clicks location on map (simulates phone GPS)
        ↓
Trained ML Model (TF-IDF + Logistic Regression)
        ↓
Safety-Net Keyword Layer (catches missed critical cases)
        ↓
Routing Algorithm (haversine distance + ETA calculation)
        ↓
Live map updates + Incident log + Analytics dashboard
The AI Model — Real Details
•	Training data: HumAID — ~53,500 real, human-labeled tweets from actual past disasters (earthquakes, floods, hurricanes), mapped from HumAID's 10 detailed categories down into 3 simplified severity levels (critical / medium / low).
•	Added some keywords by me as well according to the Indian words.
•	Approach: Text converted to numerical features using TF-IDF, classified using Logistic Regression (class_weight="balanced" to handle the smaller "medium" category fairly).
•	Result on held-out test data (20%, never seen during training):
Metric	Score
Overall Accuracy	82.9%
Critical — Precision / Recall	0.87 / 0.88
Medium — Precision / Recall	0.83 / 0.79
Low — Precision / Recall	0.79 / 0.79
•	(See confusion_matrix.png for the full visual breakdown.)
•	Why recall on "critical" matters most: in a triage system, missing a real emergency (false negative) is far more dangerous than over-flagging a non-emergency. Our model catches 88% of true critical cases on its own — and the safety-net layer below exists specifically to catch a meaningful share of the remainder.
The Safety-Net Layer — Why It Exists
During stress-testing, I found the ML model alone sometimes under-classified short, real-world panicked phrasing — e.g., "cylinder blast in kitchen one burned" was initially misclassified as low severity, i add a hybrid AI + rule-based safety layer, where a curated list of ~190 danger-indicating words and phrases (English, Hindi code-switched terms, and common Indian-English misspellings like "blooding," "drownend") . 
This is standard practice in safety-critical systems: never rely purely on a single ML model's raw output when lives are involved.
Routing Logic(For DEMO only):
Given an incident's location and severity, the system:
1.	Calculates real-world distance (haversine formula, accounts for Earth's curvature) to every currently-available responder team.
2.	Assigns the closest available team.
3.	Estimates arrival time assuming average city traffic speed (30 km/h).
4.	Marks that team as busy, so it isn't double-assigned.
5.	If no team is available (e.g., during a disaster surge), the system honestly reports this rather than failing silently or guessing.
Features Demonstrated
•	📍 Click-to-report location (simulates automatic GPS capture from a real emergency call)
•	🗺️ Live, color-coded map (red = critical, orange = medium, green = low) with responder team status
•	🚨 Disaster Surge Simulation — submits 8 simultaneous incidents to demonstrate real-world scale handling, not just one-at-a-time reports
•	📊 Live analytics dashboard (total incidents, critical count, average ETA, safety overrides triggered)
•	🔄 Reset Demo button for repeatable testing
Honest Limitations & Future Work
We believe being upfront about what this doesn't do yet is more credible than overclaiming:
•	No real speech-to-text / telephony integration. In production, this would plug directly into 112's existing call infrastructure using a speech-to-text pipeline (e.g., Whisper) to convert live panicked calls into text automatically. This hackathon build accepts typed text as a stand-in for that pipeline.
•	Keyword safety-net is a stopgap, not the ideal fix. The real long-term solution is retraining  the classifier on actual Indian-English/Hinglish emergency call transcripts rather than global English disaster tweets — this would let the model learn these patterns naturally instead of relying on a hand-curated keyword list.
•	Responder locations are simulated, not connected to real ambulance/rescue team GPS feeds.
•	Negation handling is limited — messages like "no one is trapped, everyone is safe" can still trigger keyword-based safety overrides, a known tradeoff we accepted (a false alarm is a safer failure mode than a missed emergency, but it's not a solved problem).
Tech Stack
•	Model: Python, scikit-learn (TF-IDF + Logistic Regression)
•	App/Interface: Streamlit
•	Mapping: Folium + streamlit-folium
•	Routing: Custom haversine-distance algorithm
•	Deployment: Streamlit Community Cloud
•	Data: HumAID (CrisisNLP / QCRI)
Running Locally
git clone https://github.com/Ritesh-343/emergency_triage.git
cd emergency_triage
pip install -r requirements.txt
streamlit run app.py
Name:
Ritesh Bachhav

