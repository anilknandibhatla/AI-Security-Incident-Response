import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("incident_logs.csv")

# Encode categorical data
label_encoders = {}
for column in ["event_type", "source_ip", "status"]:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Train a new Isolation Forest model (compatible with scikit-learn 1.4.2)
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(df[["event_type", "source_ip", "status", "severity_score"]])

# Save the retrained model
joblib.dump(model, "anomaly_detection_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

# Run anomaly detection
df["anomaly"] = model.predict(df[["event_type", "source_ip", "status", "severity_score"]])
df.to_csv("anomaly_results.csv", index=False)

print("🚀 AI Model Retrained Successfully! Check 'anomaly_results.csv' for results.")

