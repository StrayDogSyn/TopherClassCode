import matplotlib.pyplot as plt
import numpy as np

# Define the data first
x = np.linspace(0, 10, 100)
temperature = np.random.normal(25, 5, 100)  # Random temperature data
humidity = temperature * 0.9 + np.random.normal(50, 10, 100)  # Correlated with temp
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [30, 25, 50, 40, 60, 70, 90, 85, 70, 60, 50, 35]

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line plot (top left)
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True)

# Plot 2: Scatter plot (top right)
axes[0, 1].scatter(temperature, humidity, alpha=0.7, c='green')
axes[0, 1].set_title('Temperature vs Humidity')

# Plot 3: Bar chart (bottom left)
axes[1, 0].bar(months[:6], rainfall[:6], color='skyblue')
axes[1, 0].set_title('Rainfall (First Half Year)')
# Fix the tick labels warning by setting ticks first
axes[1, 0].set_xticks(range(6))
axes[1, 0].set_xticklabels(months[:6], rotation=45)

# Plot 4: Histogram (bottom right)
axes[1, 1].hist(temperature, bins=15, color='orange', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Temperature Distribution')

# Adjust layout
fig.tight_layout()

# Save the plot instead of showing it
plt.savefig('subplots.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plot saved as 'subplots.png'")