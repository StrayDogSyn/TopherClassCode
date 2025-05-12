import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample temperature data (°C) for a week
temperatures = [22.5, 23.1, 24.0, 35.7, 21.8, 22.3, 23.5]

print("Temperature data (°C):", temperatures)

# Calculate variance
# ddof=0 for population variance, ddof=1 for sample variance
population_variance = np.var(temperatures, ddof=0)
sample_variance = np.var(temperatures, ddof=1)

print(f"\n--- Variance ---")
print(f"Population variance: {population_variance:.2f}°C²")
print(f"Sample variance: {sample_variance:.2f}°C²")

# Note: Variance is expressed in squared units, which makes 
# it difficult to interpret directly

# Calculate variance manually to understand the formula
def calculate_variance(values, sample=True):
    """Calculate variance manually
    
    Args:
        values: List of values
        sample: If True, use n-1 denominator (sample variance)
               If False, use n denominator (population variance)
    
    Returns:
        Calculated variance
    """
    # Calculate mean
    mean = sum(values) / len(values)
    
    # Calculate sum of squared differences from the mean
    squared_diff_sum = sum((x - mean) ** 2 for x in values)
    
    # Divide by n-1 for sample variance or n for population variance
    denominator = len(values) - 1 if sample else len(values)
    
    return squared_diff_sum / denominator

manual_sample_variance = calculate_variance(temperatures, sample=True)
manual_pop_variance = calculate_variance(temperatures, sample=False)

print(f"\n--- Manual Calculation ---")
print(f"Manually calculated sample variance: {manual_sample_variance:.2f}°C²")
print(f"Manually calculated population variance: {manual_pop_variance:.2f}°C²")
print(f"NumPy sample variance matches manual: {np.isclose(manual_sample_variance, sample_variance)}")
print(f"NumPy population variance matches manual: {np.isclose(manual_pop_variance, population_variance)}")

# Let's see what happens to the variance when we remove the outlier
temps_without_outlier = [22.5, 23.1, 24.0, 21.8, 22.3, 23.5]  # Removed 35.7°C
variance_without_outlier = np.var(temps_without_outlier, ddof=1)

print("\n--- Effect of Outliers on Variance ---")
print(f"Sample variance with outlier: {sample_variance:.2f}°C²")
print(f"Sample variance without outlier: {variance_without_outlier:.2f}°C²")
print(f"Difference: {sample_variance - variance_without_outlier:.2f}°C²")
print("Variance is very sensitive to outliers because it squares the differences!")

# Visualizing the variance concept
plt.figure(figsize=(10, 6))

# Calculate mean
mean_temp = np.mean(temperatures)

# Sort temperatures for clarity in the visualization
sorted_indices = np.argsort(temperatures)
sorted_temps = np.array(temperatures)[sorted_indices]

# Plot the temperatures
plt.scatter(range(len(sorted_temps)), sorted_temps, s=100, color='blue', 
            label='Temperature values')
plt.axhline(y=mean_temp, color='red', linestyle='-', 
            label=f'Mean: {mean_temp:.2f}°C')

# Plot the squared differences from mean
for i, temp in enumerate(sorted_temps):
    # Draw a line from the point to the mean
    plt.plot([i, i], [temp, mean_temp], 'k--', alpha=0.5)
    
    # Calculate squared difference
    sq_diff = (temp - mean_temp) ** 2
    
    # Annotate with the squared difference
    plt.annotate(f'{sq_diff:.1f}°C²', 
                xy=(i, (temp + mean_temp) / 2), 
                xytext=(10, 0), 
                textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3))

plt.title('Visualizing Variance: Squared Differences from Mean')
plt.xlabel('Data Point')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(range(len(temperatures)), sorted_indices + 1)  # Add 1 for 1-based indexing

# Save the figure (for GitHub Codespaces)
plt.savefig('variance_visualization.png')
plt.close()
print("Variance visualization saved as 'variance_visualization.png'")