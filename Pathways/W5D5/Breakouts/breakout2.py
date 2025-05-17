# Time Series Analysis - Weather Data Visualization
# Key concepts: time series indexing, resampling, and visualization

"""
BREAKOUT GOALS:
1. Format time series data with proper datetime indexing
2. Perform time-based aggregations (daily, weekly, monthly)
3. Visualize weather trends and seasonal patterns
4. Identify relationships between different weather measurements
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import seaborn as sns

# -----------------------------------------------------------------------------
# Exercise 1: Load and Prepare the Weather Data
# -----------------------------------------------------------------------------
# Time series data requires proper datetime formatting to enable time-based operations

# Load the dataset
weather_data = pd.read_csv('weather_data.csv')

# Convert the date column to datetime and set it as the index
# Discussion point: Why is datetime formatting critical for time series analysis?
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
# Discussion point: How do different aggregation periods reveal different patterns?

# 1. Calculate monthly averages for all variables
monthly_data = weather_data.resample('ME').mean()  # Updated from 'M' to 'ME'

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
weather_data['season'] = weather_data.index.month.map(assign_season)

# Calculate seasonal statistics
# Discussion point: How does multi-level aggregation help analyze complex patterns?
seasonal_stats = weather_data.groupby('season').agg({
    'temperature': ['mean', 'min', 'max', 'std'],
    'precipitation': ['mean', 'sum', 'max'],
    'humidity': ['mean'],
    'wind_speed': ['mean', 'max']
}).round(2).T

print("\nSeasonal weather statistics:")
print(seasonal_stats)

# 3. Calculate rolling averages to smooth out the data
# Discussion point: Why use rolling averages in time series analysis?
weather_data['temp_7day'] = weather_data['temperature'].rolling(window=7).mean()
weather_data['temp_30day'] = weather_data['temperature'].rolling(window=30).mean()

# -----------------------------------------------------------------------------
# Exercise 3: Basic Time Series Visualization
# -----------------------------------------------------------------------------
# Discussion point: What visualizations are most effective for time series data?

# 1. Plot temperature over time with 7-day and 30-day moving averages
plt.figure(figsize=(12, 6))

# Create a clean, informative multi-line chart
plt.plot(weather_data.index, weather_data['temperature'], 
         alpha=0.5, color='#3a86ff', label='Daily Temperature')
plt.plot(weather_data.index, weather_data['temp_7day'], 
         linewidth=2, color='#fb5607', label='7-Day Average')
plt.plot(weather_data.index, weather_data['temp_30day'], 
         linewidth=2.5, color='#8338ec', label='30-Day Average')

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
monthly_precip = weather_data['precipitation'].resample('ME').sum()

# Format the x-axis labels to show month and year
months = monthly_precip.index.strftime('%b %Y')
plt.bar(months, monthly_precip.values, color='#219ebc')

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
# Discussion point: How do boxplots help identify outliers and seasonal changes?

# 1. Create a boxplot of temperature by month to visualize seasonal patterns
plt.figure(figsize=(14, 6))

# Group by month and create boxplots with a color gradient
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_data = [weather_data[weather_data.index.month == m]['temperature'] for m in range(1, 13)]

# Create a gradient color scheme
colors = plt.cm.coolwarm(np.linspace(0, 1, 12))
box = plt.boxplot(month_data, patch_artist=True, tick_labels=month_labels)  # Updated from 'labels' to 'tick_labels'

# Apply the colors to each box
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Temperature Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_by_month.png')

# 2. Create a scatter plot to explore the relationship between temperature and humidity
plt.figure(figsize=(10, 6))

# Create a color-coded scatter plot by season
season_colors = {'Winter': '#0077b6', 'Spring': '#70e000', 
                 'Summer': '#ff9500', 'Fall': '#9d4edd'}

for season, color in season_colors.items():
    season_data = weather_data[weather_data['season'] == season]
    plt.scatter(season_data['temperature'], season_data['humidity'], 
               color=color, alpha=0.6, label=season)

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
# Discussion point: How can we identify multi-year trends in time series data?

# 1. Create a plot comparing the same months across different years
plt.figure(figsize=(14, 8))

# Get unique years in the dataset
years = sorted(weather_data.index.year.unique())

# Create a subplot grid for each month
fig, axes = plt.subplots(3, 4, figsize=(14, 8), sharey=True)
axes = axes.flatten()

# Plot each month with data from all years
for month in range(1, 13):
    ax = axes[month-1]
    month_name = datetime(2020, month, 1).strftime('%B')
    
    for year in years:
        # Select data for this month and year
        data = weather_data[
            (weather_data.index.year == year) & 
            (weather_data.index.month == month)
        ]
        # Plot the temperature data
        days = data.index.day
        ax.plot(days, data['temperature'], label=str(year))
    
    ax.set_title(month_name)
    ax.set_xlabel('Day')
    if month % 4 == 1:
        ax.set_ylabel('Temperature (°C)')
    ax.grid(True, alpha=0.3)

# Add a common legend at the bottom
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=len(years), bbox_to_anchor=(0.5, 0.02))

plt.suptitle('Year-over-Year Comparison by Month', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.1)
plt.savefig('year_over_year.png')

# 2. Create a heatmap of average temperatures by month and year
plt.figure(figsize=(12, 8))

# Create pivot table of average temperatures by month and year
monthly_temp_pivot = weather_data['temperature'].groupby([
    weather_data.index.year, 
    weather_data.index.month
]).mean().unstack()

# Set proper row and column labels
monthly_temp_pivot.index.name = 'Year'
monthly_temp_pivot.columns = [datetime(2020, m, 1).strftime('%b') for m in monthly_temp_pivot.columns]

# Create heatmap
sns.heatmap(monthly_temp_pivot, cmap='coolwarm', annot=True, fmt='.1f',
            linewidths=.5, cbar_kws={'label': 'Temperature (°C)'})

plt.title('Monthly Average Temperature Heatmap')
plt.tight_layout()
plt.savefig('temperature_heatmap.png')

# -----------------------------------------------------------------------------
# Exercise 6: Lollipop Chart Visualization with Pastel Gradients
# -----------------------------------------------------------------------------
# Discussion point: How do lollipop charts combine the clarity of bar charts with the elegance of scatter plots?

# Create a monthly temperature range lollipop chart with pastel gradient
plt.figure(figsize=(14, 8))

# Calculate min and max temperatures for each month across all years
monthly_temp_min = weather_data.groupby(weather_data.index.month)['temperature'].min()
monthly_temp_max = weather_data.groupby(weather_data.index.month)['temperature'].max()
monthly_temp_mean = weather_data.groupby(weather_data.index.month)['temperature'].mean()

# Print available month indices for debugging
print("Available months in the data:")
print("Min temp months:", monthly_temp_min.index.tolist())
print("Max temp months:", monthly_temp_max.index.tolist())
print("Mean temp months:", monthly_temp_mean.index.tolist())

# Set up x-axis positions
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x = np.arange(1, 13)

# Create pastel color gradient
pastel_colors = plt.cm.Pastel1(np.linspace(0, 1, 12))

# Create arrays to store values for each month (initialize with NaN)
min_temps = np.full(12, np.nan)
max_temps = np.full(12, np.nan)
mean_temps = np.full(12, np.nan)

# Fill in the arrays for available months
for month in monthly_temp_min.index:
    if 1 <= month <= 12:  # Ensure the month index is valid
        min_temps[month-1] = monthly_temp_min[month]
        max_temps[month-1] = monthly_temp_max[month]
        mean_temps[month-1] = monthly_temp_mean[month]

# Plot the stems (lines)
for i in range(len(x)):
    # Only plot if we have data for this month
    if not np.isnan(min_temps[i]) and not np.isnan(max_temps[i]):
        plt.plot([x[i], x[i]], [min_temps[i], max_temps[i]], 
                color=pastel_colors[i], 
                linewidth=2.5,
                alpha=0.7)

# Filter out months with no data
valid_months = ~np.isnan(min_temps)
x_valid = x[valid_months]
min_valid = min_temps[valid_months]
max_valid = max_temps[valid_months]
mean_valid = mean_temps[valid_months]
colors_valid = pastel_colors[valid_months]

# Plot the min temperature circles
plt.scatter(x_valid, min_valid, 
            s=120, 
            color=colors_valid,
            edgecolor='white', 
            linewidth=1.5, 
            zorder=3, 
            label='Min Temp')

# Plot the max temperature circles
plt.scatter(x_valid, max_valid, 
            s=120, 
            color=colors_valid,
            edgecolor='white', 
            linewidth=1.5, 
            zorder=3, 
            label='Max Temp')

# Plot the mean temperature as diamonds
plt.scatter(x_valid, mean_valid, 
            s=100, 
            color='white',
            edgecolor=colors_valid, 
            linewidth=1.5, 
            zorder=4, 
            marker='D', 
            label='Mean Temp')

# Customize the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(x, months)
plt.title('Monthly Temperature Ranges (Lollipop Chart)', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend()

# Add a subtle background gradient
gradient = np.linspace(0, 1, 100).reshape(-1, 1)
# Calculate min and max temps, filtering out NaN values
valid_min = np.nanmin(min_temps)
valid_max = np.nanmax(max_temps)
plt.imshow(gradient, aspect='auto', extent=[0, 13, valid_min-3, valid_max+3], 
           cmap='Pastel2_r', alpha=0.15, zorder=0)

plt.tight_layout()
plt.savefig('temperature_lollipop.png')
plt.show()