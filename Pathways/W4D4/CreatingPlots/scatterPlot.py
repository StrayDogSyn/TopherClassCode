import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
temperature = np.random.normal(25, 5, 100)  # Mean 25°C, std 5°C
humidity = temperature * 0.9 + np.random.normal(50, 10, 100)  # Correlated with temp

# Create a scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(temperature, humidity, c=temperature, 
                     cmap='coolwarm', alpha=0.7, s=50)

# Add labels and title
ax.set_title('Temperature vs Humidity', fontsize=14)
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('Humidity (%)', fontsize=12)

# Add a color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Temperature (°C)', fontsize=12)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

plt.savefig('my_plot.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'my_plot.png'")
print("Open the file to see your plot!")
