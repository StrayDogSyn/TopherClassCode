"""
Data Preparation for Weather Time Series
This example demonstrates key preprocessing techniques for weather data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load data (in a classroom setting, you would load a real CSV file)
# Here we'll create sample data similar to what you might get from a weather station
print("Step 1: Loading weather data")

# Create a sample dataset with missing values and other issues to clean
np.random.seed(42)

# Create dates for one month of hourly data
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(hours=i) for i in range(24*30)]  # 30 days

# Create a dataframe with some realistic weather data
data = {
    'timestamp': dates,
    'temperature': np.random.normal(20, 8, len(dates)),  # Mean of 20°C with standard deviation of 8
    'humidity': np.random.normal(60, 15, len(dates)),    # Mean of 60% with standard deviation of 15
    'pressure': np.random.normal(1013, 5, len(dates)),   # Mean of 1013 hPa
    'wind_speed': np.abs(np.random.normal(10, 6, len(dates))),  # Wind speed can't be negative
    'precipitation': np.random.exponential(1, len(dates))  # Precipitation follows exponential distribution
}

df = pd.DataFrame(data)

# Introduce missing values randomly (about 5% of data)
for col in df.columns[1:]:  # Skip timestamp
    mask = np.random.random(len(df)) < 0.05
    df.loc[mask, col] = np.nan

# Create some outliers
df.loc[np.random.choice(df.index, 5), 'temperature'] = 99  # Unrealistic temperatures
df.loc[np.random.choice(df.index, 5), 'humidity'] = 150    # Impossible humidity values

# Display the raw data
print("\nRaw data with missing values and outliers:")
print(df.head())
print(f"\nMissing values per column:\n{df.isna().sum()}")

# Step 2: Basic preprocessing
print("\nStep 2: Basic preprocessing")

# Set the timestamp as index
df = df.set_index('timestamp')

# Check for duplicate timestamps and remove if any
duplicate_count = df.index.duplicated().sum()
if duplicate_count > 0:
    print(f"Found {duplicate_count} duplicate timestamps. Removing them.")
    df = df[~df.index.duplicated()]
else:
    print("No duplicate timestamps found.")

# Step 3: Handling missing values
print("\nStep 3: Handling missing values")

# Method 1: Forward fill (using previous valid observation)
df_ffill = df.ffill()

# Method 2: Interpolation (linear by default)
df_interp = df.interpolate()

# Method 3: Using rolling mean (more sophisticated)
df_rolling = df.copy()
window_size = 5  # hours
for col in df.columns:
    # Calculate rolling mean (centered)
    rolling_mean = df[col].rolling(window=window_size, center=True).mean()
    # Fill missing values with rolling mean
    mask = df[col].isna()
    df_rolling.loc[mask, col] = rolling_mean[mask]
    # Any remaining NaNs at edges use ffill and bfill
    df_rolling[col] = df_rolling[col].fillna(method='ffill').fillna(method='bfill')

# Compare results for temperature
plt.figure(figsize=(12, 6))
sample_start = 100  # Start from the 100th hour
sample_end = 150    # to the 150th hour

# Plot a slice of the data to see the difference between methods
df['temperature'][sample_start:sample_end].plot(label='Original with gaps', marker='o')
df_ffill['temperature'][sample_start:sample_end].plot(label='Forward fill', linestyle='--')
df_interp['temperature'][sample_start:sample_end].plot(label='Interpolation', linestyle='-.')
df_rolling['temperature'][sample_start:sample_end].plot(label='Rolling mean', linestyle=':')

plt.title('Comparing Methods for Handling Missing Temperature Data')
plt.legend()
plt.grid(True)

# Choose a method for subsequent analysis (interpolation often works well for weather)
df_clean = df_interp.copy()

# Step 4: Handling outliers
print("\nStep 4: Handling outliers")

# Method 1: Clip values to a reasonable range
temp_min, temp_max = -40, 50  # Reasonable temperature range in Celsius
humidity_min, humidity_max = 0, 100  # Humidity percentage range

df_clean['temperature'] = df_clean['temperature'].clip(temp_min, temp_max)
df_clean['humidity'] = df_clean['humidity'].clip(humidity_min, humidity_max)

print("After cleaning outliers:")
print(df_clean.describe())

# Step 5: Feature engineering for time series
print("\nStep 5: Feature engineering")

# Add calendar features
df_clean['hour'] = df_clean.index.hour
df_clean['day'] = df_clean.index.day
df_clean['month'] = df_clean.index.month
df_clean['day_of_week'] = df_clean.index.dayofweek  # Monday=0, Sunday=6

# Create cyclical features for time (important for capturing periodicity)
# This transforms hour into two features that preserve the cyclical nature
df_clean['hour_sin'] = np.sin(2 * np.pi * df_clean['hour'] / 24)
df_clean['hour_cos'] = np.cos(2 * np.pi * df_clean['hour'] / 24)

# Add lag features (previous values)
for lag in [1, 3, 24]:  # 1 hour ago, 3 hours ago, 24 hours ago
    df_clean[f'temp_lag_{lag}h'] = df_clean['temperature'].shift(lag)

# Add rolling features (moving averages)
for window in [3, 6, 24]:
    df_clean[f'temp_rolling_{window}h'] = df_clean['temperature'].rolling(window=window).mean()

# Display the engineered features
print("\nDataset with engineered features:")
print(df_clean.head())

# Step 6: Data splitting for time series
print("\nStep 6: Time series data splitting")

# Time series data must be split chronologically
train_end = '2023-01-21'  # First 21 days for training
test_start = '2023-01-22'  # Last 9 days for testing

train_data = df_clean[:train_end]
test_data = df_clean[test_start:]

print(f"Training data: {train_data.index.min()} to {train_data.index.max()} ({len(train_data)} records)")
print(f"Testing data: {test_data.index.min()} to {test_data.index.max()} ({len(test_data)} records)")

# Visualization of the train-test split
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Testing data', color='red')
plt.axvline(x=train_data.index.max(), color='black', linestyle='--')
plt.title('Train-Test Split for Time Series Forecasting')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Clean up NaN values created by lag features before modeling
train_data = train_data.dropna()

print("\nFinal training data shape:", train_data.shape)
print("Final testing data shape:", test_data.shape)

# In a classroom, you would save the figures with:
plt.savefig('data_preparation.png')
# And interactive display:
# plt.show()