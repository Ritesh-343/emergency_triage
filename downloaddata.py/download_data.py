import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
df = pd.read_csv("data/humaid_data.csv")

label_mapping = {
    "injured_or_dead_people": "critical",
    "rescue_volunteering_or_donation_effort": "critical",
    "requests_or_urgent_needs": "critical",
    "missing_or_found_people": "critical",
    "infrastructure_and_utility_damage": "medium",
    "displaced_people_and_evacuations": "medium",
    "caution_and_advice": "medium",
    "sympathy_and_support": "low",
    "other_relevant_information": "low",
    "not_humanitarian": "low",
}

df["severity"] = df["class_label"].map(label_mapping)

# Drop any rows where the label didn't match (just in case)
df = df.dropna(subset=["severity"])

# Keep only the columns you actually need
final_df = df[["tweet_text", "severity"]]
final_df.to_csv("data/training_data.csv", index=False)
X_train, X_test, y_train, y_test = train_test_split(
    df["tweet_text"], df["severity"], test_size=0.2, random_state=42
)
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print("Severity counts:")
print(final_df["severity"].value_counts())
print(final_df.head())