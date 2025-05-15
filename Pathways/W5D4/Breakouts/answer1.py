# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('seasons.csv')

# Solution 1: Basic box plot with Matplotlib
plt.figure(figsize=(12, 6))
data.boxplot(column='temperature', by='season', figsize=(12, 6))
plt.title('Seasonal Temperature Distributions')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.suptitle('')  # Remove the automatic title
plt.tight_layout()
plt.show()

# Solution 2: Enhanced box plot with Seaborn
plt.figure(figsize=(12, 6))
sns.boxplot(x='season', y='temperature', data=temperatures, 
            palette="coolwarm")  # Use a color palette to show temperature differences
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.title('Seasonal Temperature Distributions')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()