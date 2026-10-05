import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1,000 hourly samples
n_samples = 1000

# Synthetic features
temperature = np.random.uniform(15, 42, n_samples)          # °C
solar_irradiance = np.random.uniform(0, 1000, n_samples)     # W/m²
humidity = np.random.uniform(20, 90, n_samples)              # %
cloud_cover = np.random.uniform(0, 100, n_samples)           # %

# Target calculation with realistic physical relationships + noise
# Higher irradiance & lower cloud cover -> higher output
power_output = (
    (solar_irradiance * 0.004) 
    + (temperature * 0.05) 
    - (cloud_cover * 0.02) 
    - (humidity * 0.01) 
    + np.random.normal(0, 0.2, n_samples)
)
power_output = np.clip(power_output, 0, None)  # Ensure non-negative

# Create DataFrame
df = pd.DataFrame({
    'Temperature_C': temperature,
    'Solar_Irradiance_Wm2': solar_irradiance,
    'Humidity_Pct': humidity,
    'Cloud_Cover_Pct': cloud_cover,
    'Power_Output_kW': power_output
})

df.to_csv('solar_data.csv', index=False)
print("Dataset created: solar_data.csv")