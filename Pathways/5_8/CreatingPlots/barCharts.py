import matplotlib.pyplot as plt
import numpy as np

# Sample weather data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [30, 25, 50, 40, 60, 70, 90, 85, 70, 60, 50, 35]

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(months, rainfall, color='skyblue', edgecolor='navy')

# Customize the plot
ax.set_title('Monthly Rainfall', fontsize=14)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Rainfall (mm)', fontsize=12)
ax.set_ylim(0, 100)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height}', ha='center', va='bottom')

plt.savefig('my_plot.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'my_plot.png'")
print("Open the file to see your plot!")
