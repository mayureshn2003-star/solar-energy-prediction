# ☀️ All India Solar Energy Tracker & Prediction App

An interactive machine learning and geo-visualization platform built with **Python**, **Streamlit**, and **Folium**. This project predicts solar power generation based on environmental factors and tracks daily/monthly solar energy consumption across all **28 States, Union Territories, and major cities in India**.

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/) *(Replace with your deployed app link)*

---

## ✨ Features

- **🗺️ Interactive India Map**: Pinpoint solar energy consumption metrics across all 28 states, union territories, and key Indian cities using Folium markers.
- **📊 Granular Energy Tracking**: View and switch between daily (`kWh/day`) and monthly (`kWh/month`) solar power consumption.
- **🤖 Solar Power Generation Predictor**: Machine learning model (Random Forest Regressor) predicting power output based on real-time environmental factors:
  - Solar Irradiance ($W/m^2$)
  - Temperature (°C)
  - Cloud Cover (%)
  - Humidity (%)
- **🎛️ Dynamic Sidebar Filtering**: Filter locations seamlessly by state or union territory.

---

## 🛠️ Tech Stack & Libraries

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white)

---

## 📁 Directory Structure

```text
solar-prediction/
├── generate_data.py   # Script to produce synthetic solar weather dataset
├── train_model.py     # ML training script using Random Forest
├── app.py             # Main Streamlit web application with Folium map
├── solar_data.csv     # Historical solar weather dataset
├── solar_model.pkl    # Serialized trained model
├── requirements.txt   # Dependencies for local setup & cloud deployment
└── README.md          # Project documentation