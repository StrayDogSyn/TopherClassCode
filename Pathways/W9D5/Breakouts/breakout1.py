"""
BREAKOUT ROOM 1: WEATHER DATA EXPLORATION

In this activity, you'll work in small groups to:
1. Load a weather dataset
2. Clean and preprocess the data
3. Create visualizations that reveal patterns
4. Identify and discuss key patterns found

Follow the instructions below and complete the code where indicated.
"""


# Part 1: Load the Dataset
# -----------------------
# We've provided a CSV file with historical weather data
# The file contains daily weather measurements for a city over one year

# First, we need to import the libraries we'll use
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import numpy as np  # For numerical operations
import seaborn as sns  # For advanced statistical visualizations

# Set matplotlib to non-interactive backend to prevent display issues
plt.ioff()  # Turn off interactive mode
# Set up matplotlib for better looking plots
plt.style.use('default')  # Use default matplotlib style
plt.rcParams['figure.figsize'] = (10, 6)  # Set default figure size

# Load the CSV file using pandas
# pd.read_csv() reads a CSV file and creates a DataFrame (like a spreadsheet in Python)
weather_data = pd.read_csv('weather_data.csv')

# Print the first 5 rows to understand the data structure
# .head() shows the first few rows of our dataset
print("First 5 rows of the dataset:")
print(weather_data.head())


# Part 2: Data Inspection and Cleaning
# -----------------------------------
# Examine the dataset and handle any issues

# Check basic information about the dataset
# .info() gives us an overview of the dataset structure
print("\nDataset Information:")
print(weather_data.info())

# .describe() gives us statistical summary of numerical columns
print("\nStatistical Summary:")
print(weather_data.describe())

# Check for missing values in each column
# .isna() returns True where values are missing, .sum() counts them
print("\nMissing values in each column:")
missing_values = weather_data.isna().sum()
print(missing_values)

# Handle missing values if any exist
# For this example, we'll fill missing values with the column mean
# This is a simple approach - in real projects, you might use more sophisticated methods
if missing_values.sum() > 0:
    print("\nFilling missing values with column means...")
    # .fillna() replaces missing values
    weather_data = weather_data.fillna(weather_data.mean(numeric_only=True))
else:
    print("\nNo missing values found - data is clean!")

# Convert the 'date' column to datetime format
# pd.to_datetime() converts text dates to Python datetime objects
# This allows us to work with dates more easily (sorting, extracting months, etc.)
print("\nConverting date column to datetime format...")
weather_data['date'] = pd.to_datetime(weather_data['date'])

# Set the 'date' column as the index
# This makes it easier to work with time series data
print("Setting date as index...")
weather_data = weather_data.set_index('date')

# Ensure the index is recognized as a DatetimeIndex for proper attribute access
weather_data.index = pd.to_datetime(weather_data.index)

# Check for and handle any outliers in the temperature column
# We'll use a simple approach: identify values that are extremely high or low
print("\nChecking for temperature outliers...")
# Calculate quartiles (25th and 75th percentiles)
Q1 = weather_data['temperature'].quantile(0.25)
Q3 = weather_data['temperature'].quantile(0.75)
IQR = Q3 - Q1  # Interquartile Range

# Define outlier boundaries (standard statistical method)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Count outliers
outliers = weather_data[(weather_data['temperature'] < lower_bound) | 
                      (weather_data['temperature'] > upper_bound)]
print(f"Found {len(outliers)} temperature outliers")

# For this exercise, we'll keep the outliers as they might be real extreme weather events
# In a real project, you'd investigate these more carefully


# Part 3: Feature Engineering
# --------------------------
# Add useful features for time series analysis

# Add a column for month
# Extract month from the datetime index using a more explicit approach
print("\nAdding month and season columns...")
# Use a simple loop to extract months (novice-friendly approach)
months = []
for date in weather_data.index:
    months.append(date.month)
weather_data['month'] = months

# Add a column for season
# We'll create a function to map months to seasons
def get_season(month):
    """
    Function to determine season based on month number
    This is a simple approach assuming Northern Hemisphere seasons
    """
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:  # months 9, 10, 11
        return 'Fall'

# Apply the function to create the season column
# .apply() runs our function on each value in the month column
weather_data['season'] = weather_data['month'].apply(get_season)

# Display the first few rows with new features
print("Dataset with new features:")
print(weather_data.head())


# Part 4: Data Visualization
# -------------------------
# Create at least THREE different visualizations that reveal patterns in the data

# VISUALIZATION 1 - Plot temperature over time
# Create a line plot showing the temperature trends throughout the year
print("\nCreating Visualization 1: Temperature over time...")

# Create a new figure with a specific size
plt.figure(figsize=(12, 6))

# Plot temperature as a line chart
# The index (dates) will be on x-axis, temperature on y-axis
plt.plot(weather_data.index, weather_data['temperature'], 
         color='blue', linewidth=1, alpha=0.7)

# Add labels and title to make the plot clear
plt.title('Daily Temperature Throughout the Year', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a grid to make it easier to read values
plt.grid(True, alpha=0.3)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.savefig('temperature_over_time.png', dpi=150, bbox_inches='tight')
plt.close()  # Close the figure to free memory
print("Saved: temperature_over_time.png")

# VISUALIZATION 2 - Create a box plot showing seasonal temperature patterns
print("\nCreating Visualization 2: Seasonal temperature patterns...")

# Create a new figure
plt.figure(figsize=(10, 6))

# Create a box plot grouped by season
# Box plots show the distribution of data (median, quartiles, outliers)
seasons_order = ['Winter', 'Spring', 'Summer', 'Fall']  # Define order for logical progression
weather_data.boxplot(column='temperature', by='season', ax=plt.gca())

# Customize the plot
plt.title('Temperature Distribution by Season', fontsize=16, fontweight='bold')
plt.xlabel('Season', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Remove the automatic title that boxplot adds
plt.suptitle('')  # This removes the default title

# Adjust layout
plt.tight_layout()
plt.savefig('seasonal_temperature_boxplot.png', dpi=150, bbox_inches='tight')
plt.close()  # Close the figure to free memory
print("Saved: seasonal_temperature_boxplot.png")

# VISUALIZATION 3 - Create a scatter plot showing relationship between humidity and temperature
print("\nCreating Visualization 3: Temperature vs Humidity relationship...")

# Create a new figure
plt.figure(figsize=(10, 6))

# Create a scatter plot with color coding by season
# This helps us see if the relationship changes by season
seasons = weather_data['season'].unique()
colors = ['blue', 'green', 'red', 'orange']  # Different color for each season

# Plot each season separately so we can color-code them
for i, season in enumerate(seasons_order):
    # Filter data for this season
    season_data = weather_data[weather_data['season'] == season]
    
    # Create scatter plot for this season
    plt.scatter(season_data['humidity'], season_data['temperature'], 
               color=colors[i], label=season, alpha=0.6, s=30)

# Add labels and title
plt.title('Temperature vs Humidity by Season', fontsize=16, fontweight='bold')
plt.xlabel('Humidity (%)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Add legend to show what each color represents
plt.legend()

# Add grid for easier reading
plt.grid(True, alpha=0.3)

# Adjust layout
plt.tight_layout()
plt.savefig('temperature_humidity_scatter.png', dpi=150, bbox_inches='tight')
plt.close()  # Close the figure to free memory
print("Saved: temperature_humidity_scatter.png")

# BONUS VISUALIZATION - Monthly average temperature with precipitation
print("\nCreating Bonus Visualization: Monthly patterns...")

# Calculate monthly averages
monthly_stats = weather_data.groupby('month').agg({
    'temperature': 'mean',
    'precipitation': 'mean',
    'humidity': 'mean'
}).round(1)

# Create a figure with two y-axes (dual axis plot)
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot temperature on the first y-axis
color1 = 'tab:red'
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Average Temperature (°C)', color=color1, fontsize=12)
ax1.plot(monthly_stats.index, monthly_stats['temperature'], 
         color=color1, marker='o', linewidth=2, markersize=6)
ax1.tick_params(axis='y', labelcolor=color1)

# Create a second y-axis for precipitation
ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('Average Precipitation (mm)', color=color2, fontsize=12)
ax2.bar(monthly_stats.index, monthly_stats['precipitation'], 
        color=color2, alpha=0.6, width=0.6)
ax2.tick_params(axis='y', labelcolor=color2)

# Add title
plt.title('Monthly Temperature and Precipitation Patterns', fontsize=16, fontweight='bold')

# Set month labels
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels(month_names)

# Adjust layout
plt.tight_layout()
plt.savefig('monthly_temperature_precipitation.png', dpi=150, bbox_inches='tight')
plt.close()  # Close the figure to free memory
print("Saved: monthly_temperature_precipitation.png")


# Part 5: Pattern Identification
# ----------------------------
# Analyze your visualizations and identify patterns

"""
Write your observations below:

1. Daily patterns observed:
   - Temperature shows clear seasonal variation throughout the year
   - Daily temperatures can fluctuate significantly (visible as noise in the line plot)
   - There appears to be a general warming trend from winter through summer, then cooling in fall
   - Some extreme temperature events (outliers) occur, possibly representing weather anomalies

2. Seasonal trends identified:
   - Winter months (Dec-Feb) show the lowest temperatures, typically below 0°C
   - Summer months likely show the highest temperatures (visible in the seasonal box plot)
   - Spring and fall show intermediate temperatures with more variation
   - The box plot reveals that winter has less temperature variation than other seasons

3. Relationships between variables:
   - The scatter plot shows the relationship between humidity and temperature varies by season
   - Different seasons cluster in different areas of the humidity-temperature space
   - There may be an inverse relationship between humidity and temperature in some seasons
   - Seasonal patterns are clearly distinguishable in the scatter plot

4. Any anomalies or unusual patterns:
   - Some extreme temperature outliers were detected (shown in our outlier analysis)
   - Precipitation patterns may not correlate directly with temperature
   - The dual-axis plot shows how precipitation and temperature patterns differ throughout the year
   - Winter months may have different precipitation patterns compared to summer

5. How might these patterns affect weather forecasting?
   - Seasonal patterns provide a baseline for temperature predictions
   - Understanding humidity-temperature relationships helps predict comfort levels
   - Identifying outliers helps forecasters recognize unusual weather events
   - Monthly averages can be used as historical baselines for comparison
   - The cyclical nature of weather makes historical patterns valuable for prediction models

"""

# Print summary statistics for final analysis
print("\n" + "="*60)
print("FINAL DATA SUMMARY")
print("="*60)

print(f"\nDataset covers from {weather_data.index.min().strftime('%B %d, %Y')} to {weather_data.index.max().strftime('%B %d, %Y')}")
print(f"Total number of days: {len(weather_data)}")

print("\nTemperature Statistics:")
print(f"  Average temperature: {weather_data['temperature'].mean():.1f}°C")
print(f"  Minimum temperature: {weather_data['temperature'].min():.1f}°C")
print(f"  Maximum temperature: {weather_data['temperature'].max():.1f}°C")

print("\nSeasonal Temperature Averages:")
seasonal_temps = weather_data.groupby('season')['temperature'].mean().round(1)
for season, temp in seasonal_temps.items():
    print(f"  {season}: {temp}°C")

print("\nOther Weather Variables:")
print(f"  Average humidity: {weather_data['humidity'].mean():.1f}%")
print(f"  Total precipitation: {weather_data['precipitation'].sum():.1f}mm")
print(f"  Average wind speed: {weather_data['wind_speed'].mean():.1f} km/h")

# Save plots with a descriptive filename
# Note: In a real environment, you would uncomment this line
# plt.savefig('weather_exploration_group_analysis.png', dpi=300, bbox_inches='tight')

print("\nCompleted the Weather Data Exploration activity!")
print("All visualizations have been generated and patterns have been analyzed.")
print("Ready for class presentation and discussion!")