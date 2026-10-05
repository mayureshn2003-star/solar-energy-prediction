import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('solar_model.pkl')

st.title("☀️ Solar Power Generation Predictor")
st.write("Adjust environmental factors to predict estimated power output in kW.")

# Sidebar / Main Sliders
col1, col2 = st.columns(2)

with col1:
    irradiance = st.slider("Solar Irradiance (W/m²)", 0.0, 1000.0, 600.0)
    temp = st.slider("Temperature (°C)", 10.0, 50.0, 28.0)

with col2:
    cloud = st.slider("Cloud Cover (%)", 0.0, 100.0, 20.0)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 45.0)

# Prediction
if st.button("Predict Generation"):
    input_features = np.array([[temp, irradiance, humidity, cloud]])
    prediction = model.predict(input_features)[0]
    
    st.success(f"⚡ Estimated Power Output: **{prediction:.2f} kW**")