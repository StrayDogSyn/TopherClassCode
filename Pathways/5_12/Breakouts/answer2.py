# Dispersion Analysis - ANSWER KEY
# ===============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample monthly temperature data for a city (°C)
monthly_temps = {
    'January': [2.3, 1.5, 0.8, -5.2, 3.1, -7.8, 2.9, 1.7, 0.5, -2.1, 
                1.3, 2.5, 1.1, -0.9, 3.4, 2.2, 1.8, 0.3, -1.5, 4.2],
    'April': [15.2, 16.8, 14.5, 15.9, 17.2, 16.3, 15.7, 14.9, 16.1, 17.5, 
              15.3, 16.5, 14.7, 15.8, 16.9, 15.1, 16.2, 15.6, 14.3, 16.7],
    'July': [28.5, 29.1, 27.8, 30.2, 29.4, 31.5, 28.9, 29.7, 28.2, 29.9, 
             36.8, 28.7, 29.5, 27.9, 30.3, 29.2, 28.1, 29.8, 37.5, 29.6],
    'October': [18.1, 17.5, 19.2, 17.8, 16.9, 18.7, 17.3, 18.9, 16.5, 17.1, 
                18.5, 16.8, 17.6, 19.5, 18.3, 17.4, 16.2, 17.9, 18.6, 17.2]
}

# Sample precipitation data for the same months (mm)
monthly_precip = {
    'January': [35.2, 42.1, 0.0, 28.5, 15.3, 52.7, 0.0, 31.8, 45.2, 22.6, 
                39.4, 0.0, 18.7, 25.3, 48.9, 37.1, 0.0, 29.6, 33.5, 41.2],
    'April': [62.5, 58.2, 71.4, 0.0, 53.7, 47.8, 59.6, 0.0, 66.3, 49.5, 
              55.8, 61.7, 52.9, 0.0, 57.3, 63.4, 50.1, 68.9, 54.2, 0.0],
    'July': [10.2, 0.0, 5.7, 15.3, 0.0, 8.9, 12.5, 0.0, 7.6, 4.8, 
             82.5, 0.0, 6.3, 11.7, 0.0, 9.4, 7.1, 0.0, 95.8, 8.2],
    'October': [43.7, 39.5, 0.0, 46.2, 50.8, 0.0, 37.1, 44.6, 52.3, 0.0, 
                41.9, 47.5, 36.8, 0.0, 48.9, 53.4, 0.0, 40.2, 45.7, 38.3]
}

# Create DataFrames for each dataset
temp_df = pd.DataFrame(monthly_temps)
precipitation_df = pd.DataFrame(monthly_precip)

print("Temperature data (first 5 rows):")
print(temp_df.head())

print("\nPrecipitation data (first 5 rows):")
print(precipitation_df.head())

# Calculate basic dispersion measures for each month's temperature
temp_range = {}
temp_variance = {}
temp_std = {}
temp_iqr = {}

for month in monthly_temps.keys():
    temp_range[month] = max(monthly_temps[month]) - min(monthly_temps[month])
    temp_variance[month] = np.var(monthly_temps[month], ddof=1)
    temp_std[month] = np.std(monthly_temps[month], ddof=1)
    q1 = np.percentile(monthly_temps[month], 25)
    q3 = np.percentile(monthly_temps[month], 75)
    temp_iqr[month] = q3 - q1

# Create a summary table of all dispersion measures for temperature
temp_dispersion = pd.DataFrame({
    'Range': temp_range,
    'Variance': temp_variance,
    'Standard Deviation': temp_std,
    'IQR': temp_iqr
})

# Format to 2 decimal places
temp_dispersion = temp_dispersion.round(2)
print("\nTemperature Dispersion Measures:")
print(temp_dispersion)

# Calculate the coefficient of variation (CV) for temperature
# CV = (standard deviation / mean) * 100
temp_cv = {}
for month in monthly_temps.keys():
    mean = np.mean(monthly_temps[month])
    temp_cv[month] = (temp_std[month] / mean) * 100

temp_dispersion['CV (%)'] = pd.Series(temp_cv).round(2)
print("\nTemperature Dispersion with Coefficient of Variation:")
print(temp_dispersion)

# Calculate the same dispersion measures for precipitation data
precip_range = {}
precip_variance = {}
precip_std = {}
precip_iqr = {}
precip_cv = {}

for month in monthly_precip.keys():
    precip_range[month] = max(monthly_precip[month]) - min(monthly_precip[month])
    precip_variance[month] = np.var(monthly_precip[month], ddof=1)
    precip_std[month] = np.std(monthly_precip[month], ddof=1)
    q1 = np.percentile(monthly_precip[month], 25)
    q3 = np.percentile(monthly_precip[month], 75)
    precip_iqr[month] = q3 - q1
    
    # Calculate CV, handling the case of zero mean
    mean = np.mean(monthly_precip[month])
    if mean != 0:
        precip_cv[month] = (precip_std[month] / mean) * 100
    else:
        precip_cv[month] = float('inf')  # Infinite CV if mean is zero

# Create a summary table for precipitation
precip_dispersion = pd.DataFrame({
    'Range': precip_range,
    'Variance': precip_variance,
    'Standard Deviation': precip_std,
    'IQR': precip_iqr,
    'CV (%)': precip_cv
})

# Format to 2 decimal places
precip_dispersion = precip_dispersion.round(2)
print("\nPrecipitation Dispersion Measures:")
print(precip_dispersion)

# Visualize the dispersion of temperature data with box plots
plt.figure(figsize=(12, 6))
plt.boxplot([monthly_temps[month] for month in monthly_temps.keys()], 
           labels=monthly_temps.keys(), patch_artist=True,
           boxprops=dict(facecolor='lightblue'),
           medianprops=dict(color='navy'))

plt.title('Temperature Distribution by Month')
plt.ylabel('Temperature (°C)')
plt.grid(axis='y', alpha=0.3)
plt.savefig('temperature_boxplot.png')
plt.close()
print("\nTemperature boxplot saved as 'temperature_boxplot.png'")

# Visualize the dispersion of precipitation data with box plots
plt.figure(figsize=(12, 6))
plt.boxplot([monthly_precip[month] for month in monthly_precip.keys()], 
           labels=monthly_precip.keys(), patch_artist=True,
           boxprops=dict(facecolor='lightgreen'),
           medianprops=dict(color='darkgreen'))

plt.title('Precipitation Distribution by Month')
plt.ylabel('Precipitation (mm)')
plt.grid(axis='y', alpha=0.3)
plt.savefig('precipitation_boxplot.png')
plt.close()
print("\nPrecipitation boxplot saved as 'precipitation_boxplot.png'")

# Create histograms for temperature data
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, month in enumerate(monthly_temps.keys()):
    axes[i].hist(monthly_temps[month], bins=10, alpha=0.7, color='skyblue')
    axes[i].axvline(np.mean(monthly_temps[month]), color='red', linestyle='--', 
                   label=f'Mean: {np.mean(monthly_temps[month]):.2f}°C')
    axes[i].axvline(np.median(monthly_temps[month]), color='green', linestyle='-', 
                   label=f'Median: {np.median(monthly_temps[month]):.2f}°C')
    
    # Add standard deviation markers
    mean = np.mean(monthly_temps[month])
    std = np.std(monthly_temps[month], ddof=1)
    axes[i].axvline(mean + std, color='orange', linestyle=':', 
                   label=f'Mean ± SD: {std:.2f}°C')
    axes[i].axvline(mean - std, color='orange', linestyle=':')
    
    axes[i].set_title(f'{month} Temperature Distribution')
    axes[i].set_xlabel('Temperature (°C)')
    axes[i].set_ylabel('Frequency')
    axes[i].legend()
    axes[i].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('temperature_histograms.png')
plt.close()
print("\nTemperature histograms saved as 'temperature_histograms.png'")

# Create histograms for precipitation data
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, month in enumerate(monthly_precip.keys()):
    axes[i].hist(monthly_precip[month], bins=10, alpha=0.7, color='lightgreen')
    axes[i].axvline(np.mean(monthly_precip[month]), color='red', linestyle='--', 
                   label=f'Mean: {np.mean(monthly_precip[month]):.2f}mm')
    axes[i].axvline(np.median(monthly_precip[month]), color='green', linestyle='-', 
                   label=f'Median: {np.median(monthly_precip[month]):.2f}mm')
    
    # Add standard deviation markers
    mean = np.mean(monthly_precip[month])
    std = np.std(monthly_precip[month], ddof=1)
    axes[i].axvline(mean + std, color='orange', linestyle=':', 
                   label=f'Mean ± SD: {std:.2f}mm')
    axes[i].axvline(mean - std, color='orange', linestyle=':')
    
    axes[i].set_title(f'{month} Precipitation Distribution')
    axes[i].set_xlabel('Precipitation (mm)')
    axes[i].set_ylabel('Frequency')
    axes[i].legend()
    axes[i].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('precipitation_histograms.png')
plt.close()
print("\nPrecipitation histograms saved as 'precipitation_histograms.png'")

# Detect temperature outliers using the IQR method
temp_outliers_iqr = {}

for month in monthly_temps.keys():
    q1 = np.percentile(monthly_temps[month], 25)
    q3 = np.percentile(monthly_temps[month], 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [temp for temp in monthly_temps[month] 
                if temp < lower_bound or temp > upper_bound]
    
    temp_outliers_iqr[month] = outliers

print("\nTemperature Outliers (IQR Method):")
for month, outliers in temp_outliers_iqr.items():
    if outliers:
        print(f"{month}: {outliers}")
    else:
        print(f"{month}: No outliers detected")

# Detect temperature outliers using the Z-score method
temp_outliers_zscore = {}

for month in monthly_temps.keys():
    z_scores = stats.zscore(monthly_temps[month])
    outlier_indices = np.where(np.abs(z_scores) > 3)[0]
    outliers = [monthly_temps[month][i] for i in outlier_indices]
    
    temp_outliers_zscore[month] = outliers

print("\nTemperature Outliers (Z-Score Method):")
for month, outliers in temp_outliers_zscore.items():
    if outliers:
        print(f"{month}: {outliers}")
    else:
        print(f"{month}: No outliers detected")

# Compare the outliers detected by each method
print("\nComparison of Outlier Detection Methods:")
for month in monthly_temps.keys():
    iqr_set = set(temp_outliers_iqr[month])
    z_set = set(temp_outliers_zscore[month])
    
    common = iqr_set.intersection(z_set)
    only_iqr = iqr_set - z_set
    only_z = z_set - iqr_set
    
    print(f"\n{month}:")
    print(f"  Detected by both methods: {common}")
    print(f"  Detected only by IQR method: {only_iqr}")
    print(f"  Detected only by Z-score method: {only_z}")

# Detect precipitation outliers (using both methods)
precip_outliers_iqr = {}
precip_outliers_zscore = {}

for month in monthly_precip.keys():
    # IQR method
    q1 = np.percentile(monthly_precip[month], 25)
    q3 = np.percentile(monthly_precip[month], 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [precip for precip in monthly_precip[month] 
                if precip < lower_bound or precip > upper_bound]
    
    precip_outliers_iqr[month] = outliers
    
    # Z-score method
    z_scores = stats.zscore(monthly_precip[month])
    outlier_indices = np.where(np.abs(z_scores) > 3)[0]
    outliers = [monthly_precip[month][i] for i in outlier_indices]
    
    precip_outliers_zscore[month] = outliers

print("\nPrecipitation Outliers (IQR Method):")
for month, outliers in precip_outliers_iqr.items():
    if outliers:
        print(f"{month}: {outliers}")
    else:
        print(f"{month}: No outliers detected")

print("\nPrecipitation Outliers (Z-Score Method):")
for month, outliers in precip_outliers_zscore.items():
    if outliers:
        print(f"{month}: {outliers}")
    else:
        print(f"{month}: No outliers detected")

# Comprehensive Interpretation
print("\n--- COMPREHENSIVE ANALYSIS ---")
print("Based on our analysis of the dispersion measures:")

# 1. Temperature variability
max_temp_var_month = temp_dispersion['Standard Deviation'].idxmax()
max_temp_cv_month = temp_dispersion['CV (%)'].idxmax()

print(f"\n1. Temperature Variability:")
print(f"   - {max_temp_var_month} has the highest standard deviation ({temp_dispersion.loc['Standard Deviation', max_temp_var_month]}°C)")
print(f"   - {max_temp_cv_month} has the highest coefficient of variation ({temp_dispersion.loc['CV (%)', max_temp_cv_month]}%)")
print(f"   - This indicates that {max_temp_var_month} has the largest absolute temperature variability,")
print(f"     while {max_temp_cv_month} has the highest variability relative to its mean temperature.")

# 2. Precipitation variability
max_precip_var_month = precip_dispersion['Standard Deviation'].idxmax()
max_precip_cv_month = precip_dispersion['CV (%)'].idxmax()

print(f"\n2. Precipitation Variability:")
print(f"   - {max_precip_var_month} has the highest standard deviation ({precip_dispersion.loc['Standard Deviation', max_precip_var_month]}mm)")
print(f"   - {max_precip_cv_month} has the highest coefficient of variation ({precip_dispersion.loc['CV (%)', max_precip_cv_month]}%)")
print(f"   - This indicates that {max_precip_var_month} has the largest absolute precipitation variability,")
print(f"     while {max_precip_cv_month} has the highest variability relative to its mean precipitation.")

# 3. Outlier Detection Methods
print("\n3. Outlier Detection Methods Comparison:")
print(f"   - The IQR method detected more temperature outliers in {', '.join([m for m in monthly_temps.keys() if len(temp_outliers_iqr[m]) > len(temp_outliers_zscore[m])])}")
print(f"   - The Z-score method detected more temperature outliers in {', '.join([m for m in monthly_temps.keys() if len(temp_outliers_zscore[m]) > len(temp_outliers_iqr[m])])}")
print(f"   - For precipitation, the IQR method is generally more robust as it doesn't assume a normal distribution,")
print(f"     which is important since precipitation data is often right-skewed with many zero or low values.")

# 4. Seasonal Patterns
print("\n4. Seasonal Weather Patterns:")
print(f"   - Winter (January) shows high temperature variability relative to its mean ({temp_dispersion.loc['CV (%)', 'January']}%), ")
print(f"     suggesting more inconsistent temperatures.")
print(f"   - Summer (July) shows the most extreme precipitation outliers, indicating occasional heavy storms")
print(f"     despite generally lower precipitation.")
print(f"   - Spring and fall (April and October) tend to have more consistent temperature patterns but")
print(f"     variable precipitation.")

# 5. Practical Implications
print("\n5. Practical Implications:")
print(f"   - For weather forecasting, {max_temp_var_month} temperatures would be the most difficult to predict accurately")
print(f"     due to their high variability.")
print(f"   - Flood risk is likely highest in {max_precip_var_month} despite not having the highest average precipitation,")
print(f"     due to the potential for extreme events (outliers).")
print(f"   - For public communication, ranges and IQR might be more intuitive than standard deviation")
print(f"     to explain the typical spread of daily temperatures.")