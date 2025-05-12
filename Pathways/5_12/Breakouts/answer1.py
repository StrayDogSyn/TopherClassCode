# Central Tendency Analysis - ANSWER KEY
# ======================================

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Temperature data for different cities (°C)
city_temps = {
    'Phoenix': [28.5, 29.2, 30.1, 31.5, 42.8, 29.8, 30.2],
    'Seattle': [12.3, 13.1, 12.9, 13.2, 12.8, 11.9, 13.0],
    'Miami': [26.5, 26.8, 27.2, 45.1, 26.9, 27.3, 26.5],
    'Chicago': [18.2, 3.5, 16.8, 17.2, 16.5, 17.9, 18.1],
    'Denver': [15.6, 16.2, 2.3, 14.8, 15.9, 16.3, -3.7]
}

# Create a DataFrame from the city temperature data
temps_df = pd.DataFrame(city_temps)
print("Temperature data by city:")
print(temps_df)

# Calculate mean, median, and mode for each city
city_means = {}
city_medians = {}
city_modes = {}

for city, temps in city_temps.items():
    city_means[city] = np.mean(temps)
    city_medians[city] = np.median(temps)
    mode_result = stats.mode(temps)
    city_modes[city] = mode_result.mode[0]

# Create a table to compare measures across cities
comparison_df = pd.DataFrame({
    'Mean': city_means,
    'Median': city_medians,
    'Mode': city_modes
}).T  # Transpose to have cities as columns

# Format to 1 decimal place
comparison_df = comparison_df.round(1)
print("\nComparison of central tendency measures (°C):")
print(comparison_df)

# Calculate the differences between mean and median
diff_df = pd.DataFrame({
    'City': city_means.keys(),
    'Mean': city_means.values(),
    'Median': city_medians.values()
})
diff_df['Mean-Median Difference'] = (diff_df['Mean'] - diff_df['Median']).round(1)
print("\nDifference between mean and median:")
print(diff_df.set_index('City'))

# Create boxplots to visualize data distribution and outliers
plt.figure(figsize=(12, 6))
plt.boxplot(city_temps.values(), labels=city_temps.keys())
plt.title('Temperature Distribution by City')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.grid(axis='y', alpha=0.3)
plt.savefig('city_temps_boxplot.png')
plt.close()

# Create histogram for each city
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, (city, temps) in enumerate(city_temps.items()):
    if i < len(axes):
        axes[i].hist(temps, bins=7, alpha=0.7)
        axes[i].axvline(city_means[city], color='red', linestyle='--', label=f'Mean: {city_means[city]:.1f}°C')
        axes[i].axvline(city_medians[city], color='green', linestyle='-', label=f'Median: {city_medians[city]:.1f}°C')
        axes[i].axvline(city_modes[city], color='blue', linestyle=':', label=f'Mode: {city_modes[city]:.1f}°C')
        axes[i].set_title(f'{city} Temperatures')
        axes[i].set_xlabel('Temperature (°C)')
        axes[i].set_ylabel('Frequency')
        axes[i].legend()
        axes[i].grid(alpha=0.3)

# Remove any empty subplots
for i in range(len(city_temps), len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.savefig('city_temps_histograms.png')
plt.close()

# Identify outliers using IQR method
print("\nOutlier Detection using IQR method:")
for city, temps in city_temps.items():
    q1 = np.percentile(temps, 25)
    q3 = np.percentile(temps, 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [temp for temp in temps if temp < lower_bound or temp > upper_bound]
    
    if outliers:
        print(f"{city}: Outliers detected - {outliers}")
    else:
        print(f"{city}: No outliers detected")

# Interpretation of results
print("\nInterpretation of Results:")
print("==========================")

# Phoenix
print("\nPhoenix:")
print("- The mean (31.7°C) is higher than the median (30.1°C) due to the outlier of 42.8°C.")
print("- The median is more appropriate for Phoenix as it provides a better measure of the typical temperature.")
print("- If reporting to the public, the median would give a more accurate picture of normal temperatures.")

# Seattle
print("\nSeattle:")
print("- All three measures are very close (mean: 12.7°C, median: 12.9°C, mode: 13.0°C).")
print("- Seattle has the most consistent temperatures with no significant outliers.")
print("- Any measure would be appropriate for Seattle, but the mean is commonly used for weather data.")

# Miami
print("\nMiami:")
print("- The mean (29.5°C) is significantly higher than the median (26.9°C) due to the extreme outlier of 45.1°C.")
print("- The median or mode (26.5°C) would be more representative of Miami's typical temperature.")
print("- This is a clear case where using the mean could be misleading for the public.")

# Chicago
print("\nChicago:")
print("- The mean (15.5°C) is lower than the median (17.2°C) due to the cold outlier of 3.5°C.")
print("- The median is more appropriate for Chicago's temperature data.")
print("- This shows how outliers can pull the mean in either direction (lower in this case).")

# Denver
print("\nDenver:")
print("- Denver has outliers on both extremes (2.3°C and -3.7°C), making its data highly variable.")
print("- The median (15.9°C) provides the most reliable measure of central tendency.")
print("- Denver demonstrates why examining the full distribution is important, not just a single measure.")

print("\nOverall recommendation:")
print("For weather reporting to the public, the median would generally be the most appropriate")
print("measure for most of these cities due to the presence of outliers. When communicating")
print("to a non-technical audience, using terms like 'typical temperature' (for median) and")
print("'temperature range' may be more intuitive than statistical terminology.")