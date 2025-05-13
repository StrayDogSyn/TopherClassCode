"""
Feature Scaling Workshop
-----------------------
STUDENT TASKS:
1. Complete the functions for different scaling methods
2. Run the scaling operations on the provided dataset
3. Visualize the effect of scaling on feature distributions
4. Compare the performance of models with different scaling methods
5. Answer the questions in the "Conclusions" section
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

# Print basic dataset info
print("Original Dataset Stats:")
print(df.describe().round(2))

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
    
    print(f"\n{scaler_name} Scaling Results:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    return model, mse, r2

# TODO: Complete the min-max scaling implementation
def apply_min_max_scaling(X_train, X_test):
    """
    Apply min-max scaling to the data
    Returns: scaled training and test data
    """
    # Your code here
    
    # Create a MinMaxScaler
    
    # Fit the scaler on training data and transform both train and test
    
    # Return the scaled data
    pass

# TODO: Complete the standardization implementation
def apply_standardization(X_train, X_test):
    """
    Apply standardization (z-score normalization) to the data
    Returns: scaled training and test data
    """
    # Your code here
    
    # Create a StandardScaler
    
    # Fit the scaler on training data and transform both train and test
    
    # Return the scaled data
    pass

# TODO: Implement your own custom scaler from scratch
def apply_custom_scaling(X_train, X_test):
    """
    Implement a custom scaling method of your choice
    Ideas: median normalization, decimal scaling, etc.
    Returns: scaled training and test data
    """
    # Your code here - implement your own scaling method without using sklearn
    
    pass

# TODO: Run models with different scaling methods and compare results

# 1. No Scaling (baseline)
print("\n--- Evaluating model with no scaling ---")
model_no_scaling, mse_no_scaling, r2_no_scaling = evaluate_model(
    X_train, X_test, y_train, y_test, "No Scaling"
)

# 2. TODO: Apply Min-Max scaling and evaluate
print("\n--- Evaluating model with min-max scaling ---")
# Your code here

# 3. TODO: Apply Standardization and evaluate
print("\n--- Evaluating model with standardization ---")
# Your code here

# 4. TODO: Apply your custom scaling and evaluate
print("\n--- Evaluating model with custom scaling ---")
# Your code here

# TODO: Create a bar chart comparing model performance across different scaling methods
def plot_performance_comparison():
    """Create a bar chart comparing MSE and R² for different scaling methods"""
    # Your code here
    pass

# TODO: Answer these questions in your report:
"""
Conclusions:
-----------
1. What is the difference between normalization and standardization?

2. Which scaling method performed best on this dataset? Why do you think that is?

3. Would the best scaling method be the same for all ML algorithms? Why or why not?

4. In what situations would you choose:
   a) Min-max scaling
   b) Standardization
   c) Your custom scaling method

5. Why is feature scaling important for many machine learning algorithms?
"""