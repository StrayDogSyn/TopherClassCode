import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample temperature data (°C) for a week
temperatures = [22.5, 23.1, 24.0, 35.7, 21.8, 22.3, 23.5]

print("Temperature data (°C):", temperatures)

# Calculate standard deviation
# ddof=0 for population standard deviation, ddof=1 for sample standard deviation
population_std = np.std(temperatures, ddof=0)
sample_std = np.std(temperatures, ddof=1)

print(f"\n--- Standard Deviation ---")
print(f"Population standard deviation: {population_std:.2f}°C")
print(f"Sample standard deviation: {sample_std:.2f}°C")

# Calculate standard deviation manually (from variance)
population_variance = np.var(temperatures, ddof=0)
sample_variance = np.var(temperatures, ddof=1)

manual_pop_std = np.sqrt(population_variance)
manual_sample_std = np.sqrt(sample_variance)

print(f"\n--- Manual Calculation ---")
print(f"Standard deviation from variance: {manual_sample_std:.2f}°C")
print(f"NumPy std matches manual calculation: {np.isclose(manual_sample_std, sample_std)}")

# Let's see what happens to the standard deviation when we remove the outlier
temps_without_outlier = [22.5, 23.1, 24.0, 21.8, 22.3, 23.5]  # Removed 35.7°C
std_without_outlier = np.std(temps_without_outlier, ddof=1)

print("\n--- Effect of Outliers on Standard Deviation ---")
print(f"Standard deviation with outlier: {sample_std:.2f}°C")
print(f"Standard deviation without outlier: {std_without_outlier:.2f}°C")
print(f"Difference: {sample_std - std_without_outlier:.2f}°C")
print("Standard deviation is sensitive to outliers, like variance!")

# Interpreting standard deviation with normal distribution
# Generate a normal distribution with the same mean and std as our temperature data
mean_temp = np.mean(temperatures)
np.random.seed(42)  # For reproducibility
normal_temps = np.random.normal(mean_temp, sample_std, 1000)

print("\n--- Interpreting Standard Deviation with Normal Distribution ---")
print(f"For normally distributed data:")
print(f"  ~68% of values fall within 1 standard deviation of the mean")
print(f"  ~95% of values fall within 2 standard deviations")
print(f"  ~99.7% of values fall within 3 standard deviations")

print(f"\nFor our temperature data:")
print(f"  Mean: {mean_temp:.2f}°C")
print(f"  Mean ± 1 SD: {mean_temp - sample_std:.2f}°C to {mean_temp + sample_std:.2f}°C")
print(f"  Mean ± 2 SD: {mean_temp - 2*sample_std:.2f}°C to {mean_temp + 2*sample_std:.2f}°C")
print(f"  Mean ± 3 SD: {mean_temp - 3*sample_std:.2f}°C to {mean_temp + 3*sample_std:.2f}°C")

# Count how many original temperatures fall within these ranges
within_1sd = sum((mean_temp - sample_std <= x <= mean_temp + sample_std) for x in temperatures)
within_2sd = sum((mean_temp - 2*sample_std <= x <= mean_temp + 2*sample_std) for x in temperatures)
within_3sd = sum((mean_temp - 3*sample_std <= x <= mean_temp + 3*sample_std) for x in temperatures)

print(f"\nOf our {len(temperatures)} data points:")
print(f"  {within_1sd} ({within_1sd/len(temperatures)*100:.1f}%) are within 1 SD of the mean")
print(f"  {within_2sd} ({within_2sd/len(temperatures)*100:.1f}%) are within 2 SD of the mean")
print(f"  {within_3sd} ({within_3sd/len(temperatures)*100:.1f}%) are within 3 SD of the mean")

# Visualize the standard deviation with histogram and normal curve
plt.figure(figsize=(12, 6))

# Plot histogram of the simulated normal distribution
plt.hist(normal_temps, bins=30, density=True, alpha=0.5, color='skyblue', 
         label='Normal Distribution\nwith same Mean & SD')

# Plot normal curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean_temp, sample_std)
plt.plot(x, p, 'k', linewidth=2, label='Normal Curve')

# Plot the mean and standard deviation lines
plt.axvline(x=mean_temp, color='red', linestyle='--', label=f'Mean: {mean_temp:.2f}°C')
plt.axvline(x=mean_temp + sample_std, color='green', linestyle=':', 
            label=f'Mean + 1 SD: {mean_temp + sample_std:.2f}°C')
plt.axvline(x=mean_temp - sample_std, color='green', linestyle=':',
            label=f'Mean - 1 SD: {mean_temp - sample_std:.2f}°C')

# Plot the original data points
for temp in temperatures:
    plt.axvline(x=temp, color='blue', alpha=0.7, linewidth=1)

plt.title('Standard Deviation and Normal Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)

# Save the figure (for GitHub Codespaces)
plt.savefig('std_dev_visualization.png')
plt.close()
print("Standard deviation visualization saved as 'std_dev_visualization.png'")