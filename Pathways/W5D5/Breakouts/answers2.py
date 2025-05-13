# Time Series Basics - Breakout Session #2 - ANSWER KEY
# W5D5 - Weather Data Analysis and Visualization

"""
INSTRUCTOR VERSION: This file contains complete solutions for the breakout session exercises.
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

# In a real-world scenario, we would load an external CSV file
# For this answer key, we'll generate synthetic data

# Generate 3 years of daily data
np.random.seed(42)  # For reproducible results
date_range = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')

# Create seasonal patterns for temperature
days = np.arange(len(date_range))
seasonal_temp = 15 + 10 * np.sin(2 * np.pi * days / 365.25)  # Seasonal cycle
trend_temp = 0.001 * days  # Slight warming trend
noise_temp = np.random.normal(0, 3, len(days))  # Random variation
temperature = seasonal_temp + trend_temp + noise_temp

# Create seasonal patterns for humidity
seasonal_humid = 60 + 20 * np.sin(2 * np.pi * (days / 365.25 + 0.5))  # Offset from temp
noise_humid = np.random.normal(0, 10, len(days))
humidity = np.clip(seasonal_humid + noise_humid, 20, 100)  # Clip to valid range

# Create precipitation data (more in certain seasons)
seasonal_precip = 2 + 2 * np.sin(2 * np.pi * (days / 365.25 + 0.3))
noise_precip = np.random.exponential(1, len(days))
precipitation = seasonal_precip * noise_precip * (np.random.random(len(days)) < 0.4)  # 40% chance of rain
precipitation = np.round(precipitation, 1)  # Round to 1 decimal

# Create wind speed data
seasonal_wind = 3 + 2 * np.sin(2 * np.pi * (days / 365.25 + 0.7))
noise_wind = np.random.gamma(2, 1, len(days))
wind_speed = seasonal_wind + noise_wind
wind_speed = np.round(wind_speed, 1)  # Round to 1 decimal

# Create the DataFrame
weather_data = pd.DataFrame({
    'date': date_range,
    'temperature': temperature,
    'humidity': humidity,
    'precipitation': precipitation,
    'wind_speed': wind_speed
})

# Convert the date column to datetime and set it as the index
weather_data['date'] = pd.to_datetime(weather_data['date'])
weather_data.set_index('date', inplace=True)

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
monthly_data = weather_data.resample('M').mean()
monthly_data.index = monthly_data.index.strftime('%Y-%m')  # Format for readability

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
weather_data['season'] = weather_data.index.map(lambda x: assign_season(x.month))

# Calculate seasonal statistics
seasonal_stats = weather_data.groupby('season').agg({
    'temperature': ['mean', 'min', 'max', 'std'],
    'precipitation': ['mean', 'sum', 'max'],
    'humidity': ['mean'],
    'wind_speed': ['mean', 'max']
})

print("\nSeasonal weather statistics:")
print(seasonal_stats)

# 3. Calculate rolling averages to smooth out the data
# Calculate 7-day and 30-day moving averages for temperature
weather_data['temp_7day'] = weather_data['temperature'].rolling(window=7, center=True).mean()
weather_data['temp_30day'] = weather_data['temperature'].rolling(window=30, center=True).mean()

# -----------------------------------------------------------------------------
# Exercise 3: Basic Time Series Visualization
# -----------------------------------------------------------------------------

# 1. Plot temperature over time with 7-day and 30-day moving averages
plt.figure(figsize=(12, 6))

# Plot the raw data and moving averages
plt.plot(weather_data.index, weather_data['temperature'], 'b-', alpha=0.3, label='Daily')
plt.plot(weather_data.index, weather_data['temp_7day'], 'g-', linewidth=1.5, label='7-day MA')
plt.plot(weather_data.index, weather_data['temp_30day'], 'r-', linewidth=2.5, label='30-day MA')

# Format the x-axis to show years
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())

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
monthly_precip = weather_data['precipitation'].resample('M').sum()

# Create a bar chart with formatted dates
plt.bar(monthly_precip.index.strftime('%Y-%m'), monthly_precip.values, color='blue', alpha=0.7)

plt.title('Monthly Precipitation Totals')
plt.xlabel('Month')
plt.ylabel('Total Precipitation (mm)')
plt.xticks(rotation=90)  # Rotate to fit all labels
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monthly_precipitation.png')

# -----------------------------------------------------------------------------
# Exercise 4: Identify Seasonal Patterns
# -----------------------------------------------------------------------------

# 1. Create a boxplot of temperature by month to visualize seasonal patterns
plt.figure(figsize=(14, 6))

# Group by month and plot
monthly_groups = weather_data.groupby(weather_data.index.month)['temperature']
box_data = [group[1].values for group in monthly_groups]
plt.boxplot(box_data)

# Format the x-axis with month names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(range(1, 13), month_names)

plt.title('Temperature Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_by_month.png')

# 2. Create a scatter plot to explore the relationship between temperature and humidity
plt.figure(figsize=(10, 6))

# Define colors for each season
season_colors = {'Winter': 'blue', 'Spring': 'green', 'Summer': 'red', 'Fall': 'orange'}

# Plot each season with different colors
for season in season_colors:
    season_data = weather_data[weather_data['season'] == season]
    plt.scatter(season_data['temperature'], season_data['humidity'], 
                alpha=0.5, label=season, color=season_colors[season])

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

# Create a subplot for each month
for i, month in enumerate(range(1, 13)):
    ax = plt.subplot(3, 4, i + 1)
    
    # Plot each year's data for this month
    for year in years:
        # Filter data for this month and year
        month_data = weather_data[(weather_data.index.month == month) & 
                                 (weather_data.index.year == year)]
        
        # Plot the data
        days_of_month = month_data.index.day
        plt.plot(days_of_month, month_data['temperature'], label=str(year))
    
    # Add title and labels
    plt.title(month_names[i])
    
    # Only add ylabel for the leftmost plots
    if i % 4 == 0:
        plt.ylabel('Temperature (°C)')
    
    # Only add xlabel for the bottom plots
    if i >= 8:
        plt.xlabel('Day of Month')
    
    # Only add legend to the first plot
    if i == 0:
        plt.legend()
    
    plt.grid(True, alpha=0.3)

plt.suptitle('Year-over-Year Comparison by Month', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('year_over_year.png')

# 2. Create a heatmap of average temperatures by month and year
plt.figure(figsize=(12, 8))

# Create a pivot table with months as rows and years as columns
pivot_data = weather_data['temperature'].groupby([weather_data.index.year, 
                                                 weather_data.index.month]).mean().unstack()

# Create a heatmap
plt.imshow(pivot_data, aspect='auto', cmap='viridis')
plt.colorbar(label='Average Temperature (°C)')

# Add labels
plt.xticks(range(len(years)), years)
plt.yticks(range(len(month_names)), month_names)
plt.xlabel('Year')
plt.ylabel('Month')

# Add text annotations
for i in range(len(pivot_data.index)):
    for j in range(len(pivot_data.columns)):
        text_color = 'white' if pivot_data.iloc[i, j] > pivot_data.values.mean() else 'black'
        plt.text(j, i, f'{pivot_data.iloc[i, j]:.1f}', 
                ha='center', va='center', color=text_color)

plt.title('Monthly Average Temperature Heatmap')
plt.tight_layout()
plt.savefig('temperature_heatmap.png')

print("\nAll visualizations have been created successfully!")