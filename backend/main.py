from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os 
app = FastAPI()

# Load your trained model and vectorizer once, when the server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "model", "severity_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "model", "vectorizer.pkl"))
class Report(BaseModel):
    message: str

CRITICAL_KEYWORDS = [
    "trapped", "stuck", "bleeding", "blooding", "not breathing",
    "unconscious", "collapsed on", "drowning", "dying", "can't move",
    "buried", "crushed", "no pulse", "child inside", "kids inside", "drown", "drowned", "drowning", "drownd", "drownend",
    "trapped", "stuck", "bleed", "blood",  # catches bleeding, blooding, bled, blood
    "breath",                               # catches "not breathing", "can't breathe"
    "unconscious", "collapsed on", "drown", # catches drown, drowned, drowning, drownend
    "dying", "can't move", "buried", "crushed",
    "no pulse", "child inside", "kids inside"
]

@app.post("/classify")
def classify(report: Report):
    text_vec = vectorizer.transform([report.message])
    prediction = model.predict(text_vec)[0]
    probabilities = model.predict_proba(text_vec)[0]
    confidence = max(probabilities)

    message_lower = report.message.lower()
    keyword_hit = any(word in message_lower for word in CRITICAL_KEYWORDS)

    final_severity = prediction
    override_applied = False

    if keyword_hit and prediction != "critical":
        final_severity = "critical"
        override_applied = True

    return {
        "message": report.message,
        "model_prediction": prediction,
        "severity": final_severity,
        "confidence": round(float(confidence), 2),
        "safety_override_applied": override_applied
    }

@app.get("/")
def home():
    return {"status": "Emergency triage API is running"}
