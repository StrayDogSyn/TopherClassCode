"""
Visualizing Weather Time Series Data
This example demonstrates key visualization techniques for weather data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# Set the style for better-looking plots
plt.style.use('seaborn-v0_8-whitegrid')

# Create a sample dataset with one year of daily weather data
np.random.seed(42)

# Generate dates for one year
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

# Create seasonal temperature pattern (warmer in summer, cooler in winter)
# For Northern Hemisphere
base_temp = 15  # Annual average temperature
annual_variation = 15  # Annual temperature swing

# Generate temperature with a seasonal pattern plus some random variation
temperatures = []
for date in dates:
    # Day of year from 0 to 1
    day_of_year = (date.timetuple().tm_yday - 1) / 365
    # Seasonal cycle (coldest around January 15, warmest around July 15)
    seasonal_factor = -np.cos(2 * np.pi * day_of_year)
    # Add some random daily variation
    daily_noise = np.random.normal(0, 3)  # Random daily fluctuations
    temp = base_temp + seasonal_factor * annual_variation + daily_noise
    temperatures.append(temp)

# Generate related weather variables
humidity = [max(30, min(95, 70 - 0.5 * (temp - base_temp) + np.random.normal(0, 10))) for temp in temperatures]
pressure = [1013 - 0.1 * (temp - base_temp) + np.random.normal(0, 3) for temp in temperatures]
precipitation = [max(0, np.random.exponential(2) * humidity[i]/100) for i in range(len(humidity))]
wind_speed = [max(0, 8 + np.random.normal(0, 4)) for _ in range(len(dates))]

# Create a pandas DataFrame
weather_data = pd.DataFrame({
    'date': dates,
    'temperature': temperatures,
    'humidity': humidity,
    'pressure': pressure,
    'precipitation': precipitation,
    'wind_speed': wind_speed
})

# Set the date as the index
weather_data.set_index('date', inplace=True)

# Add month and season for grouping
weather_data['month'] = weather_data.index.month
weather_data['season'] = pd.cut(
    weather_data.index.month, 
    bins=[0, 3, 6, 9, 12], 
    labels=['Winter', 'Spring', 'Summer', 'Fall'],
    include_lowest=True
)

# Display the first few rows
print("Weather time series data sample:")
print(weather_data.head())

# Basic Time Series Visualization

# 1. Basic time series plot
plt.figure(figsize=(12, 6))
plt.plot(weather_data.index, weather_data['temperature'], linewidth=1)
plt.title('Daily Temperature Over One Year')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
# Format x-axis to show month names
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.tight_layout()
print("\nCreated basic time series plot.")

# 2. Multiple variables in subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Temperature
axes[0].plot(weather_data.index, weather_data['temperature'], color='red')
axes[0].set_ylabel('Temperature (°C)')
axes[0].set_title('Temperature')

# Humidity
axes[1].plot(weather_data.index, weather_data['humidity'], color='blue')
axes[1].set_ylabel('Humidity (%)')
axes[1].set_title('Humidity')

# Precipitation
axes[2].plot(weather_data.index, weather_data['precipitation'], color='green')
axes[2].set_ylabel('Precipitation (mm)')
axes[2].set_title('Precipitation')

plt.tight_layout()
print("Created multi-variable subplot visualization.")

# 3. Highlighting seasonality with monthly boxplots
plt.figure(figsize=(14, 7))
sns.boxplot(x=weather_data.index.month_name(), y=weather_data['temperature'])
plt.title('Monthly Temperature Distribution')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
print("Created monthly boxplot to highlight seasonality.")

# 4. Dual-axis plot for related variables
fig, ax1 = plt.subplots(figsize=(12, 6))

# Temperature on left y-axis
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color=color)
ax1.plot(weather_data.index, weather_data['temperature'], color=color, alpha=0.7)
ax1.tick_params(axis='y', labelcolor=color)

# Precipitation on right y-axis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Precipitation (mm)', color=color)
ax2.plot(weather_data.index, weather_data['precipitation'], color=color, alpha=0.5)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Temperature and Precipitation Relationship')
print("Created dual-axis plot for temperature and precipitation.")

# 5. Correlation heatmap
plt.figure(figsize=(10, 8))
corr = weather_data[['temperature', 'humidity', 'pressure', 'precipitation', 'wind_speed']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Weather Variables')
plt.tight_layout()
print("Created correlation heatmap between weather variables.")

# 6. Seasonal pattern visualization
# Group by month and calculate statistics
monthly_stats = weather_data.groupby(weather_data.index.month)['temperature'].agg(['mean', 'min', 'max'])
monthly_stats.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(12, 6))
monthly_stats['mean'].plot(marker='o', linewidth=2, label='Mean')
plt.fill_between(
    monthly_stats.index,
    monthly_stats['min'],
    monthly_stats['max'],
    alpha=0.2,
    label='Min-Max Range'
)
plt.title('Monthly Temperature Pattern')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
print("Created seasonal pattern visualization with error ranges.")

# 7. Detect anomalies and visualize them
# Calculate rolling mean and standard deviation
window = 30  # 30-day window
rolling_mean = weather_data['temperature'].rolling(window=window).mean()
rolling_std = weather_data['temperature'].rolling(window=window).std()

# Define anomalies as observations that are more than 2 standard deviations from the mean
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
print("Created anomaly detection visualization.")

# 8. Interactive visualization simulation (in a real classroom, you'd use Plotly, Bokeh, or similar)
# Here we'll simulate the concept with a technique to enhance standard Matplotlib

# Create an "interactive" time series by highlighting selections
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the full data
ax.plot(weather_data.index, weather_data['temperature'], label='Temperature', color='gray', alpha=0.5)

# Highlight summer months (June, July, August)
summer = weather_data[(weather_data.index.month >= 6) & (weather_data.index.month <= 8)]
ax.plot(summer.index, summer['temperature'], color='red', linewidth=2, label='Summer')

# Highlight winter months (December, January, February)
winter = weather_data[(weather_data.index.month == 12) | (weather_data.index.month <= 2)]
ax.plot(winter.index, winter['temperature'], color='blue', linewidth=2, label='Winter')

plt.title('Interactive Time Series Visualization (Simulated)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
print("Created simulated interactive visualization highlighting seasons.")

# 9. Create a polar plot to show seasonal patterns in a circular layout
monthly_avg = weather_data.groupby('month')['temperature'].mean()
# Convert to radians for polar plot (January at top, clockwise)
theta = np.linspace(0, 2*np.pi, 12, endpoint=False)  # 12 months
# Close the circle by appending the first value at the end
r = list(monthly_avg) + [monthly_avg[1]]
theta = list(theta) + [0]  # Close the loop

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, linewidth=2, marker='o')
ax.fill(theta, r, alpha=0.25)
ax.set_xticks(theta[:-1])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.set_title('Annual Temperature Cycle', y=1.1)
plt.tight_layout()
print("Created polar plot showing annual temperature cycle.")

# In a classroom, you would save the figures with:
plt.savefig('weather_visualizations.png')
# And for interactive display:
# plt.show()

print("\nCompleted all visualizations!")
print("In a real classroom setting, you would also demonstrate interactive tools like:")
print("- Plotly for interactive time series plots")
print("- Bokeh for interactive dashboards")
print("- Matplotlib widgets for interactive exploration")
print("- Pandas plotting functions for quick exploratory plots")