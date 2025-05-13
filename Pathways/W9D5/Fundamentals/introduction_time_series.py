"""
Introduction to Time Series Data and Weather Forecasting
This example demonstrates basic concepts of time series data 
with weather data examples.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

# Generate a simple weather dataset with timestamps (simulated data)
# This is useful for teaching when you don't have external data available

# Create a series of dates (one week of hourly data)
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(hours=i) for i in range(24*7)]  # One week of hourly data

# Simulate temperature with daily cycles (warmer during day, cooler at night)
# Plus some random noise to make it realistic
np.random.seed(42)  # For reproducible results
base_temp = 20  # Base temperature in Celsius
daily_variation = 8  # Daily temperature swing
random_noise = 2  # Random fluctuations

# Generate temperature with a realistic pattern
temperatures = []
for date in dates:
    hour = date.hour
    # Daily cycle: coolest at 4AM, warmest at 2PM
    hour_factor = np.sin((hour - 4) * np.pi / 12) if 4 <= hour <= 16 else -np.sin((hour - 16) * np.pi / 12)
    temp = base_temp + hour_factor * daily_variation + np.random.normal(0, random_noise)
    temperatures.append(temp)

# Generate other weather variables that correlate with temperature
# Humidity is often inversely related to temperature
humidity = [max(30, min(95, 80 - 0.8 * (temp - base_temp) + np.random.normal(0, 5))) for temp in temperatures]

# Pressure (in hPa) - slight inverse correlation with temperature
pressure = [1013 - 0.2 * (temp - base_temp) + np.random.normal(0, 2) for temp in temperatures]

# Wind speed (in km/h) - random but with some correlation to pressure changes
wind_speed = [max(0, 5 + 0.1 * (1013 - p) + np.random.normal(0, 3)) for p in pressure]

# Create a pandas DataFrame - the standard way to work with time series data in Python
weather_data = pd.DataFrame({
    'timestamp': dates,
    'temperature': temperatures,
    'humidity': humidity,
    'pressure': pressure,
    'wind_speed': wind_speed
})

# Set the timestamp as the index (important for time series data)
weather_data.set_index('timestamp', inplace=True)

# Display the first few rows
print("Sample of our weather time series data:")
print(weather_data.head())

# Basic information about the dataset
print("\nData information:")
print(f"Time range: {weather_data.index.min()} to {weather_data.index.max()}")
print(f"Data frequency: {weather_data.index.to_series().diff().mode()[0]}")
print(f"Number of observations: {len(weather_data)}")
print("\nBasic statistics:")
print(weather_data.describe())

# Demonstrate what makes time series unique
print("\nTime Series Key Characteristics:")
print("1. Data is ordered by time")
print("2. Observations have a consistent frequency (hourly in this case)")
print("3. Past values can influence future values")
print("4. Often exhibits patterns like:")
print("   - Trends (long-term increase/decrease)")
print("   - Seasonality (daily/yearly cycles)")
print("   - Cyclical patterns (recurring but not fixed frequency)")

# Show a simple plot of temperature over time
plt.figure(figsize=(12, 6))
weather_data['temperature'].plot(title='Temperature Over One Week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()

# In a real classroom, you would use:
plt.savefig('temperature_time_series.png')
# For interactive display:
# plt.show()

print("\nWeather Forecasting Applications:")
print("- Daily weather predictions")
print("- Severe weather warnings")
print("- Agricultural planning")
print("- Energy demand forecasting")
print("- Transportation planning")
print("- Tourism industry planning")
print("- Climate change research")