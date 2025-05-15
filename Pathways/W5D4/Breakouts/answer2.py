# Histogram Exercise Solution

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('seasons.csv')

# 1. Create a histogram of overall temperature distribution
plt.figure(figsize=(10, 6))
plt.hist(data['temperature'], bins=15, color='skyblue', edgecolor='black')
plt.title('Overall Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig('overall_temperature_histogram.png')
plt.close()

# 2. Create histograms with different bin sizes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Few bins (5)
axs[0].hist(data['temperature'], bins=5, color='skyblue', edgecolor='black')
axs[0].set_title('Temperature Distribution (5 bins)')
axs[0].set_xlabel('Temperature (°C)')
axs[0].set_ylabel('Frequency')
axs[0].grid(axis='y', alpha=0.75)

# Medium bins (15)
axs[1].hist(data['temperature'], bins=15, color='skyblue', edgecolor='black')
axs[1].set_title('Temperature Distribution (15 bins)')
axs[1].set_xlabel('Temperature (°C)')
axs[1].set_ylabel('Frequency')
axs[1].grid(axis='y', alpha=0.75)

# Many bins (30)
axs[2].hist(data['temperature'], bins=30, color='skyblue', edgecolor='black')
axs[2].set_title('Temperature Distribution (30 bins)')
axs[2].set_xlabel('Temperature (°C)')
axs[2].set_ylabel('Frequency')
axs[2].grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.savefig('bin_size_comparison.png')
plt.close()

# 3. Create histograms comparing seasonal distributions
# Individual season histograms
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

seasons = ['Winter', 'Spring', 'Summer', 'Fall']
colors = ['blue', 'green', 'red', 'orange']

for i, (season, color) in enumerate(zip(seasons, colors)):
    row, col = i // 2, i % 2
    season_data = data[data['season'] == season]['temperature']
    
    axs[row, col].hist(season_data, bins=10, color=color, edgecolor='black', alpha=0.7)
    axs[row, col].set_title(f'{season} Temperature Distribution')
    axs[row, col].set_xlabel('Temperature (°C)')
    axs[row, col].set_ylabel('Frequency')
    axs[row, col].grid(axis='y', alpha=0.75)
    
    # Add mean line
    mean_temp = season_data.mean()
    axs[row, col].axvline(mean_temp, color='black', linestyle='dashed', linewidth=1)
    axs[row, col].text(mean_temp + 0.5, axs[row, col].get_ylim()[1]*0.9, 
                      f'Mean: {mean_temp:.1f}°C', rotation=0)

plt.tight_layout()
plt.savefig('seasonal_histograms.png')
plt.close()

# Overlaid seasonal distributions using KDE plots for better comparison
plt.figure(figsize=(12, 6))
for season, color in zip(seasons, colors):
    season_data = data[data['season'] == season]['temperature']
    sns.kdeplot(season_data, label=season, color=color, fill=True, alpha=0.3)

plt.title('Seasonal Temperature Distributions')
plt.xlabel('Temperature (°C)')
plt.ylabel('Density')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('seasonal_kde_comparison.png')
plt.close()

# Calculate and print statistical summaries for each season
print("Statistical Summary of Seasonal Temperatures:")
print(data.groupby('season')['temperature'].agg(['min', 'max', 'mean', 'std']).round(2))

# Calculate the temperature range that occurs most frequently
# Using the bin with highest frequency from the overall histogram
hist, bin_edges = np.histogram(data['temperature'], bins=15)
max_freq_bin_index = np.argmax(hist)
most_common_range = (bin_edges[max_freq_bin_index], bin_edges[max_freq_bin_index + 1])
print(f"\nMost frequently occurring temperature range: {most_common_range[0]:.1f}°C to {most_common_range[1]:.1f}°C")