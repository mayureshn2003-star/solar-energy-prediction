import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="India Solar Energy Tracker", layout="wide")

st.title("☀️ All India Solar Energy Consumption Tracker")
st.write("Select a state or search for a city to view real-time daily and monthly solar energy usage.")

# Data covering all 28 States & major Union Territories with major cities
all_cities_data = [
    # Andhra Pradesh
    {"state": "Andhra Pradesh", "city": "Visakhapatnam", "lat": 17.6868, "lon": 83.2185, "daily_kwh": 4300, "monthly_kwh": 129000},
    {"state": "Andhra Pradesh", "city": "Vijayawada", "lat": 16.5062, "lon": 80.6480, "daily_kwh": 3900, "monthly_kwh": 117000},
    {"state": "Andhra Pradesh", "city": "Tirupati", "lat": 13.6288, "lon": 79.4192, "daily_kwh": 3600, "monthly_kwh": 108000},
    
    # Arunachal Pradesh
    {"state": "Arunachal Pradesh", "city": "Itanagar", "lat": 27.0844, "lon": 93.6053, "daily_kwh": 2100, "monthly_kwh": 63000},
    {"state": "Arunachal Pradesh", "city": "Naharlagun", "lat": 27.1000, "lon": 93.6900, "daily_kwh": 1800, "monthly_kwh": 54000},
    
    # Assam
    {"state": "Assam", "city": "Guwahati", "lat": 26.1445, "lon": 91.7362, "daily_kwh": 3100, "monthly_kwh": 93000},
    {"state": "Assam", "city": "Silchar", "lat": 24.8333, "lon": 92.7789, "daily_kwh": 2400, "monthly_kwh": 72000},
    {"state": "Assam", "city": "Dibrugarh", "lat": 27.4728, "lon": 94.9120, "daily_kwh": 2200, "monthly_kwh": 66000},
    
    # Bihar
    {"state": "Bihar", "city": "Patna", "lat": 25.5941, "lon": 85.1376, "daily_kwh": 4100, "monthly_kwh": 123000},
    {"state": "Bihar", "city": "Gaya", "lat": 24.7914, "lon": 85.0002, "daily_kwh": 3500, "monthly_kwh": 105000},
    {"state": "Bihar", "city": "Muzaffarpur", "lat": 26.1209, "lon": 85.3647, "daily_kwh": 3200, "monthly_kwh": 96000},
    
    # Chhattisgarh
    {"state": "Chhattisgarh", "city": "Raipur", "lat": 21.2514, "lon": 81.6296, "daily_kwh": 3800, "monthly_kwh": 114000},
    {"state": "Chhattisgarh", "city": "Bhilai", "lat": 21.1938, "lon": 81.3509, "daily_kwh": 3600, "monthly_kwh": 108000},
    {"state": "Chhattisgarh", "city": "Bilaspur", "lat": 22.0797, "lon": 82.1391, "daily_kwh": 3300, "monthly_kwh": 99000},
    
    # Goa
    {"state": "Goa", "city": "Panaji", "lat": 15.4909, "lon": 73.8278, "daily_kwh": 2800, "monthly_kwh": 84000},
    {"state": "Goa", "city": "Margao", "lat": 15.2832, "lon": 73.9862, "daily_kwh": 2600, "monthly_kwh": 78000},
    
    # Gujarat
    {"state": "Gujarat", "city": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "daily_kwh": 5500, "monthly_kwh": 165000},
    {"state": "Gujarat", "city": "Surat", "lat": 21.1702, "lon": 72.8311, "daily_kwh": 5100, "monthly_kwh": 153000},
    {"state": "Gujarat", "city": "Vadodara", "lat": 22.3072, "lon": 73.1812, "daily_kwh": 4600, "monthly_kwh": 138000},
    {"state": "Gujarat", "city": "Rajkot", "lat": 22.3039, "lon": 70.8022, "daily_kwh": 4400, "monthly_kwh": 132000},
    
    # Haryana
    {"state": "Haryana", "city": "Gurugram", "lat": 28.4595, "lon": 77.0266, "daily_kwh": 4800, "monthly_kwh": 144000},
    {"state": "Haryana", "city": "Faridabad", "lat": 28.4089, "lon": 77.3178, "daily_kwh": 4200, "monthly_kwh": 126000},
    {"state": "Haryana", "city": "Panipat", "lat": 29.3909, "lon": 76.9635, "daily_kwh": 3600, "monthly_kwh": 108000},
    
    # Himachal Pradesh
    {"state": "Himachal Pradesh", "city": "Shimla", "lat": 31.1048, "lon": 77.1734, "daily_kwh": 2300, "monthly_kwh": 69000},
    {"state": "Himachal Pradesh", "city": "Dharamshala", "lat": 32.2190, "lon": 76.3234, "daily_kwh": 2100, "monthly_kwh": 63000},
    {"state": "Himachal Pradesh", "city": "Mandi", "lat": 31.5892, "lon": 76.9182, "daily_kwh": 1900, "monthly_kwh": 57000},
    
    # Jharkhand
    {"state": "Jharkhand", "city": "Ranchi", "lat": 23.3441, "lon": 85.3096, "daily_kwh": 3700, "monthly_kwh": 111000},
    {"state": "Jharkhand", "city": "Jamshedpur", "lat": 22.8046, "lon": 86.2029, "daily_kwh": 4100, "monthly_kwh": 123000},
    {"state": "Jharkhand", "city": "Dhanbad", "lat": 23.7957, "lon": 86.4304, "daily_kwh": 3800, "monthly_kwh": 114000},
    
    # Karnataka
    {"state": "Karnataka", "city": "Bengaluru", "lat": 12.9716, "lon": 77.5946, "daily_kwh": 5200, "monthly_kwh": 156000},
    {"state": "Karnataka", "city": "Mysuru", "lat": 12.2958, "lon": 76.6394, "daily_kwh": 3900, "monthly_kwh": 117000},
    {"state": "Karnataka", "city": "Hubballi", "lat": 15.3647, "lon": 75.1240, "daily_kwh": 3600, "monthly_kwh": 108000},
    {"state": "Karnataka", "city": "Mangaluru", "lat": 12.9141, "lon": 74.8560, "daily_kwh": 3800, "monthly_kwh": 114000},
    
    # Kerala
    {"state": "Kerala", "city": "Thiruvananthapuram", "lat": 8.5241, "lon": 76.9366, "daily_kwh": 3800, "monthly_kwh": 114000},
    {"state": "Kerala", "city": "Kochi", "lat": 9.9312, "lon": 76.2673, "daily_kwh": 4200, "monthly_kwh": 126000},
    {"state": "Kerala", "city": "Kozhikode", "lat": 11.2588, "lon": 75.7804, "daily_kwh": 3500, "monthly_kwh": 105000},
    
    # Madhya Pradesh
    {"state": "Madhya Pradesh", "city": "Bhopal", "lat": 23.2599, "lon": 77.4126, "daily_kwh": 4400, "monthly_kwh": 132000},
    {"state": "Madhya Pradesh", "city": "Indore", "lat": 22.7196, "lon": 75.8577, "daily_kwh": 4900, "monthly_kwh": 147000},
    {"state": "Madhya Pradesh", "city": "Gwalior", "lat": 26.2183, "lon": 78.1828, "daily_kwh": 4200, "monthly_kwh": 126000},
    {"state": "Madhya Pradesh", "city": "Jabalpur", "lat": 23.1815, "lon": 79.9864, "daily_kwh": 3900, "monthly_kwh": 117000},
    
    # Maharashtra
    {"state": "Maharashtra", "city": "Mumbai", "lat": 19.0760, "lon": 72.8777, "daily_kwh": 5600, "monthly_kwh": 168000},
    {"state": "Maharashtra", "city": "Pune", "lat": 18.5204, "lon": 73.8567, "daily_kwh": 4800, "monthly_kwh": 144000},
    {"state": "Maharashtra", "city": "Nagpur", "lat": 21.1458, "lon": 79.0882, "daily_kwh": 4500, "monthly_kwh": 135000},
    {"state": "Maharashtra", "city": "Nashik", "lat": 20.0059, "lon": 73.7898, "daily_kwh": 4100, "monthly_kwh": 123000},
    {"state": "Maharashtra", "city": "Chhatrapati Sambhajinagar", "lat": 19.8762, "lon": 75.3433, "daily_kwh": 3900, "monthly_kwh": 117000},
    
    # Manipur
    {"state": "Manipur", "city": "Imphal", "lat": 24.8170, "lon": 93.9368, "daily_kwh": 2200, "monthly_kwh": 66000},
    {"state": "Manipur", "city": "Thoubal", "lat": 24.6381, "lon": 93.9999, "daily_kwh": 1800, "monthly_kwh": 54000},
    
    # Meghalaya
    {"state": "Meghalaya", "city": "Shillong", "lat": 25.5788, "lon": 91.8933, "daily_kwh": 2100, "monthly_kwh": 63000},
    {"state": "Meghalaya", "city": "Tura", "lat": 25.5141, "lon": 90.2032, "daily_kwh": 1900, "monthly_kwh": 57000},
    
    # Mizoram
    {"state": "Mizoram", "city": "Aizawl", "lat": 23.7271, "lon": 92.7176, "daily_kwh": 2000, "monthly_kwh": 60000},
    {"state": "Mizoram", "city": "Lunglei", "lat": 22.8671, "lon": 92.7652, "daily_kwh": 1700, "monthly_kwh": 51000},
    
    # Nagaland
    {"state": "Nagaland", "city": "Kohima", "lat": 25.6751, "lon": 94.1086, "daily_kwh": 2000, "monthly_kwh": 60000},
    {"state": "Nagaland", "city": "Dimapur", "lat": 25.9060, "lon": 93.7271, "daily_kwh": 2300, "monthly_kwh": 69000},
    
    # Odisha
    {"state": "Odisha", "city": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245, "daily_kwh": 4200, "monthly_kwh": 126000},
    {"state": "Odisha", "city": "Cuttack", "lat": 20.4625, "lon": 85.8828, "daily_kwh": 3800, "monthly_kwh": 114000},
    {"state": "Odisha", "city": "Rourkela", "lat": 22.2604, "lon": 84.8536, "daily_kwh": 3900, "monthly_kwh": 117000},
    
    # Punjab
    {"state": "Punjab", "city": "Ludhiana", "lat": 30.9010, "lon": 75.8573, "daily_kwh": 4300, "monthly_kwh": 129000},
    {"state": "Punjab", "city": "Amritsar", "lat": 31.6340, "lon": 74.8723, "daily_kwh": 4100, "monthly_kwh": 123000},
    {"state": "Punjab", "city": "Jalandhar", "lat": 31.3260, "lon": 75.5762, "daily_kwh": 3800, "monthly_kwh": 114000},
    
    # Rajasthan
    {"state": "Rajasthan", "city": "Jaipur", "lat": 26.9124, "lon": 75.7873, "daily_kwh": 5800, "monthly_kwh": 174000},
    {"state": "Rajasthan", "city": "Jodhpur", "lat": 26.2389, "lon": 73.0243, "daily_kwh": 6100, "monthly_kwh": 183000},
    {"state": "Rajasthan", "city": "Udaipur", "lat": 24.5854, "lon": 73.7125, "daily_kwh": 4900, "monthly_kwh": 147000},
    {"state": "Rajasthan", "city": "Kota", "lat": 25.2138, "lon": 75.8648, "daily_kwh": 4700, "monthly_kwh": 141000},
    
    # Sikkim
    {"state": "Sikkim", "city": "Gangtok", "lat": 27.3389, "lon": 88.6065, "daily_kwh": 1900, "monthly_kwh": 57000},
    {"state": "Sikkim", "city": "Namchi", "lat": 27.1667, "lon": 88.3500, "daily_kwh": 1700, "monthly_kwh": 51000},
    
    # Tamil Nadu
    {"state": "Tamil Nadu", "city": "Chennai", "lat": 13.0827, "lon": 80.2707, "daily_kwh": 5400, "monthly_kwh": 162000},
    {"state": "Tamil Nadu", "city": "Coimbatore", "lat": 11.0168, "lon": 76.9558, "daily_kwh": 4800, "monthly_kwh": 144000},
    {"state": "Tamil Nadu", "city": "Madurai", "lat": 9.9252, "lon": 78.1198, "daily_kwh": 4600, "monthly_kwh": 138000},
    {"state": "Tamil Nadu", "city": "Tiruchirappalli", "lat": 10.7905, "lon": 78.7047, "daily_kwh": 4300, "monthly_kwh": 129000},
    
    # Telangana
    {"state": "Telangana", "city": "Hyderabad", "lat": 17.3850, "lon": 78.4867, "daily_kwh": 5300, "monthly_kwh": 159000},
    {"state": "Telangana", "city": "Warangal", "lat": 17.9689, "lon": 79.5941, "daily_kwh": 3800, "monthly_kwh": 114000},
    {"state": "Telangana", "city": "Nizamabad", "lat": 18.6725, "lon": 78.0941, "daily_kwh": 3500, "monthly_kwh": 105000},
    
    # Tripura
    {"state": "Tripura", "city": "Agartala", "lat": 23.8315, "lon": 91.2868, "daily_kwh": 2500, "monthly_kwh": 75000},
    {"state": "Tripura", "city": "Dharmanagar", "lat": 24.3833, "lon": 92.1667, "daily_kwh": 2000, "monthly_kwh": 60000},
    
    # Uttar Pradesh
    {"state": "Uttar Pradesh", "city": "Lucknow", "lat": 26.8467, "lon": 80.9462, "daily_kwh": 4700, "monthly_kwh": 141000},
    {"state": "Uttar Pradesh", "city": "Kanpur", "lat": 26.4499, "lon": 80.3319, "daily_kwh": 4500, "monthly_kwh": 135000},
    {"state": "Uttar Pradesh", "city": "Varanasi", "lat": 25.3176, "lon": 82.9739, "daily_kwh": 4200, "monthly_kwh": 126000},
    {"state": "Uttar Pradesh", "city": "Agra", "lat": 27.1767, "lon": 78.0081, "daily_kwh": 4100, "monthly_kwh": 123000},
    {"state": "Uttar Pradesh", "city": "Noida", "lat": 28.5355, "lon": 77.3910, "daily_kwh": 4800, "monthly_kwh": 144000},
    
    # Uttarakhand
    {"state": "Uttarakhand", "city": "Dehradun", "lat": 30.3165, "lon": 78.0322, "daily_kwh": 2900, "monthly_kwh": 87000},
    {"state": "Uttarakhand", "city": "Haridwar", "lat": 29.9457, "lon": 78.1642, "daily_kwh": 3100, "monthly_kwh": 93000},
    {"state": "Uttarakhand", "city": "Haldwani", "lat": 29.2183, "lon": 79.5130, "daily_kwh": 2700, "monthly_kwh": 81000},
    
    # West Bengal
    {"state": "West Bengal", "city": "Kolkata", "lat": 22.5726, "lon": 88.3639, "daily_kwh": 5100, "monthly_kwh": 153000},
    {"state": "West Bengal", "city": "Siliguri", "lat": 26.7271, "lon": 88.3953, "daily_kwh": 2900, "monthly_kwh": 87000},
    {"state": "West Bengal", "city": "Asansol", "lat": 23.6889, "lon": 86.9661, "daily_kwh": 3800, "monthly_kwh": 114000},
    
    # Union Territories
    {"state": "Delhi (UT)", "city": "New Delhi", "lat": 28.6139, "lon": 77.2090, "daily_kwh": 5800, "monthly_kwh": 174000},
    {"state": "Jammu & Kashmir (UT)", "city": "Srinagar", "lat": 34.0837, "lon": 74.7973, "daily_kwh": 2200, "monthly_kwh": 66000},
    {"state": "Jammu & Kashmir (UT)", "city": "Jammu", "lat": 32.7266, "lon": 74.8570, "daily_kwh": 3400, "monthly_kwh": 102000},
    {"state": "Ladakh (UT)", "city": "Leh", "lat": 34.1526, "lon": 77.5771, "daily_kwh": 2600, "monthly_kwh": 78000},
    {"state": "Chandigarh (UT)", "city": "Chandigarh", "lat": 30.7333, "lon": 76.7794, "daily_kwh": 3600, "monthly_kwh": 108000},
    {"state": "Puducherry (UT)", "city": "Puducherry", "lat": 11.9416, "lon": 79.8083, "daily_kwh": 3200, "monthly_kwh": 96000}
]

df = pd.DataFrame(all_cities_data)

# Sidebar Controls
st.sidebar.header("🗺️ Location Filters")

state_list = ["All States & UTs"] + sorted(list(df["state"].unique()))
selected_state = st.sidebar.selectbox("Select State / UT", state_list)

view_type = st.sidebar.radio("Display Energy Output As", ["Daily Usage (kWh)", "Monthly Usage (kWh)"])

# Filter Dataset based on selected State
if selected_state != "All States & UTs":
    filtered_df = df[df["state"] == selected_state]
    # Set map view center based on filtered selection
    map_center = [filtered_df["lat"].mean(), filtered_df["lon"].mean()]
    zoom_lvl = 6
else:
    filtered_df = df
    map_center = [20.5937, 78.9629]
    zoom_lvl = 5

# Create Map
m = folium.Map(location=map_center, zoom_start=zoom_lvl)

for _, row in filtered_df.iterrows():
    val = row['daily_kwh'] if view_type == "Daily Usage (kWh)" else row['monthly_kwh']
    unit = "kWh/day" if view_type == "Daily Usage (kWh)" else "kWh/month"
    
    popup_html = f"""
    <div style="font-family: Arial; width: 190px;">
        <h4 style="margin-bottom:2px;"><b>{row['city']}</b></h4>
        <p style="color:gray; margin-top:0px;">{row['state']}</p>
        <hr style="margin:5px 0;">
        <p><b>{view_type}:</b><br>
        <span style="color: #E65100; font-size: 17px;"><b>{val:,} {unit}</b></span></p>
    </div>
    """
    
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=f"{row['city']}, {row['state']}",
        icon=folium.Icon(color="orange", icon="sun-o", prefix="fa")
    ).add_to(m)

# Layout Presentation
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Map View ({len(filtered_df)} Locations)")
    st_folium(m, width=700, height=520)

with col2:
    st.subheader("Data Summary Table")
    st.dataframe(
        filtered_df[["state", "city", "daily_kwh", "monthly_kwh"]],
        column_config={
            "state": "State / UT",
            "city": "City",
            "daily_kwh": st.column_config.NumberColumn("Daily (kWh)", format="%d kWh"),
            "monthly_kwh": st.column_config.NumberColumn("Monthly (kWh)", format="%d kWh"),
        },
        hide_index=True,
        use_container_width=True
    )