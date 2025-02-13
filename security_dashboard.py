import streamlit as st
import pandas as pd

# Load anomaly detection results
df = pd.read_csv("anomaly_results.csv")

# Streamlit UI
st.title("🚨 AI-Powered Incident Response Dashboard")
st.write("Real-time security monitoring and anomaly detection")

# Show all incidents
st.subheader("All Security Incidents")
st.dataframe(df)

# Show anomalies
anomalies = df[df["anomaly"] == -1]
st.subheader("⚠️ Detected Security Anomalies")
st.dataframe(anomalies)

st.write("✔️ This dashboard helps prioritize incidents and automate response.")
