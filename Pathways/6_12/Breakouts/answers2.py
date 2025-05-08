"""
Feature Scaling Workshop - ANSWER SHEET
--------------------------------------
This file contains the completed solutions for the Feature Scaling Workshop.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set seed for reproducibility
np.random.seed(42)

# Load diabetes dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

# Create a DataFrame
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Save basic dataset info to file instead of printing
with open('dataset_info.txt', 'w') as f:
    f.write("Original Dataset Stats:\n")
    f.write(df.describe().round(2).to_string())

# Create a boxplot of original data to see the scale differences
plt.figure(figsize=(10, 6))
df.boxplot()
plt.title('Original Feature Scales')
plt.ylabel('Value')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('original_feature_scales.png')
plt.close()

# Split data for model evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Function to plot data before and after scaling
def plot_scaling_comparison(original_data, scaled_data, feature_names, scaler_name, filename):
    """Plot boxplots of data before and after scaling"""
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

# Function to evaluate model performance
def evaluate_model(X_train_scaled, X_test_scaled, y_train, y_test, scaler_name):
    """Train and evaluate a linear regression model"""
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    with open(f'{scaler_name.lower().replace(" ", "_")}_results.txt', 'w') as f:
        f.write(f"{scaler_name} Scaling Results:\n")
        f.write(f"Mean Squared Error: {mse:.2f}\n")
        f.write(f"R² Score: {r2:.4f}\n")
    
    return model, mse, r2

# Completed min-max scaling implementation
def apply_min_max_scaling(X_train, X_test):
    """
    Apply min-max scaling to the data
    Returns: scaled training and test data
    """
    # Create a MinMaxScaler
    min_max_scaler = MinMaxScaler()
    
    # Fit the scaler on training data and transform both train and test
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.transform(X_test)
    
    # For visualization
    X_full_scaled = min_max_scaler.fit_transform(X)
    plot_scaling_comparison(X, X_full_scaled, feature_names, "Min-Max", "minmax_scaling.png")
    
    return X_train_scaled, X_test_scaled

# Completed standardization implementation
def apply_standardization(X_train, X_test):
    """
    Apply standardization (z-score normalization) to the data
    Returns: scaled training and test data
    """
    # Create a StandardScaler
    standard_scaler = StandardScaler()
    
    # Fit the scaler on training data and transform both train and test
    X_train_scaled = standard_scaler.fit_transform(X_train)
    X_test_scaled = standard_scaler.transform(X_test)
    
    # For visualization
    X_full_scaled = standard_scaler.fit_transform(X)
    plot_scaling_comparison(X, X_full_scaled, feature_names, "Standardization", "standardization.png")
    
    return X_train_scaled, X_test_scaled

# Implemented custom scaling method (Median-IQR scaling)
def apply_custom_scaling(X_train, X_test):
    """
    Custom scaling method: Median and IQR based scaling
    Similar to robust scaling but implemented manually
    Returns: scaled training and test data
    """
    # Calculate median and IQR for each feature using training data
    medians = np.median(X_train, axis=0)
    q75 = np.percentile(X_train, 75, axis=0)
    q25 = np.percentile(X_train, 25, axis=0)
    iqr = q75 - q25
    
    # Handle potential division by zero
    iqr = np.where(iqr == 0, 1, iqr)
    
    # Apply scaling to train and test data
    X_train_scaled = (X_train - medians) / iqr
    X_test_scaled = (X_test - medians) / iqr
    
    # For visualization
    X_full = X.copy()
    X_full_scaled = (X_full - medians) / iqr
    plot_scaling_comparison(X, X_full_scaled, feature_names, "Median-IQR", "custom_scaling.png")
    
    return X_train_scaled, X_test_scaled

# Run models with different scaling methods and compare results

# 1. No Scaling (baseline)
model_no_scaling, mse_no_scaling, r2_no_scaling = evaluate_model(
    X_train, X_test, y_train, y_test, "No Scaling"
)

# 2. Apply Min-Max scaling and evaluate
X_train_minmax, X_test_minmax = apply_min_max_scaling(X_train, X_test)
model_minmax, mse_minmax, r2_minmax = evaluate_model(
    X_train_minmax, X_test_minmax, y_train, y_test, "Min-Max"
)

# 3. Apply Standardization and evaluate
X_train_standard, X_test_standard = apply_standardization(X_train, X_test)
model_standard, mse_standard, r2_standard = evaluate_model(
    X_train_standard, X_test_standard, y_train, y_test, "Standardization"
)

# 4. Apply custom scaling and evaluate
X_train_custom, X_test_custom = apply_custom_scaling(X_train, X_test)
model_custom, mse_custom, r2_custom = evaluate_model(
    X_train_custom, X_test_custom, y_train, y_test, "Custom Median-IQR"
)

# Create bar chart comparing model performance across different scaling methods
def plot_performance_comparison():
    """Create a bar chart comparing MSE and R² for different scaling methods"""
    scaling_methods = ['No Scaling', 'Min-Max', 'Standardization', 'Median-IQR']
    mse_values = [mse_no_scaling, mse_minmax, mse_standard, mse_custom]
    r2_values = [r2_no_scaling, r2_minmax, r2_standard, r2_custom]
    
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

# Generate the performance comparison chart
plot_performance_comparison()

# Create a dataset with mixed scales to demonstrate importance of scaling
np.random.seed(42)
n_samples = 100

# Create features with different scales
large_scale = np.random.normal(1000, 100, n_samples)
small_scale = np.random.normal(0.1, 0.01, n_samples)

# Create a target that depends equally on both features
target = 0.5 * (large_scale - 1000) / 100 + 0.5 * (small_scale - 0.1) / 0.01 + np.random.normal(0, 0.5, n_samples)

# Create DataFrame for the mixed scales example
mixed_df = pd.DataFrame({
    'large_scale': large_scale,
    'small_scale': small_scale,
    'target': target
})

# Save mixed scales data info
with open('mixed_scales_info.txt', 'w') as f:
    f.write("Mixed Scales Dataset:\n")
    f.write(mixed_df.describe().to_string())

# Split the mixed scales data
X_mixed = mixed_df[['large_scale', 'small_scale']].values
y_mixed = mixed_df['target'].values
X_mixed_train, X_mixed_test, y_mixed_train, y_mixed_test = train_test_split(
    X_mixed, y_mixed, test_size=0.2, random_state=42
)

# Train a model without scaling
model_mixed_no_scaling = LinearRegression()
model_mixed_no_scaling.fit(X_mixed_train, y_mixed_train)

# Train a model with standardization
scaler_mixed = StandardScaler()
X_mixed_train_scaled = scaler_mixed.fit_transform(X_mixed_train)
X_mixed_test_scaled = scaler_mixed.transform(X_mixed_test)
model_mixed_with_scaling = LinearRegression()
model_mixed_with_scaling.fit(X_mixed_train_scaled, y_mixed_train)

# Compare coefficients
coef_no_scaling = model_mixed_no_scaling.coef_
coef_with_scaling = model_mixed_with_scaling.coef_

# Save coefficient comparison
with open('mixed_scales_coefficients.txt', 'w') as f:
    f.write("Linear Regression Coefficients Comparison:\n\n")
    f.write("Without Scaling:\n")
    f.write(f"Large Scale Feature: {coef_no_scaling[0]:.8f}\n")
    f.write(f"Small Scale Feature: {coef_no_scaling[1]:.8f}\n\n")
    f.write("With Standardization:\n")
    f.write(f"Large Scale Feature: {coef_with_scaling[0]:.8f}\n")
    f.write(f"Small Scale Feature: {coef_with_scaling[1]:.8f}\n")

# Visualize coefficients
feature_names_mixed = ['Large Scale', 'Small Scale']
plt.figure(figsize=(10, 6))
x = np.arange(len(feature_names_mixed))
width = 0.35

plt.bar(x - width/2, coef_no_scaling, width, label='Without Scaling')
plt.bar(x + width/2, coef_with_scaling, width, label='With Standardization')
plt.title('Feature Coefficients Comparison')
plt.xticks(x, feature_names_mixed)
plt.ylabel('Coefficient Value')
plt.legend()
plt.savefig('mixed_scales_coefficient_comparison.png')
plt.close()

"""
Answers to Questions:
--------------------

1. What is the difference between normalization and standardization?
   - Normalization (Min-Max scaling) scales features to a fixed range (typically 0-1)
   - Standardization scales features to have mean=0 and standard deviation=1
   - Normalization is affected more by outliers than standardization

2. Which scaling method performed best on this dataset? Why?
   - Standardization performed slightly better because the features in the diabetes 
     dataset have different distributions and some may have outliers
   - The difference is small because Linear Regression is scale-invariant for the 
     coefficients (though not for regularization)

3. Would the best scaling method be the same for all ML algorithms?
   - No, different algorithms have different sensitivities to feature scaling
   - Distance-based algorithms (K-means, KNN) need features on similar scales
   - Tree-based methods (Random Forest, Decision Trees) are not affected by monotonic 
     transformations like scaling
   - Neural networks typically work better with normalized (0-1) features

4. When to choose different scaling methods:
   a) Min-max scaling:
      - When you need values in a bounded interval (e.g., for neural networks)
      - When the distribution is not Gaussian or when the standard deviation is small
   
   b) Standardization:
      - For general-purpose scaling with unknown distribution
      - When outliers are present (less sensitive than min-max)
      - For algorithms assuming normally distributed data
   
   c) Median-IQR scaling (custom method):
      - When data has many outliers
      - When you want to preserve the general distribution shape but need scaling

5. Why is feature scaling important?
   - Prevents features with larger scales from dominating the learning process
   - Essential for algorithms using distance measures (K-means, KNN, SVM)
   - Improves convergence speed in gradient-based algorithms
   - Required for regularization to treat all features equally
   - Makes model coefficients more interpretable in terms of relative importance
"""

print("All analyses completed. Results saved to files.")