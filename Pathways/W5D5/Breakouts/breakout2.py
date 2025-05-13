# Time Series Basics - Breakout Session #2
# W5D5 - Weather Data Analysis and Visualization

"""
INSTRUCTIONS:
Working in random groups, analyze and visualize the provided time series weather data.
Complete the code in each section and be prepared to discuss your findings.

GOALS:
1. Load the provided weather dataset and properly format the datetime index
2. Perform time-based aggregations at different frequencies (daily, weekly, monthly)
3. Create visualizations showing weather patterns over time
4. Identify seasonal patterns or trends in the data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# -----------------------------------------------------------------------------
# Exercise 1: Load and Prepare the Weather Data
# -----------------------------------------------------------------------------
# The data file 'weather_data.csv' contains 3 years of daily weather measurements
# for a city with columns: date, temperature, humidity, precipitation, wind_speed

# Load the dataset
# YOUR CODE HERE
# weather_data = ...

# Convert the date column to datetime and set it as the index
# YOUR CODE HERE
# weather_data['date'] = ...
# weather_data.set_index(..., inplace=...)

# Examine the data
print("Dataset overview:")
print(weather_data.head())
print("\nDataset information:")
print(weather_data.info())
print("\nBasic statistics:")
print(weather_data.describe())

# Check the date range
print(f"\nDate range: {weather_data.index.min()} to {weather_data.index.max()}")
print(f"Total days: {len(weather_data)}")

# -----------------------------------------------------------------------------
# Exercise 2: Time-Based Aggregations
# -----------------------------------------------------------------------------

# 1. Calculate monthly averages for all variables
# YOUR CODE HERE
# monthly_data = ...

print("Monthly averages (first 5 months):")
print(monthly_data.head())

# 2. Calculate seasonal statistics
# Define a function to assign seasons based on month
def assign_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

# Add a season column
# YOUR CODE HERE
# weather_data['season'] = ...

# Calculate seasonal statistics
# YOUR CODE HERE
# seasonal_stats = weather_data.groupby(...).agg({
#     'temperature': ['mean', 'min', 'max', 'std'],
#     'precipitation': ['mean', 'sum', 'max'],
#     'humidity': ['mean'],
#     'wind_speed': ['mean', 'max']
# })

print("\nSeasonal weather statistics:")
print(seasonal_stats)

# 3. Calculate rolling averages to smooth out the data
# Calculate 7-day and 30-day moving averages for temperature
# YOUR CODE HERE
# weather_data['temp_7day'] = ...
# weather_data['temp_30day'] = ...

# -----------------------------------------------------------------------------
# Exercise 3: Basic Time Series Visualization
# -----------------------------------------------------------------------------

# 1. Plot temperature over time with 7-day and 30-day moving averages
plt.figure(figsize=(12, 6))

# YOUR CODE HERE
# Add temperature and moving averages to the plot

plt.title('Temperature Over Time with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('temperature_over_time.png')

# 2. Create a monthly precipitation totals bar chart
plt.figure(figsize=(12, 6))

# Calculate monthly precipitation totals
# YOUR CODE HERE
# monthly_precip = ...

# YOUR CODE HERE
# Create a bar chart of monthly precipitation totals

plt.title('Monthly Precipitation Totals')
plt.xlabel('Month')
plt.ylabel('Total Precipitation (mm)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monthly_precipitation.png')

# -----------------------------------------------------------------------------
# Exercise 4: Identify Seasonal Patterns
# -----------------------------------------------------------------------------

# 1. Create a boxplot of temperature by month to visualize seasonal patterns
plt.figure(figsize=(14, 6))

# YOUR CODE HERE
# Group temperature data by month and create a boxplot

plt.title('Temperature Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_by_month.png')

# 2. Create a scatter plot to explore the relationship between temperature and humidity
plt.figure(figsize=(10, 6))

# YOUR CODE HERE
# Create scatter plot with points colored by season

plt.title('Temperature vs. Humidity by Season')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('temp_humidity_scatter.png')

# -----------------------------------------------------------------------------
# Exercise 5: Advanced Analysis - Year-over-Year Comparison
# -----------------------------------------------------------------------------

# 1. Create a plot comparing the same months across different years
plt.figure(figsize=(14, 8))

# Get unique years in the dataset
years = sorted(weather_data.index.year.unique())

# Create a plot for each month
# YOUR CODE HERE
# Use subplots to create a grid of plots, one for each month

plt.suptitle('Year-over-Year Comparison by Month', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('year_over_year.png')

# 2. Create a heatmap of average temperatures by month and year
plt.figure(figsize=(12, 8))

# YOUR CODE HERE
# Create a pivot table with months as rows and years as columns
# Create a heatmap visualization of this table

plt.title('Monthly Average Temperature Heatmap')
plt.tight_layout()
plt.savefig('temperature_heatmap.png')