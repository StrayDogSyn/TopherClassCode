# Example 2: Enhanced Box Plots with Seaborn
# This example shows how to create more visually appealing box plots using Seaborn

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Create a DataFrame with our data
# DataFrames make it easier to work with labeled data
df = pd.DataFrame({
    'Low Variance': np.random.normal(0, 1, 100),
    'Medium Variance': np.random.normal(0, 2, 100),
    'High Variance': np.random.normal(0, 3, 100)
})

# Show the first few rows of our DataFrame
print("First 5 rows of our DataFrame:")
print(df.head())

# We need to reshape our DataFrame for Seaborn
# This converts from "wide format" to "long format"
melted_df = pd.melt(df, var_name='Distribution', value_name='Value')

# Show the first few rows of our reshaped DataFrame
print("\nFirst 5 rows of our reshaped DataFrame:")
print(melted_df.head())

# Create a figure
plt.figure(figsize=(10, 6))

# Create a box plot with Seaborn
# x: category for the x-axis
# y: values for the y-axis
# data: our DataFrame
sns.boxplot(x='Distribution', y='Value', data=melted_df)

# Add a title
plt.title('Box Plot Comparison of Distributions with Different Variances')

# Adjust the bottom margin to make room for labels
plt.tight_layout()

# Display the plot
plt.savefig('plot.png')

# Seaborn advantages:
# - Better default styling
# - Works well with pandas DataFrames
# - Easier to customize
# - Built-in support for showing data points