"""
Normalization and Standardization
--------------------------------
This script demonstrates various scaling techniques for numerical features
and explains when to use each method.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set seed for reproducibility
np.random.seed(42)

# Load a real dataset for demonstration
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Create a DataFrame with the feature names
feature_names = diabetes.feature_names
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

print("Original Dataset:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# Check for differences in feature scales
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(ax=ax)
ax.set_title('Original Feature Scales')
ax.set_ylabel('Value')
ax.tick_params(axis='x', rotation=90)
plt.tight_layout()
plt.savefig('original_feature_scales.png')
plt.close()

# Split data for later model evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Function to train a model and evaluate performance
def evaluate_model(X_train_scaled, X_test_scaled, y_train, y_test, scaler_name):
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\n{scaler_name} Scaling Results:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    return model, mse, r2

# Function to plot data before and after scaling
def plot_scaling_comparison(original_data, scaled_data, feature_names, scaler_name, filename):
    n_features = original_data.shape[1]
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    # Original data
    axes[0].boxplot(original_data)
    axes[0].set_title('Original Feature Scales')
    axes[0].set_xticklabels(feature_names, rotation=90)
    axes[0].set_ylabel('Value')
    
    # Scaled data
    axes[1].boxplot(scaled_data)
    axes[1].set_title(f'After {scaler_name} Scaling')
    axes[1].set_xticklabels(feature_names, rotation=90)
    axes[1].set_ylabel('Value')
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 1. Min-Max Scaling (Normalization)
# Scales features to a fixed range, usually 0 to 1
min_max_scaler = MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
X_test_minmax = min_max_scaler.transform(X_test)

# Transform for visualization
X_minmax = min_max_scaler.fit_transform(X)
plot_scaling_comparison(X, X_minmax, feature_names, "Min-Max", "minmax_scaling.png")

# Evaluate model with min-max scaling
model_minmax, mse_minmax, r2_minmax = evaluate_model(
    X_train_minmax, X_test_minmax, y_train, y_test, "Min-Max"
)

# 2. Z-score Standardization
# Scales features to have zero mean and unit variance
standard_scaler = StandardScaler()
X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

# Transform for visualization
X_standard = standard_scaler.fit_transform(X)
plot_scaling_comparison(X, X_standard, feature_names, "Z-score", "zscore_scaling.png")

# Evaluate model with standardization
model_standard, mse_standard, r2_standard = evaluate_model(
    X_train_standard, X_test_standard, y_train, y_test, "Z-score"
)

# 3. Robust Scaling
# Scales features using statistics that are robust to outliers
robust_scaler = RobustScaler()
X_train_robust = robust_scaler.fit_transform(X_train)
X_test_robust = robust_scaler.transform(X_test)

# Transform for visualization
X_robust = robust_scaler.fit_transform(X)
plot_scaling_comparison(X, X_robust, feature_names, "Robust", "robust_scaling.png")

# Evaluate model with robust scaling
model_robust, mse_robust, r2_robust = evaluate_model(
    X_train_robust, X_test_robust, y_train, y_test, "Robust"
)

# 4. Max Absolute Scaling
# Scales features by dividing by the maximum absolute value
maxabs_scaler = MaxAbsScaler()
X_train_maxabs = maxabs_scaler.fit_transform(X_train)
X_test_maxabs = maxabs_scaler.transform(X_test)

# Transform for visualization
X_maxabs = maxabs_scaler.fit_transform(X)
plot_scaling_comparison(X, X_maxabs, feature_names, "Max Absolute", "maxabs_scaling.png")

# Evaluate model with max absolute scaling
model_maxabs, mse_maxabs, r2_maxabs = evaluate_model(
    X_train_maxabs, X_test_maxabs, y_train, y_test, "Max Absolute"
)

# Compare the performance of different scaling methods
scaling_methods = ['No Scaling', 'Min-Max', 'Z-score', 'Robust', 'Max Absolute']

# First train a model without scaling for comparison
model_no_scaling, mse_no_scaling, r2_no_scaling = evaluate_model(
    X_train, X_test, y_train, y_test, "No Scaling"
)

# Collect MSE and R² metrics
mse_values = [mse_no_scaling, mse_minmax, mse_standard, mse_robust, mse_maxabs]
r2_values = [r2_no_scaling, r2_minmax, r2_standard, r2_robust, r2_maxabs]

# Plot comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# MSE comparison (lower is better)
ax1.bar(scaling_methods, mse_values, color='salmon')
ax1.set_title('Mean Squared Error (Lower is Better)')
ax1.set_ylabel('MSE')
ax1.tick_params(axis='x', rotation=45)

# R² comparison (higher is better)
ax2.bar(scaling_methods, r2_values, color='skyblue')
ax2.set_title('R² Score (Higher is Better)')
ax2.set_ylabel('R²')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('scaling_performance_comparison.png')
plt.close()

# Create a dataset with mixed scales to demonstrate the importance of scaling
np.random.seed(42)
n_samples = 500

# Create a dataset with features on different scales
large_scale_feature = np.random.normal(1000, 100, n_samples)  # Mean 1000, std 100
medium_scale_feature = np.random.normal(10, 2, n_samples)     # Mean 10, std 2
small_scale_feature = np.random.normal(0.1, 0.01, n_samples)  # Mean 0.1, std 0.01

# Create a target variable influenced by all features equally
target = (0.3 * (large_scale_feature - 1000) / 100 + 
          0.3 * (medium_scale_feature - 10) / 2 + 
          0.3 * (small_scale_feature - 0.1) / 0.01 + 
          np.random.normal(0, 0.5, n_samples))  # Add some noise

# Create a DataFrame
mixed_scales_df = pd.DataFrame({
    'large_scale': large_scale_feature,
    'medium_scale': medium_scale_feature,
    'small_scale': small_scale_feature,
    'target': target
})

print("\nMixed Scales Dataset:")
print(mixed_scales_df.describe())

# Split the mixed scales data
X_mixed = mixed_scales_df[['large_scale', 'medium_scale', 'small_scale']].values
y_mixed = mixed_scales_df['target'].values
X_mixed_train, X_mixed_test, y_mixed_train, y_mixed_test = train_test_split(
    X_mixed, y_mixed, test_size=0.2, random_state=42
)

# Train a linear regression model without scaling
model_mixed_no_scaling = LinearRegression()
model_mixed_no_scaling.fit(X_mixed_train, y_mixed_train)
y_mixed_pred_no_scaling = model_mixed_no_scaling.predict(X_mixed_test)
mse_mixed_no_scaling = mean_squared_error(y_mixed_test, y_mixed_pred_no_scaling)

# Check the coefficients
print("\nLinear Regression Coefficients Without Scaling:")
print(f"Large Scale Feature: {model_mixed_no_scaling.coef_[0]:.8f}")
print(f"Medium Scale Feature: {model_mixed_no_scaling.coef_[1]:.8f}")
print(f"Small Scale Feature: {model_mixed_no_scaling.coef_[2]:.8f}")
print(f"MSE: {mse_mixed_no_scaling:.4f}")

# Apply standardization to the mixed scales data
scaler_mixed = StandardScaler()
X_mixed_train_scaled = scaler_mixed.fit_transform(X_mixed_train)
X_mixed_test_scaled = scaler_mixed.transform(X_mixed_test)

# Train a linear regression model with scaling
model_mixed_with_scaling = LinearRegression()
model_mixed_with_scaling.fit(X_mixed_train_scaled, y_mixed_train)
y_mixed_pred_with_scaling = model_mixed_with_scaling.predict(X_mixed_test_scaled)
mse_mixed_with_scaling = mean_squared_error(y_mixed_test, y_mixed_pred_with_scaling)

# Check the coefficients
print("\nLinear Regression Coefficients With Scaling:")
print(f"Large Scale Feature: {model_mixed_with_scaling.coef_[0]:.8f}")
print(f"Medium Scale Feature: {model_mixed_with_scaling.coef_[1]:.8f}")
print(f"Small Scale Feature: {model_mixed_with_scaling.coef_[2]:.8f}")
print(f"MSE: {mse_mixed_with_scaling:.4f}")

# Visualize the impact of feature scaling on coefficients
feature_names_mixed = ['Large Scale', 'Medium Scale', 'Small Scale']
coef_no_scaling = model_mixed_no_scaling.coef_
coef_with_scaling = model_mixed_with_scaling.coef_

# For visualization, normalize the coefficients to show relative importance
coef_no_scaling_norm = coef_no_scaling / np.sum(np.abs(coef_no_scaling))
coef_with_scaling_norm = coef_with_scaling / np.sum(np.abs(coef_with_scaling))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Without scaling
ax1.bar(feature_names_mixed, coef_no_scaling_norm, color=['red', 'green', 'blue'])
ax1.set_title('Feature Coefficients Without Scaling')
ax1.set_ylabel('Normalized Coefficient')
ax1.set_ylim(-1, 1)

# With scaling
ax2.bar(feature_names_mixed, coef_with_scaling_norm, color=['red', 'green', 'blue'])
ax2.set_title('Feature Coefficients With Scaling')
ax2.set_ylabel('Normalized Coefficient')
ax2.set_ylim(-1, 1)

plt.tight_layout()
plt.savefig('mixed_scales_coefficient_comparison.png')
plt.close()

# Summary of scaling methods
print("\nNormalization and Standardization Summary:")
print("\n1. Min-Max Scaling (Normalization):")
print("   - Scales features to a fixed range, usually 0 to 1")
print("   - Formula: X_scaled = (X - X_min) / (X_max - X_min)")
print("   - Best for: When you need values in a bounded interval")
print("   - Drawbacks: Sensitive to outliers")
print("\n2. Z-score Standardization:")
print("   - Scales features to have mean=0 and variance=1")
print("   - Formula: X_scaled = (X - mean) / std_deviation")
print("   - Best for: Methods that assume features are normally distributed")
print("   - Advantages: Handles outliers better than Min-Max")
print("\n3. Robust Scaling:")
print("   - Uses the median and interquartile range instead of mean and variance")
print("   - Formula: X_scaled = (X - median) / IQR")
print("   - Best for: Datasets with many outliers")
print("   - Advantages: Least affected by outliers")
print("\n4. Max Absolute Scaling:")
print("   - Scales by dividing by maximum absolute value")
print("   - Formula: X_scaled = X / max(abs(X))")
print("   - Best for: Sparse data with zeros that should be preserved")
print("   - Advantages: Preserves zero entries in sparse data")
print("\nWhen to use each method:")
print("- Min-Max: When you need a precise feature range (e.g., for images, neural networks)")
print("- Z-score: For general-purpose scaling, especially with normally distributed features")
print("- Robust: When working with data containing outliers")
print("- Max Absolute: For sparse matrices or when zero values have special meaning")
print("\nImportance of scaling:")
print("- Prevents features with larger scales from dominating the learning process")
print("- Essential for algorithms using distance measures (K-means, KNN)")
print("- Required for gradient-based optimizers and regularization methods")
print("- Improves convergence speed in many algorithms")