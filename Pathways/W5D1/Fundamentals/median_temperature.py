import numpy as np
import pandas as pd
from scipy import stats

# Sample temperature data (°C) for a week
temperatures = [22.5, 23.1, 24.0, 35.7, 21.8, 22.3, 23.5]

# Calculate median
median_temp = np.median(temperatures)
print(f"Daily temperatures (°C): {temperatures}")
print(f"Median temperature: {median_temp:.2f}°C")

# Let's see what happens with and without the outlier
temps_without_outlier = [22.5, 23.1, 24.0, 21.8, 22.3, 23.5]  # Removed 35.7°C
median_without_outlier = np.median(temps_without_outlier)

print("\n--- Effect of Outliers on Median ---")
print(f"Median with outlier: {median_temp:.2f}°C")
print(f"Median without outlier: {median_without_outlier:.2f}°C")
print(f"Difference: {median_temp - median_without_outlier:.2f}°C")

# Using pandas for a more realistic example
# Creating a DataFrame with dates
dates = pd.date_range('2025-05-01', periods=7)
temp_df = pd.DataFrame({
    'date': dates,
    'temperature': temperatures
})

print("\n--- Temperature Data with Dates ---")
print(temp_df)

# Sort the data to demonstrate finding the median manually
sorted_temps = sorted(temperatures)
print(f"\nSorted temperatures: {sorted_temps}")

# Calculate median manually
def calculate_median(values):
    """Calculate the median of a list of values manually"""
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    # If the length is odd, return the middle value
    if n % 2 == 1:
        return sorted_values[n // 2]
    
    # If the length is even, return the average of the two middle values
    else:
        mid1 = sorted_values[(n // 2) - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) / 2

manual_median = calculate_median(temperatures)
print(f"\nManually calculated median: {manual_median:.2f}°C")
print(f"NumPy median matches manual calculation: {np.isclose(manual_median, median_temp)}")

# Example with even number of values
even_temps = [22.5, 23.1, 24.0, 21.8, 22.3, 23.5]  # 6 values
even_median = np.median(even_temps)
manual_even_median = calculate_median(even_temps)

print(f"\nMedian of even-length list: {even_median:.2f}°C")
print(f"Manually calculated: {manual_even_median:.2f}°C")