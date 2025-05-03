import matplotlib.pyplot as plt
import numpy as np

# Use your actual cleaned_data
cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm
}

# Extract data for plotting
temperature = cleaned_data['temperature']
humidity = cleaned_data['humidity']

# Create a scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(temperature, humidity, c=temperature, 
                     cmap='coolwarm', alpha=0.7, s=50)

# Add labels and title
ax.set_title('Temperature vs Humidity', fontsize=14)
ax.set_xlabel('Temperature (°F)', fontsize=12)  # Changed to °F
ax.set_ylabel('Humidity (%)', fontsize=12)

# Add a color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Temperature (°F)', fontsize=12)  # Changed to °F

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

plt.savefig('scatter.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'scatter.png'")
print("Open the file to see your plot!")


import matplotlib.pyplot as plt
import numpy as np

# Use your actual cleaned_data
cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm
}

# Extract data for plotting
dates = cleaned_data['date']
precipitation = cleaned_data['precipitation']

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(dates, precipitation, color='skyblue', edgecolor='navy')

# Customize the plot
ax.set_title('Daily Precipitation', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Precipitation (mm)', fontsize=12)
ax.set_ylim(0, max(precipitation) + 5)  # Adjust y-axis to fit data

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{height}', ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.savefig('bar.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'bar.png'")
print("Open the file to see your plot!")


import matplotlib.pyplot as plt
import numpy as np

# Use your actual cleaned_data
cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm
}

# Create a more customized plot with your data
fig, ax = plt.subplots(figsize=(12, 7))

# Plot temperature and humidity with custom styling
x = range(len(cleaned_data['date']))
ax.plot(x, cleaned_data['temperature'], linestyle='-', color='red', linewidth=2, 
        marker='o', markersize=8, label='Temperature (°F)')

# Create secondary y-axis for humidity
ax2 = ax.twinx()
ax2.plot(x, cleaned_data['humidity'], linestyle='--', color='blue', linewidth=2, 
         marker='s', markersize=8, label='Humidity (%)')

# Customize title and labels
ax.set_title('Temperature and Humidity Over Time', fontsize=16, fontweight='bold')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Temperature (°F)', fontsize=12, color='red')
ax2.set_ylabel('Humidity (%)', fontsize=12, color='blue')

# Set x-tick labels
ax.set_xticks(x)
ax.set_xticklabels(cleaned_data['date'], rotation=45)

# Customize grid
ax.grid(True, linestyle=':', alpha=0.7)

# Add legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Add annotation for the temperature outlier
max_temp_idx = cleaned_data['temperature'].index(max(cleaned_data['temperature']))
ax.annotate('Temperature Spike', 
            xy=(max_temp_idx, cleaned_data['temperature'][max_temp_idx]), 
            xytext=(max_temp_idx, cleaned_data['temperature'][max_temp_idx] + 10),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

plt.tight_layout()
plt.savefig('line.png')
plt.close()

print("Plot saved as 'line.png'")
print("Open the file to see your plot!")