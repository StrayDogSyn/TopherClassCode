"""
Basic Numerical Transformations
------------------------------
This script demonstrates various numerical transformations commonly used
in feature engineering to handle different data distributions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import scipy.stats as stats

# Set random seed for reproducibility
np.random.seed(42)

# Create a synthetic dataset with different distributions
n_samples = 1000

# Right-skewed data (common in prices, incomes, etc.)
right_skewed = np.random.exponential(scale=2.0, size=n_samples)

# Left-skewed data
left_skewed = 10 - np.random.exponential(scale=2.0, size=n_samples)
left_skewed = left_skewed[left_skewed > 0]  # Ensure positive values
left_skewed = np.append(left_skewed, np.zeros(n_samples - len(left_skewed)))  # Maintain size

# Normal distribution
normal = np.random.normal(loc=5.0, scale=1.0, size=n_samples)

# Bimodal distribution
bimodal = np.concatenate([
    np.random.normal(loc=2.0, scale=0.5, size=n_samples//2),
    np.random.normal(loc=8.0, scale=0.5, size=n_samples//2)
])

# Uniform distribution
uniform = np.random.uniform(low=0, high=10, size=n_samples)

# Creating a dataframe
df = pd.DataFrame({
    'right_skewed': right_skewed,
    'left_skewed': left_skewed,
    'normal': normal,
    'bimodal': bimodal,
    'uniform': uniform
})

print("Original Data Summary:")
print(df.describe())

# Function to plot distribution before and after transformation
def plot_transformation(original, transformed, title, filename):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Original distribution
    ax1.hist(original, bins=30, alpha=0.7, color='blue')
    ax1.set_title(f'Original {title} Distribution')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Frequency')
    
    # Calculate skewness
    skewness = stats.skew(original)
    ax1.text(0.05, 0.95, f'Skewness: {skewness:.3f}', transform=ax1.transAxes,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Transformed distribution
    ax2.hist(transformed, bins=30, alpha=0.7, color='green')
    ax2.set_title(f'Transformed {title} Distribution')
    ax2.set_xlabel('Value')
    ax2.set_ylabel('Frequency')
    
    # Calculate skewness for transformed data
    skewness_transformed = stats.skew(transformed)
    ax2.text(0.05, 0.95, f'Skewness: {skewness_transformed:.3f}', transform=ax2.transAxes,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 1. Log Transformation (for right-skewed data)
# Adding a small value to avoid log(0)
df['log_right_skewed'] = np.log1p(df['right_skewed'])
plot_transformation(df['right_skewed'], df['log_right_skewed'], 
                    'Right-Skewed (Log Transform)', 'log_transform.png')

# 2. Square Root Transformation (for right-skewed data, less aggressive than log)
df['sqrt_right_skewed'] = np.sqrt(df['right_skewed'])
plot_transformation(df['right_skewed'], df['sqrt_right_skewed'], 
                    'Right-Skewed (Square Root Transform)', 'sqrt_transform.png')

# 3. Square Transformation (for left-skewed data)
df['square_left_skewed'] = df['left_skewed'] ** 2
plot_transformation(df['left_skewed'], df['square_left_skewed'], 
                    'Left-Skewed (Square Transform)', 'square_transform.png')

# 4. Box-Cox Transformation (requires positive values)
positive_values = df['right_skewed'] + 1e-10  # Ensure all values are positive
df['boxcox_right_skewed'], lambda_param = stats.boxcox(positive_values)
plot_transformation(df['right_skewed'], df['boxcox_right_skewed'], 
                    f'Right-Skewed (Box-Cox λ={lambda_param:.3f})', 'boxcox_transform.png')

# 5. Binning Continuous Variables
# Equal-width binning
df['binned_uniform_equal_width'] = pd.cut(df['uniform'], bins=5, labels=[1, 2, 3, 4, 5])

# Equal-frequency binning (quantiles)
df['binned_uniform_quantiles'] = pd.qcut(df['uniform'], q=5, labels=[1, 2, 3, 4, 5])

# Custom binning
custom_bins = [0, 2, 5, 7, 10]
custom_labels = ['Low', 'Medium', 'High', 'Very High']
df['binned_uniform_custom'] = pd.cut(df['uniform'], bins=custom_bins, labels=custom_labels)

# Visualize the binning results
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Equal-width binning
value_counts_equal = df['binned_uniform_equal_width'].value_counts().sort_index()
axes[0].bar(value_counts_equal.index.astype(str), value_counts_equal.values, color='skyblue')
axes[0].set_title('Equal-Width Binning')
axes[0].set_xlabel('Bin')
axes[0].set_ylabel('Count')

# Equal-frequency binning
value_counts_quantile = df['binned_uniform_quantiles'].value_counts().sort_index()
axes[1].bar(value_counts_quantile.index.astype(str), value_counts_quantile.values, color='lightgreen')
axes[1].set_title('Equal-Frequency Binning (Quantiles)')
axes[1].set_xlabel('Bin')
axes[1].set_ylabel('Count')

# Custom binning
value_counts_custom = df['binned_uniform_custom'].value_counts().sort_index()
axes[2].bar(value_counts_custom.index, value_counts_custom.values, color='salmon')
axes[2].set_title('Custom Binning')
axes[2].set_xlabel('Bin')
axes[2].set_ylabel('Count')

plt.tight_layout()
plt.savefig('binning_comparison.png')
plt.close()

# 6. Handling Outliers
# Generate data with outliers
data_with_outliers = np.random.normal(loc=50, scale=10, size=n_samples)
# Add outliers
outlier_indices = np.random.choice(range(n_samples), size=20, replace=False)
data_with_outliers[outlier_indices] = np.random.uniform(low=100, high=150, size=20)

# Winsorization (capping)
def winsorize(data, limits):
    lower_limit = np.percentile(data, limits[0])
    upper_limit = np.percentile(data, limits[1])
    winsorized = np.copy(data)
    winsorized[winsorized < lower_limit] = lower_limit
    winsorized[winsorized > upper_limit] = upper_limit
    return winsorized

winsorized_data = winsorize(data_with_outliers, (5, 95))

# Plot original vs winsorized
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.boxplot(data_with_outliers)
ax1.set_title('Data with Outliers')
ax1.set_ylabel('Value')

ax2.boxplot(winsorized_data)
ax2.set_title('Winsorized Data (5th-95th percentiles)')
ax2.set_ylabel('Value')

plt.tight_layout()
plt.savefig('outlier_handling.png')
plt.close()

# Print summary of transformations
print("\nTransformation Summary:")
print("1. Log Transformation: Reduces positive skew, compresses large values")
print("2. Square Root Transformation: Milder than log, also reduces positive skew")
print("3. Square Transformation: Can reduce negative skew")
print("4. Box-Cox Transformation: Automatically finds the best power transformation")
print("5. Binning: Converts continuous variables to categorical")
print("6. Winsorization: Caps extreme values to handle outliers")

# Save the transformed dataset
df.to_csv('transformed_features_dataset.csv', index=False)
print("\nTransformed dataset saved as 'transformed_features_dataset.csv'")