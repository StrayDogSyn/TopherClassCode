import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate temperature data with min, mean, max
dates = pd.date_range('2023-01-01', periods=30)
temp_min = np.random.normal(5, 3, 30)
temp_mean = temp_min + np.random.uniform(3, 5, 30)
temp_max = temp_mean + np.random.uniform(3, 5, 30)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot mean temperature
ax.plot(dates, temp_mean, 'r-', linewidth=2, label='Mean Temperature')

# Fill between min and max
ax.fill_between(dates, temp_min, temp_max, alpha=0.2, color='red',
                label='Temperature Range')

# Customize plot
ax.set_title('Temperature Range over Time', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Format x-axis with dates
fig.autofmt_xdate()  # Auto-format x labels for dates

plt.savefig('fillBetween.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plot saved as 'fillBetween.png'")