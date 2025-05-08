import matplotlib.pyplot as plt
import numpy as np

# Use your cleaned_data
cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm
}

# Generate x data for sine wave
x = np.linspace(0, 10, 100)

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line plot (top left) - keeping the sine wave
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True)

# Plot 2: Scatter plot (top right) - using cleaned_data
axes[0, 1].scatter(cleaned_data['temperature'], cleaned_data['humidity'], 
                   alpha=0.7, c='green', s=100)
axes[0, 1].set_title('Temperature vs Humidity')
axes[0, 1].set_xlabel('Temperature (°F)')
axes[0, 1].set_ylabel('Humidity (%)')

# Plot 3: Bar chart (bottom left) - using cleaned_data precipitation
axes[1, 0].bar(range(len(cleaned_data['date'])), cleaned_data['precipitation'], 
               color='skyblue')
axes[1, 0].set_title('Daily Precipitation')
axes[1, 0].set_xticks(range(len(cleaned_data['date'])))
axes[1, 0].set_xticklabels(cleaned_data['date'], rotation=45)
axes[1, 0].set_ylabel('Precipitation (mm)')

# Plot 4: Histogram (bottom right) - using cleaned_data temperature
axes[1, 1].hist(cleaned_data['temperature'], bins=5, color='orange', 
                edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Temperature Distribution')
axes[1, 1].set_xlabel('Temperature (°F)')
axes[1, 1].set_ylabel('Frequency')

# Adjust layout
fig.tight_layout()

# Save the plot
plt.savefig('subplots.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plot saved as 'subplots.png'")