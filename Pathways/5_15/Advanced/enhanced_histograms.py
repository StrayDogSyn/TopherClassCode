# Example 3: Enhanced Histograms with Seaborn and Distribution Comparisons
# This example shows how to create better-looking histograms with Seaborn and compare distributions

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set visual style for prettier plots
sns.set_style("whitegrid")

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data - temperature data for two cities
# City A: cooler climate
# City B: warmer climate
city_a_temps = np.random.normal(15, 8, 200)  # Mean 15°C, std 8°C, 200 days
city_b_temps = np.random.normal(25, 10, 200)  # Mean 25°C, std 10°C, 200 days

# Create a DataFrame for easier manipulation and visualization
data = pd.DataFrame({
    'Temperature (°C)': np.concatenate([city_a_temps, city_b_temps]),
    'City': ['City A'] * 200 + ['City B'] * 200
})

# Print the first few rows of our DataFrame
print("First 5 rows of our DataFrame:")
print(data.head())

# Plot 1: Basic histogram with Kernel Density Estimate (KDE)
plt.figure(figsize=(10, 6))
sns.histplot(city_a_temps, kde=True, bins=20)
plt.title('Histogram with Kernel Density Estimate (City A)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Comparing distributions with overlaid histograms
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='Temperature (°C)', hue='City', 
             element='step',  # Use step lines instead of bars
             stat='density',  # Use density instead of count
             common_norm=False,  # Don't normalize jointly
             alpha=0.6,  # Make slightly transparent
             bins=20)

plt.title('Comparison of Temperature Distributions Between Cities')
plt.show()

# Plot 3: Side-by-side histograms using FacetGrid
# FacetGrid allows creating separate plots for each category
g = sns.FacetGrid(data, col='City', height=5, aspect=1.2)
g.map_dataframe(sns.histplot, x='Temperature (°C)', kde=True, bins=20)
g.set_axis_labels('Temperature (°C)', 'Count')
g.set_titles('{col_name}')
g.tight_layout()
plt.show()

# Plot 4: Violin plot - another way to visualize distributions
plt.figure(figsize=(10, 6))
sns.violinplot(x='City', y='Temperature (°C)', data=data, inner='quartile')
plt.title('Violin Plot of Temperature Distributions by City')
plt.show()

# Create data with seasonal breakdown
# Let's add seasons to our temperature data
seasons = []
for temp in city_a_temps:
    if temp < 5:
        seasons.append('Winter')
    elif temp < 15:
        seasons.append('Spring/Fall')
    else:
        seasons.append('Summer')
        
for temp in city_b_temps:
    if temp < 15:
        seasons.append('Winter')
    elif temp < 25:
        seasons.append('Spring/Fall')
    else:
        seasons.append('Summer')

# Add seasons to our DataFrame
data['Season'] = seasons

# Plot 5: Distribution by city and season
plt.figure(figsize=(14, 8))
sns.histplot(data=data, x='Temperature (°C)', hue='Season', col='City',
             multiple='stack',  # Stack the distributions
             palette='viridis',  # Use a colorful palette
             bins=20)
plt.suptitle('Temperature Distributions by City and Season', y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('plot.png')

# Key takeaways:
# - Seaborn makes creating beautiful, informative histograms simpler
# - KDE lines show the smoothed distribution shape
# - Multiple distributions can be compared using overlaid, faceted, or violin plots  
# - Color can be used to add another dimension of information (seasons)
# - Different visualization types (histogram, violin) show different aspects of the data