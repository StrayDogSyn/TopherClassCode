# Example 1: Basic Histograms with Matplotlib
# This example shows how to create a simple histogram to visualize data distribution

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data - simulate height data with a normal distribution
# Mean height of 170 cm with standard deviation of 10 cm
heights = np.random.normal(170, 10, 250)  # 250 data points

# Print some basic statistics about our data
print(f"Number of data points: {len(heights)}")
print(f"Minimum height: {heights.min():.1f} cm")
print(f"Maximum height: {heights.max():.1f} cm")
print(f"Mean height: {heights.mean():.1f} cm")
print(f"Standard deviation: {heights.std():.1f} cm")

# Create a figure
plt.figure(figsize=(10, 6))

# Create a histogram
# bins: number of bins to divide the data into
# edgecolor: color of the edges of the bars
# alpha: transparency of the bars
plt.hist(heights, bins=15, edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Height Distribution')

# Add a grid for easier reading
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.savefig('plot.png')

# Key concepts:
# - Histograms group continuous data into bins
# - The height of each bar shows the frequency (count) of values in that bin
# - The overall shape shows the distribution pattern
# - Normal distributions have a characteristic "bell curve" shape
# - Histograms help visualize central tendency, spread, and shape