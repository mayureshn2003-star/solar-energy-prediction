import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv('solar_data.csv')

# 2. Features and Target
X = df[['Temperature_C', 'Solar_Irradiance_Wm2', 'Humidity_Pct', 'Cloud_Cover_Pct']]
y = df['Power_Output_kW']

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")

# 6. Save Model
joblib.dump(model, 'solar_model.pkl')
print("Model saved to solar_model.pkl")