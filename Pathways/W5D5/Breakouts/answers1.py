# Time Series Basics - Breakout Session #1 (ANSWER KEY)
# W5D5 - Weather Data Analysis

"""
INSTRUCTOR VERSION: This file contains complete solutions for the breakout session exercises.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# -----------------------------------------------------------------------------
# Exercise 1: Create a time series dataset from scratch
# -----------------------------------------------------------------------------

# Create a date range for March 2023 (all days in March)
march_dates = pd.date_range(start='2023-03-01', end='2023-03-31', freq='D')

# Generate random temperature data with a realistic pattern
# March temperatures might follow a slight upward trend as spring begins
base_temp = 10  # Starting from 10°C
trend = np.linspace(0, 5, len(march_dates))  # Gradual 5°C increase through the month
random_fluctuation = np.random.normal(0, 2, len(march_dates))  # Daily random fluctuation
temperatures = base_temp + trend + random_fluctuation

# Generate random precipitation data (values between 0 and 15mm)
# Make some days have 0 precipitation, others have varying amounts
precipitation = np.zeros(len(march_dates))
# Randomly select 40% of days to have precipitation
rainy_days = np.random.choice(len(march_dates), size=int(0.4 * len(march_dates)), replace=False)
precipitation[rainy_days] = np.random.exponential(3, size=len(rainy_days))  # Exponential distribution for rain amounts
precipitation = np.round(precipitation, 1)  # Round to 1 decimal place

# Create the weather DataFrame
weather_df = pd.DataFrame({
    'temperature': temperatures,
    'precipitation': precipitation
}, index=march_dates)

# Print the first 5 rows to verify
print("Exercise 1: Created weather dataset")
print(weather_df.head())
print()

# -----------------------------------------------------------------------------
# Exercise 2: Working with string dates
# -----------------------------------------------------------------------------

# Below is weather data with dates as strings
weather_data = {
    'date': ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05',
             '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09', '2023-03-10'],
    'temperature': [12.5, 13.2, 11.8, 14.5, 15.2, 12.8, 10.5, 11.7, 14.3, 16.5],
    'humidity': [78, 82, 76, 70, 65, 73, 88, 83, 74, 68],
    'wind_speed': [5.2, 4.8, 7.3, 6.5, 3.2, 2.5, 8.1, 6.2, 4.5, 3.8]
}

# Create a DataFrame from this dictionary
string_dates_df = pd.DataFrame(weather_data)

# 1. Convert the 'date' column to datetime format
string_dates_df['date'] = pd.to_datetime(string_dates_df['date'])

# 2. Set the date column as the index
string_dates_df.set_index('date', inplace=True)

# 3. Print the result to verify
print("Exercise 2: Converted string dates to datetime index")
print(string_dates_df.head())
print()

# -----------------------------------------------------------------------------
# Exercise 3: Time-based selection and indexing
# -----------------------------------------------------------------------------

# Using the DataFrame from Exercise 2, perform the following selections:

# 1. Select data for March 5th
march_5 = string_dates_df.loc['2023-03-05']
print("Data for March 5th:")
print(march_5)
print()

# 2. Select data from March 3rd to March 7th
march_3_to_7 = string_dates_df.loc['2023-03-03':'2023-03-07']
print("Data from March 3rd to March 7th:")
print(march_3_to_7)
print()

# 3. Get the average temperature for the first week of March (1st to 7th)
first_week_avg = string_dates_df.loc['2023-03-01':'2023-03-07', 'temperature'].mean()
print(f"Average temperature for the first week: {first_week_avg:.2f}°C")
print()

# 4. Find the day with the highest temperature
hottest_day = string_dates_df['temperature'].idxmax()
print(f"Hottest day: {hottest_day}, Temperature: {string_dates_df.loc[hottest_day, 'temperature']}°C")
print()

# -----------------------------------------------------------------------------
# Exercise 4: Basic time series visualization
# -----------------------------------------------------------------------------

# 1. Create a line plot showing temperature over time
plt.figure(figsize=(10, 6))
plt.plot(string_dates_df.index, string_dates_df['temperature'], 'o-', color='red', linewidth=2, markersize=8)
plt.title('March 2023 Temperatures', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_plot.png')

# 2. Create a plot that shows both temperature and humidity
fig, ax1 = plt.figure(figsize=(12, 6)), plt.gca()

# Plot temperature on left y-axis
color = 'tab:red'
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Temperature (°C)', color=color, fontsize=12)
ax1.plot(string_dates_df.index, string_dates_df['temperature'], 'o-', color=color, linewidth=2, markersize=8, label='Temperature')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

# Create second y-axis for humidity
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Humidity (%)', color=color, fontsize=12)
ax2.plot(string_dates_df.index, string_dates_df['humidity'], 's-', color=color, linewidth=2, markersize=8, label='Humidity')
ax2.tick_params(axis='y', labelcolor=color)

# Add title and legend
plt.title('March 2023 Temperature and Humidity', fontsize=14)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_humidity_plot.png')


# -----------------------------------------------------------------------------
# Exercise 5: Resampling and frequency conversion
# -----------------------------------------------------------------------------

# Load a larger dataset with hourly weather data for March 2023
# Note: In a real breakout session, this data might be provided in a CSV file
# For this exercise, we'll generate some simulated data

# Create an hourly datetime range for March 2023
hourly_dates = pd.date_range(start='2023-03-01', end='2023-03-31 23:00:00', freq='H')

# Create simulated hourly temperature data with daily cycles
hours = np.arange(len(hourly_dates))
daily_cycle = 3 * np.sin(2 * np.pi * hours / 24)  # Daily temperature cycle: +/- 3°C
trend = 10 + 0.2 * (hourly_dates.day - 1)  # Base temp of 10°C, increasing through the month
hourly_temps = trend + daily_cycle + np.random.normal(0, 1, len(hourly_dates))  # Add noise

# Create the hourly DataFrame
hourly_df = pd.DataFrame({
    'temperature': hourly_temps
}, index=hourly_dates)

# 1. Resample the hourly data to daily frequency (calculate the mean for each day)
daily_df = hourly_df.resample('D').mean()

# 2. Resample to get the daily minimum and maximum temperatures
daily_min_max = hourly_df.resample('D').agg({
    'temperature': ['min', 'mean', 'max']
})

# 3. Calculate the daily temperature range (max - min)
daily_range = daily_min_max['temperature', 'max'] - daily_min_max['temperature', 'min']
daily_range = pd.DataFrame({'temp_range': daily_range})

print("Daily temperature summary (first 5 days):")
print(daily_min_max.head())
print("\nDaily temperature range (first 5 days):")
print(daily_range.head())

# 4. Create a plot showing daily min, mean, and max temperatures
plt.figure(figsize=(12, 6))
plt.plot(daily_min_max.index, daily_min_max[('temperature', 'min')], 'b-', label='Min Temp')
plt.plot(daily_min_max.index, daily_min_max[('temperature', 'mean')], 'g-', label='Mean Temp')
plt.plot(daily_min_max.index, daily_min_max[('temperature', 'max')], 'r-', label='Max Temp')
plt.fill_between(daily_min_max.index, daily_min_max[('temperature', 'min')], 
                daily_min_max[('temperature', 'max')], alpha=0.2, color='gray')
plt.title('Daily Temperature Range - March 2023', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_temp_range_plot.png')