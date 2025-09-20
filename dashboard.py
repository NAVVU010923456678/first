import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="Dewatering AI Dashboard", layout="wide")
st.title("🚰 AI Dewatering Dashboard for Mines")

# ------------------ Fetch data ------------------ #
sensor_data = pd.DataFrame(requests.get("https://your-api-endpoint.com/sensor-data").json())

# ------------------ Water Level ------------------ #
st.subheader("Water Level")
fig1 = px.line(sensor_data, x='timestamp', y='water_level', title="Water Level Trend")
st.plotly_chart(fig1, use_container_width=True)

# ------------------ Solar Forecast ------------------ #
st.subheader("Solar Power Forecast")
solar_forecast = pd.DataFrame(requests.get("https://your-api-endpoint.com/solar-forecast").json())
fig2 = px.line(solar_forecast, x='ds', y='yhat', title="Predicted Solar Power (kW)")
st.plotly_chart(fig2, use_container_width=True)

# ------------------ Predicted Water Inflow ------------------ #
st.subheader("Predicted Water Inflow")
last_seq = sensor_data['water_level'].values[-10:]
pred_inflow = predict_next_inflow(last_seq)
st.metric("Next Hour Predicted Inflow (L)", f"{pred_inflow:.2f}")

# ------------------ Carbon Credits ------------------ #
st.subheader("Carbon Credit Tracking")
carbon_saved = calculate_carbon_credits(saved_energy_kwh=50, diesel_efficiency_l_kwh=2)
st.metric("CO2 Saved (kg)", f"{carbon_saved:.2f}")

st.info("💡 All data is updated in real-time from IoT sensors")
