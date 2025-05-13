import numpy as np
import pandas as pd

# Sample temperature data (°C) for a week
temperatures = [22.5, 23.1, 24.0, 35.7, 21.8, 22.3, 23.5]

# Calculate mean
mean_temp = np.mean(temperatures)
print(f"Daily temperatures (°C): {temperatures}")
print(f"Mean temperature: {mean_temp:.2f}°C")

# Let's see what happens with and without the outlier
temps_without_outlier = [22.5, 23.1, 24.0, 21.8, 22.3, 23.5]  # Removed 35.7°C
mean_without_outlier = np.mean(temps_without_outlier)

print("\n--- Effect of Outliers on Mean ---")
print(f"Mean with outlier: {mean_temp:.2f}°C")
print(f"Mean without outlier: {mean_without_outlier:.2f}°C")
print(f"Difference: {mean_temp - mean_without_outlier:.2f}°C")

# Using pandas for a more realistic example
# Creating a DataFrame with dates
dates = pd.date_range('2025-05-01', periods=7)
temp_df = pd.DataFrame({
    'date': dates,
    'temperature': temperatures
})

print("\n--- Temperature Data with Dates ---")
print(temp_df)

# Calculate mean using pandas
pandas_mean = temp_df['temperature'].mean()
print(f"\nMean temperature using pandas: {pandas_mean:.2f}°C")

# Let's create a function to calculate mean manually
def calculate_mean(values):
    """Calculate the mean of a list of values manually"""
    total = sum(values)
    count = len(values)
    return total / count

manual_mean = calculate_mean(temperatures)
print(f"\nManually calculated mean: {manual_mean:.2f}°C")
print(f"NumPy mean matches manual calculation: {np.isclose(manual_mean, mean_temp)}")