"""
BREAKOUT ROOM 1: WEATHER DATA EXPLORATION - ANSWER KEY

This answer key provides sample solutions for the weather data exploration activity.
Students may have different but equally valid approaches.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Part 1: Load the Dataset
# -----------------------
# Load the CSV file with historical weather data

# ANSWER:
# weather_data = pd.read_csv('weather_data.csv')
weather_data = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'temperature': [5.2, 6.1, 4.3, 7.8, 9.2, 8.5, 7.6, 6.8, 8.9, 11.2, 13.5, 15.6, 
                   14.2, 16.8, 18.5, 17.9, 19.2, 21.5, 23.8, 25.6, 27.3, 26.8, 28.1, 
                   27.5, 26.2, 24.8, 23.5, 25.6, 26.7, 27.8, 29.2] + [22.5] * 334,  # First month detailed, rest simplified
    'humidity': [65, 72, 78, 68, 62, 58, 64, 72, 75, 69, 64, 58, 
                54, 52, 48, 51, 55, 49, 45, 42, 38, 41, 36, 39,
                42, 47, 52, 48, 44, 41, 38] + [55] * 334,
    'pressure': [1012.5, 1010.2, 1008.7, 1009.5, 1011.2, 1013.5, 1014.8, 1015.2, 
                1014.7, 1013.6, 1012.8, 1011.5, 1009.8, 1008.5, 1010.2, 1012.6, 
                1013.8, 1014.5, 1015.2, 1014.8, 1013.6, 1012.4, 1011.8, 1010.5,
                1009.8, 1011.2, 1012.7, 1013.5, 1014.2, 1013.8, 1012.5] + [1013.0] * 334,
    'precipitation': [0.0, 2.5, 5.2, 0.5, 0.0, 0.0, 1.2, 0.8, 2.1, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0, 0.5, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5,
                     2.8, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0] + [0.0] * 334,
    'wind_speed': [12.5, 15.2, 18.7, 14.2, 10.5, 8.2, 9.7, 11.2, 13.8, 12.5, 9.8, 7.5,
                  6.8, 8.2, 9.5, 10.2, 8.7, 7.5, 6.2, 5.8, 7.2, 8.5, 10.2, 12.5,
                  14.8, 13.2, 11.5, 9.8, 8.5, 7.2, 8.5] + [10.0] * 334
})

# Print the first 5 rows to understand the data structure
print("First 5 rows of the dataset:")
print(weather_data.head())


# Part 2: Data Inspection and Cleaning
# -----------------------------------
# Examine the dataset and handle any issues

# ANSWER: Check basic information about the dataset
print("\nBasic information about the dataset:")
print(weather_data.info())
print("\nStatistical summary:")
print(weather_data.describe())

# ANSWER: Check for missing values in each column
print("\nMissing values per column:")
missing_values = weather_data.isna().sum()
print(missing_values)

# ANSWER: Handle missing values appropriately
# If there are missing values, interpolation works well for weather data
if missing_values.sum() > 0:
    # For temperature, humidity, pressure - interpolate
    for col in ['temperature', 'humidity', 'pressure']:
        if col in weather_data.columns and missing_values[col] > 0:
            weather_data[col] = weather_data[col].interpolate()
    
    # For precipitation, wind - forward fill (assuming persistence)
    for col in ['precipitation', 'wind_speed']:
        if col in weather_data.columns and missing_values[col] > 0:
            weather_data[col] = weather_data[col].fillna(method='ffill').fillna(method='bfill')
    
    print("\nAfter handling missing values:")
    print(weather_data.isna().sum())

# ANSWER: Convert the 'date' column to datetime format
weather_data['date'] = pd.to_datetime(weather_data['date'])

# ANSWER: Set the 'date' column as the index
weather_data = weather_data.set_index('date')

# ANSWER: Check for and handle outliers in the temperature column
# Reasonable temperature range (adjust based on your location)
temp_min, temp_max = -40, 50  # Celsius

# Check for outliers
temp_outliers = weather_data[(weather_data['temperature'] < temp_min) | 
                             (weather_data['temperature'] > temp_max)]
if len(temp_outliers) > 0:
    print(f"\nFound {len(temp_outliers)} temperature outliers:")
    print(temp_outliers)
    
    # Clip temperatures to a reasonable range
    weather_data['temperature'] = weather_data['temperature'].clip(temp_min, temp_max)
    print("\nAfter handling outliers:")
    print(weather_data['temperature'].describe())


# Part 3: Feature Engineering
# --------------------------
# Add useful features for time series analysis

# ANSWER: Add columns for month and season
weather_data['month'] = weather_data.index.month
weather_data['month_name'] = weather_data.index.month_name()
weather_data['day_of_year'] = weather_data.index.dayofyear

# Create season column
weather_data['season'] = pd.cut(
    weather_data.index.month, 
    bins=[0, 3, 6, 9, 12], 
    labels=['Winter', 'Spring', 'Summer', 'Fall'],
    include_lowest=True
)

print("\nDataset with added features:")
print(weather_data.head())


# Part 4: Data Visualization
# -------------------------
# Create different visualizations that reveal patterns in the data

# ANSWER: VISUALIZATION 1 - Temperature Over Time
plt.figure(figsize=(12, 6))
plt.plot(weather_data.index, weather_data['temperature'], linewidth=1)
plt.title('Daily Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('viz1_temperature_trend.png')
print("\nCreated Visualization 1: Temperature trend over time")

# ANSWER: VISUALIZATION 2 - Seasonal Patterns (Monthly Boxplot)
plt.figure(figsize=(14, 7))
sns.boxplot(x='month_name', y='temperature', data=weather_data.reset_index())
plt.title('Monthly Temperature Distribution')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('viz2_monthly_boxplot.png')
print("Created Visualization 2: Monthly temperature distribution")

# ANSWER: VISUALIZATION 3 - Correlation Heatmap
# Select only numeric columns for correlation
numeric_cols = weather_data.select_dtypes(include=['float64', 'int64']).columns
# Exclude the month and day_of_year columns
numeric_cols = [col for col in numeric_cols if col not in ['month', 'day_of_year']]

plt.figure(figsize=(10, 8))
corr = weather_data[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Weather Variables')
plt.tight_layout()
plt.savefig('viz3_correlation_heatmap.png')
print("Created Visualization 3: Correlation heatmap")

# ANSWER: BONUS - Advanced Visualization 
# Detect and visualize anomalies in temperature

# Calculate rolling statistics
window = 30  # 30-day window for smooth trends
rolling_mean = weather_data['temperature'].rolling(window=window).mean()
rolling_std = weather_data['temperature'].rolling(window=window).std()

# Define anomalies as observations more than 2 standard deviations from the mean
anomalies = weather_data[
    (weather_data['temperature'] > rolling_mean + 2*rolling_std) | 
    (weather_data['temperature'] < rolling_mean - 2*rolling_std)
]

plt.figure(figsize=(12, 6))
plt.plot(weather_data.index, weather_data['temperature'], label='Temperature', linewidth=1)
plt.plot(rolling_mean.index, rolling_mean, label=f'{window}-day Rolling Mean', color='red', linewidth=2)
plt.fill_between(
    rolling_mean.index,
    rolling_mean - 2*rolling_std,
    rolling_mean + 2*rolling_std,
    color='red',
    alpha=0.2,
    label='95% Confidence Interval'
)
plt.scatter(anomalies.index, anomalies['temperature'], color='green', label='Anomalies', s=50)
plt.title('Temperature Anomaly Detection')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('viz4_bonus_anomalies.png')
print("Created Bonus Visualization: Temperature anomaly detection")
