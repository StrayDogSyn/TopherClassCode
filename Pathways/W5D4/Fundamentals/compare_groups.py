# Example 3: Comparing Multiple Groups with Box Plots
# This example shows how to compare distributions across multiple categories and groups

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Create data with multiple groups and categories
# We'll simulate temperature data for different seasons and time periods
categories = ['Winter', 'Spring', 'Summer', 'Fall']  # Seasons
groups = ['Morning', 'Afternoon']                    # Time of day

# Create empty lists to store our data
all_temps = []      # All temperature values
all_seasons = []    # Season for each temperature
all_times = []      # Time of day for each temperature

# Generate synthetic temperature data
# For each season and time of day combination:
for season in categories:
    # Set different base temperatures for each season
    if season == 'Winter':
        base_temp = 0    # Cold
    elif season == 'Spring':
        base_temp = 15   # Mild
    elif season == 'Summer':
        base_temp = 25   # Hot
    else:  # Fall
        base_temp = 10   # Cool
    
    # For each time of day:
    for time in groups:
        # Afternoons are warmer than mornings
        time_adjustment = 5 if time == 'Afternoon' else 0
        
        # Generate 50 random temperatures with some variance
        temperatures = np.random.normal(
            base_temp + time_adjustment,  # Mean temperature
            3,                            # Standard deviation (variability)
            50                            # Number of data points
        )
        
        # Add these data points to our lists
        all_temps.extend(temperatures)
        all_seasons.extend([season] * 50)
        all_times.extend([time] * 50)

# Create a DataFrame from our lists
data = pd.DataFrame({
    'temperature': all_temps,
    'season': all_seasons,
    'time': all_times
})

# Show the first few rows
print("First 5 rows of our weather DataFrame:")
print(data.head())

# Create a figure
plt.figure(figsize=(12, 6))

# Create a grouped box plot
# x: category for x-axis (seasons)
# y: values for y-axis (temperatures)
# hue: grouping variable (time of day)
sns.boxplot(x='season', y='temperature', hue='time', data=data)

# Add title and labels
plt.title('Temperature Distributions by Season and Time of Day')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.legend(title='Time of Day')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.savefig('plot.png')

# Interpretation tips:
# - Compare median lines to see differences between groups
# - Look at box sizes to compare variability
# - Check for outliers (points beyond the whiskers)
# - Notice how the difference between morning and afternoon varies by season