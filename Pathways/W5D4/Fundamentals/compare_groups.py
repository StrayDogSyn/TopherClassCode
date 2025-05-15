# Example 3: Comparing Multiple Groups with Box Plots
# This example shows how to compare distributions across multiple categories and groups

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

data = pd.read_csv('groups.csv')

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