# Advanced Time Series Analysis and Visualization
# Time Series Basics - Session 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Generate sample data for 3 years of daily temperatures
# -----------------------------------------------------------------------------
np.random.seed(42)  # For reproducible results

# Create date range
start_date = '2020-01-01'
end_date = '2022-12-31'
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate temperature data with seasonal pattern and trend
days = np.arange(len(dates))
# Seasonal component with annual cycle
seasonal = 15 * np.sin(2 * np.pi * days / 365.25)
# Upward trend component
trend = 0.001 * days
# Random noise
noise = np.random.normal(0, 3, len(days))
# Base temperature
base = 15
# Combine components
temps = base + seasonal + trend + noise

# Create the DataFrame
weather_df = pd.DataFrame({
    'temperature': temps
}, index=dates)

print(f"Generated {len(weather_df)} days of temperature data from {start_date} to {end_date}")
print(weather_df.head())

# Part 1: Advanced Time Series Indexing and Selection
# -----------------------------------------------------------------------------
print("\nPART 1: ADVANCED TIME SERIES INDEXING AND SELECTION")
print("=" * 70)

# Selecting by different time periods
print("Selecting specific time periods:")
print("\nJanuary 2022:")
print(weather_df.loc['2022-01'].head())

print("\nFirst quarter of 2021:")
print(weather_df.loc['2021-Q1'].head())

print("\nAll data from summer months (Jun-Aug) across all years:")
summer_data = weather_df[(weather_df.index.month >= 6) & (weather_df.index.month <= 8)]
print(f"Summer data shape: {summer_data.shape}")
print(summer_data.head())

# More complex time-based filters
print("\nAdvanced time-based filters:")

# All Mondays
mondays = weather_df[weather_df.index.dayofweek == 0]
print(f"All Mondays: {len(mondays)} days")
print(mondays.head())

# Days where the temperature is above 25°C
hot_days = weather_df[weather_df['temperature'] > 25]
print(f"\nHot days (>25°C): {len(hot_days)} days")
print(hot_days.head())

# First day of each month
first_days = weather_df[weather_df.index.day == 1]
print(f"\nFirst day of each month: {len(first_days)} days")
print(first_days.head())

# Last 5 days of each quarter
quarter_ends = weather_df[weather_df.index.is_quarter_end]
print(f"\nQuarter end days: {len(quarter_ends)} days")
print(quarter_ends)

# Part 2: Time Series Resampling and Frequency Conversion
# -----------------------------------------------------------------------------
print("\nPART 2: TIME SERIES RESAMPLING AND FREQUENCY CONVERSION")
print("=" * 70)

# Downsampling - Reducing frequency (e.g., daily to monthly)
print("Downsampling examples:")

# Monthly averages
monthly_avg = weather_df.resample('M').mean()
print("\nMonthly averages:")
print(monthly_avg.head())

# Quarterly statistics
quarterly_stats = weather_df.resample('Q').agg({
    'temperature': ['min', 'mean', 'max', 'std']
})
print("\nQuarterly statistics:")
print(quarterly_stats.head())

# Annual statistics
yearly_stats = weather_df.resample('Y').agg({
    'temperature': ['min', 'mean', 'max', 'std', 'count']
})
print("\nYearly statistics:")
print(yearly_stats)

# Upsampling - Increasing frequency (e.g., daily to hourly)
print("\nUpsampling examples:")

# Create a small dataset with weekly data
weekly_data = weather_df.resample('W').mean()
print("\nWeekly data (original):")
print(weekly_data.head())

# Upsample to daily with different filling methods
daily_ffill = weekly_data.resample('D').ffill()  # Forward fill
daily_bfill = weekly_data.resample('D').bfill()  # Backward fill
daily_interpolate = weekly_data.resample('D').interpolate()  # Linear interpolation

print("\nUpsampled to daily (forward fill):")
print(daily_ffill.head())

print("\nUpsampled to daily (interpolation):")
print(daily_interpolate.head())

# Part 3: Advanced Time Series Visualization
# -----------------------------------------------------------------------------
print("\nPART 3: ADVANCED TIME SERIES VISUALIZATION")
print("=" * 70)

# 1. Basic time series plot with improved formatting
plt.figure(figsize=(12, 6))
plt.plot(weather_df.index, weather_df['temperature'], 'b-', alpha=0.3, label='Daily Temp')

# Add a 30-day moving average
weather_df['temp_30d_avg'] = weather_df['temperature'].rolling(window=30, center=True).mean()
plt.plot(weather_df.index, weather_df['temp_30d_avg'], 'r-', linewidth=2, label='30-Day Moving Avg')

# Format the x-axis to show appropriate dates
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())

plt.title('Daily Temperatures with 30-Day Moving Average (2020-2022)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('temperature_timeseries.png')

print("Plot saved as 'temperature_timeseries.png'")

# 2. Multiple time series plot with subplots
plt.figure(figsize=(12, 8))

# Calculate various time series derived from the original data
weather_df['temp_7d_avg'] = weather_df['temperature'].rolling(window=7).mean()
weather_df['temp_90d_avg'] = weather_df['temperature'].rolling(window=90).mean()
weather_df['temp_365d_avg'] = weather_df['temperature'].rolling(window=365).mean()

# Subplot 1: Original data with trend
plt.subplot(3, 1, 1)
plt.plot(weather_df.index, weather_df['temperature'], 'b-', alpha=0.3)
plt.plot(weather_df.index, weather_df['temp_365d_avg'], 'r-', linewidth=2)
plt.title('Daily Temperature with Annual Moving Average', fontsize=12)
plt.ylabel('Temp (°C)')
plt.grid(True, alpha=0.3)

# Subplot 2: Seasonal patterns
plt.subplot(3, 1, 2)
plt.plot(weather_df.index, weather_df['temperature'], 'b-', alpha=0.3)
plt.plot(weather_df.index, weather_df['temp_90d_avg'], 'g-', linewidth=2)
plt.title('Daily Temperature with Quarterly Moving Average', fontsize=12)
plt.ylabel('Temp (°C)')
plt.grid(True, alpha=0.3)

# Subplot 3: Short-term fluctuations
plt.subplot(3, 1, 3)
plt.plot(weather_df.index, weather_df['temperature'], 'b-', alpha=0.3)
plt.plot(weather_df.index, weather_df['temp_7d_avg'], 'c-', linewidth=2)
plt.title('Daily Temperature with Weekly Moving Average', fontsize=12)
plt.ylabel('Temp (°C)')
plt.grid(True, alpha=0.3)

# Format the x-axis for all subplots
for ax in plt.gcf().get_axes():
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.tight_layout()
plt.savefig('temperature_trends_subplots.png')

print("Plot saved as 'temperature_trends_subplots.png'")

# 3. Seasonal subseries plot
plt.figure(figsize=(14, 8))

# Calculate monthly averages
monthly_avg = weather_df.resample('M').mean()

# Create a column for month name
monthly_avg['month'] = monthly_avg.index.month_name()

# Create a column for year
monthly_avg['year'] = monthly_avg.index.year

# Group by month
for i, month in enumerate(pd.date_range(start='2020-01-01', periods=12, freq='M').month_name()):
    plt.subplot(3, 4, i+1)
    
    # Get data for this month across all years
    month_data = monthly_avg[monthly_avg['month'] == month]
    
    # Plot each year's value
    plt.plot(month_data['year'], month_data['temperature'], 'o-')
    
    plt.title(month)
    plt.ylim(min(monthly_avg['temperature'])-1, max(monthly_avg['temperature'])+1)
    
    # Only show y-axis label for leftmost plots
    if i % 4 == 0:
        plt.ylabel('Avg Temp (°C)')
    
    # Only show x-axis label for bottom plots
    if i >= 8:
        plt.xlabel('Year')
    else:
        plt.gca().xaxis.set_ticklabels([])

plt.suptitle('Monthly Temperature Comparison Across Years', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig('seasonal_subseries.png')

print("Plot saved as 'seasonal_subseries.png'")

# 4. Heatmap of temperature by month and year
plt.figure(figsize=(12, 8))

# Pivot the data to create a matrix with months as rows and years as columns
heatmap_data = monthly_avg.pivot_table(
    index=monthly_avg.index.month,
    columns=monthly_avg.index.year,
    values='temperature'
)

# Create month labels
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create the heatmap
plt.imshow(heatmap_data, cmap='viridis')

# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Temperature (°C)')

# Set ticks and labels
plt.yticks(np.arange(12), month_labels)
plt.xticks(np.arange(heatmap_data.shape[1]), heatmap_data.columns)

# Add text annotations with values
for i in range(heatmap_data.shape[0]):
    for j in range(heatmap_data.shape[1]):
        text_color = 'white' if heatmap_data.iloc[i, j] > heatmap_data.values.mean() else 'black'
        plt.text(j, i, f'{heatmap_data.iloc[i, j]:.1f}', 
                ha='center', va='center', color=text_color)

plt.title('Monthly Temperature Heatmap (2020-2022)', fontsize=14)
plt.tight_layout()
plt.savefig('temperature_heatmap.png')

print("Plot saved as 'temperature_heatmap.png'")

# 5. Year-over-year comparison
plt.figure(figsize=(12, 6))

# Reindex by day of year to compare annual cycles
years = sorted(weather_df.index.year.unique())
for year in years:
    # Get data for this year and reindex by day of year
    year_data = weather_df[weather_df.index.year == year].copy()
    year_data['dayofyear'] = year_data.index.dayofyear
    
    # Plot the data
    plt.plot(year_data['dayofyear'], year_data['temperature'], alpha=0.7, label=str(year))

plt.xlabel('Day of Year')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Comparison by Day of Year', fontsize=14)
plt.legend(title='Year')
plt.grid(True, alpha=0.3)
plt.xlim(1, 366)
plt.xticks([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366],
          ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'])

plt.tight_layout()
plt.savefig('year_over_year_comparison.png')

print("Plot saved as 'year_over_year_comparison.png'")

# 6. Anomaly detection visualization
plt.figure(figsize=(12, 6))

# Calculate the mean and standard deviation for each day of year
weather_df['dayofyear'] = weather_df.index.dayofyear
daily_means = weather_df.groupby('dayofyear')['temperature'].mean()
daily_stds = weather_df.groupby('dayofyear')['temperature'].std()

# Create a dataframe with the expected range for each date
expected_range = pd.DataFrame({
    'mean': daily_means,
    'lower': daily_means - 2 * daily_stds,
    'upper': daily_means + 2 * daily_stds
}, index=daily_means.index)

# Plot the expected range
plt.fill_between(expected_range.index, expected_range['lower'], expected_range['upper'], 
                alpha=0.2, color='blue', label='Expected Range (±2σ)')

# Plot the mean
plt.plot(expected_range.index, expected_range['mean'], 'b--', label='Mean')

# Plot the actual data for 2022 for comparison
year_2022 = weather_df[weather_df.index.year == 2022].copy()
plt.plot(year_2022['dayofyear'], year_2022['temperature'], 'r-', label='2022 Data')

# Highlight anomalies (points outside the expected range)
anomalies = year_2022[
    (year_2022['temperature'] < expected_range.loc[year_2022['dayofyear']]['lower'].values) | 
    (year_2022['temperature'] > expected_range.loc[year_2022['dayofyear']]['upper'].values)
]

plt.scatter(anomalies['dayofyear'], anomalies['temperature'], color='red', s=50,
           edgecolor='black', label='Anomalies')

plt.xlabel('Day of Year')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Anomalies in 2022 Compared to Historical Range', fontsize=14)
plt.xlim(1, 366)
plt.xticks([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366],
          ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'])
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_anomalies.png')

print("Plot saved as 'temperature_anomalies.png'")

print("\nAll visualizations have been created successfully.")