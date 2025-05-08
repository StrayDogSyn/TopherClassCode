# Example 3: Time Series Indexing and Operations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample weather dataset
np.random.seed(42)  # For reproducible results

# Create a full year of daily data for 2023
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')

# Create simulated temperature data with seasonal pattern
days = np.arange(len(dates))
temps = 20 + 15 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 3, len(days))

# Create random precipitation data (higher in certain seasons)
precip_pattern = 2 + 1.5 * np.sin(2 * np.pi * (days / 365 + 0.3))  # Offset from temp
precip = np.maximum(0, precip_pattern + np.random.normal(0, 1, len(days)))

# Create DataFrame
weather_df = pd.DataFrame({
    'temperature': temps,
    'precipitation': precip
}, index=dates)

print("Sample weather data for 2023:")
print(weather_df.head())
print()

# 1. Basic selection by date
print("Time-based selections:")
print("-" * 40)
print("Data for January 15, 2023:")
print(weather_df.loc['2023-01-15'])
print()

print("First week of February:")
print(weather_df.loc['2023-02-01':'2023-02-07'])
print()

# 2. Selecting by time period strings
print("Selecting using period strings:")
print("-" * 40)
print("All January data:")
print(weather_df.loc['2023-01'].head())  # Just show the first few rows
print(f"Number of days in January: {len(weather_df.loc['2023-01'])}")
print()

print("First quarter data:")
q1_data = weather_df.loc['2023-Q1']
print(f"First 5 days of Q1: {q1_data.head()}")
print(f"Number of days in Q1: {len(q1_data)}")
print()

# 3. Selecting using datetime attributes
print("Selecting using datetime attributes:")
print("-" * 40)
print("All Sundays in the dataset:")
sundays = weather_df[weather_df.index.dayofweek == 6]  # 6 = Sunday
print(sundays.head())
print(f"Number of Sundays: {len(sundays)}")
print()

print("Summer months (June, July, August):")
summer = weather_df[(weather_df.index.month >= 6) & (weather_df.index.month <= 8)]
print(summer.head())
print(f"Number of days in summer: {len(summer)}")
print()

print("First day of each month:")
first_days = weather_df[weather_df.index.day == 1]
print(first_days)
print()

# 4. Basic time series statistics
print("Time series statistics:")
print("-" * 40)
print("Monthly average temperatures:")
monthly_temps = weather_df['temperature'].resample('M').mean()
print(monthly_temps)
print()

print("Seasonal statistics:")
# Define seasons
weather_df['season'] = 'Winter'  # Default
weather_df.loc[weather_df.index.month.isin([3, 4, 5]), 'season'] = 'Spring'
weather_df.loc[weather_df.index.month.isin([6, 7, 8]), 'season'] = 'Summer'
weather_df.loc[weather_df.index.month.isin([9, 10, 11]), 'season'] = 'Fall'

seasonal_stats = weather_df.groupby('season').agg({
    'temperature': ['mean', 'min', 'max', 'std'],
    'precipitation': ['mean', 'sum', 'max']
})
print(seasonal_stats)
print()

# 5. Rolling statistics
print("Computing rolling statistics:")
print("-" * 40)
# 7-day rolling average temperature
weather_df['temp_7day_avg'] = weather_df['temperature'].rolling(window=7).mean()
print("7-day rolling average temperatures (first 10 days):")
print(weather_df[['temperature', 'temp_7day_avg']].head(10))
print()

# 6. Finding extreme values
print("Finding extreme values:")
print("-" * 40)
hottest_day = weather_df['temperature'].idxmax()
coldest_day = weather_df['temperature'].idxmin()
rainiest_day = weather_df['precipitation'].idxmax()

print(f"Hottest day: {hottest_day}, Temperature: {weather_df.loc[hottest_day, 'temperature']:.1f}°C")
print(f"Coldest day: {coldest_day}, Temperature: {weather_df.loc[coldest_day, 'temperature']:.1f}°C")
print(f"Rainiest day: {rainiest_day}, Precipitation: {weather_df.loc[rainiest_day, 'precipitation']:.1f}mm")
print()

# 7. Time series visualization with seasonal comparison
print("Creating comparative time series visualization...")
plt.figure(figsize=(12, 6))

# Create monthly averages
monthly_avg = weather_df.resample('M').mean()

# Plot temperature
plt.subplot(2, 1, 1)
plt.plot(monthly_avg.index, monthly_avg['temperature'], 'r-o', label='Monthly Avg Temp')
plt.title('Monthly Average Temperature and Precipitation - 2023')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()

# Plot precipitation
plt.subplot(2, 1, 2)
plt.bar(monthly_avg.index, monthly_avg['precipitation'], color='blue', label='Monthly Avg Precip')
plt.ylabel('Precipitation (mm)')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig('monthly_weather_comparison.png')
print("Plot saved as 'monthly_weather_comparison.png'")