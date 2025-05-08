# Example 2: Pandas Time Series Creation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Creating a date range
print("Creating date ranges in pandas:")
print("-" * 40)
date_range = pd.date_range(start='2023-01-01', end='2023-01-31', freq='D')
print("Daily date range for January 2023:")
print(date_range[:5], "...", date_range[-5:])
print(f"Total days: {len(date_range)}")
print()

# Different frequencies
print("Different time frequencies:")
print("-" * 40)
hourly = pd.date_range('2023-01-01', periods=24, freq='H')
print(f"Hourly (first 5): {hourly[:5]}")

weekly = pd.date_range('2023-01-01', periods=4, freq='W')
print(f"Weekly (all): {weekly}")

monthly = pd.date_range('2023-01-01', periods=12, freq='M')
print(f"Monthly (first 3): {monthly[:3]}")

business_days = pd.date_range('2023-01-01', periods=5, freq='B')
print(f"Business days (all): {business_days}")
print()

# 2. Creating a time series from scratch
print("Creating time series data:")
print("-" * 40)
# Generate random temperature data
temperatures = np.random.normal(0, 5, len(date_range))  # Random data centered at 0
temp_series = pd.Series(temperatures, index=date_range)
print("Temperature Series (first 5 days):")
print(temp_series.head())
print()

# 3. Creating a DataFrame with a date index
print("Creating a DataFrame with a date index:")
print("-" * 40)
data = {
    'temperature': np.random.normal(0, 5, len(date_range)),
    'precipitation': np.random.random(len(date_range)) * 5
}
weather_df = pd.DataFrame(data, index=date_range)
print("Weather DataFrame (first 5 rows):")
print(weather_df.head())
print()

# 4. Creating a DataFrame with string dates and converting
print("Converting string dates to datetime:")
print("-" * 40)
# Creating a DataFrame with string dates
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.0, 33.2, 34.1, 30.5],
    'precipitation': [0.0, 0.2, 0.1, 0.0, 0.5]
}
df = pd.DataFrame(data)
print("Original DataFrame with string dates:")
print(df)
print()

# Converting string dates to datetime objects
df['date'] = pd.to_datetime(df['date'])
print("With datetime column:")
print(df)
print(f"Date column type: {type(df['date'][0])}")
print()

# Setting the date as index
df.set_index('date', inplace=True)
print("With datetime index:")
print(df)
print()

# 5. Basic visualization
print("Creating a simple time series plot...")
plt.figure(figsize=(10, 4))
weather_df['temperature'].plot(marker='o')
plt.title('Daily Temperatures - January 2023')
plt.ylabel('Temperature')
plt.grid(True)
plt.tight_layout()

# Save the figure or show it if in interactive environment
plt.savefig('temperature_plot.png')
print("Plot saved as 'temperature_plot.png'")

# 6. Time series attributes
print("\nUseful time series index attributes:")
print("-" * 40)
print(f"Year: {weather_df.index.year[:5]}")
print(f"Month: {weather_df.index.month[:5]}")
print(f"Day: {weather_df.index.day[:5]}")
print(f"Day of week: {weather_df.index.dayofweek[:5]}")
print(f"Is month end?: {weather_df.index.is_month_end[:5]}")