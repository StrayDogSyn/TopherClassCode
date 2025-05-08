# Example 1: Basic Box Plot with Matplotlib
# This example shows how to create a simple box plot to compare distributions

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate three datasets with different variances
# We'll create data with low, medium, and high variance
low_variance = np.random.normal(0, 1, 100)    # Standard deviation = 1
medium_variance = np.random.normal(0, 2, 100)  # Standard deviation = 2
high_variance = np.random.normal(0, 3, 100)    # Standard deviation = 3

# Create a list of our datasets
data = [low_variance, medium_variance, high_variance]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a box plot on the axis
# The boxplot function takes a list of datasets
box_plot = ax.boxplot(data)

# Add labels to make the plot more readable
ax.set_xticklabels(['Low Variance', 'Medium Variance', 'High Variance'])
ax.set_ylabel('Value')
ax.set_title('Box Plot Comparison of Distributions with Different Variances')

# Add a grid to make it easier to read values
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.savefig('plot.png')

# Box plot components:
# - Box: Shows the Interquartile Range (IQR) - middle 50% of data
# - Line in box: Median (50th percentile)
# - Bottom of box: First quartile (25th percentile)
# - Top of box: Third quartile (75th percentile)
# - Whiskers: Extend to the most extreme data points within 1.5 * IQR
# - Points beyond whiskers: Potential outliers