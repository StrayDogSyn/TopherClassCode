"""
Introduction to Polynomial and Interaction Features
--------------------------------------------------
STUDENT TASKS:
1. Complete the functions to create polynomial features (squares and cubes)
2. Complete the interaction features function to create pairwise combinations
3. Visualize how these new features affect the ability to separate classes
4. Determine which derived features have the strongest correlation with the target
5. Create one domain-specific polynomial or interaction feature of your own design

This starter code provides the basic structure for exploring how transforming
features can reveal non-linear relationships and improve model performance.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.preprocessing import PolynomialFeatures

# Generate a synthetic non-linear dataset (moons dataset)
np.random.seed(42)
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)

# Create a dataframe for easier manipulation
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['target'] = y

print("Original Dataset:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# TODO: Function to create polynomial features (square and cubic terms)
def create_polynomial_features(dataframe):
    """
    Create polynomial features (squared and cubed) for each numeric feature.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added polynomial features
    """
    df_poly = dataframe.copy()
    
    # Your code here:
    # 1. Create squared features (feature1^2, feature2^2)
    
    # 2. Create cubic features (feature1^3, feature2^3)
    
    return df_poly

# TODO: Function to create interaction features
def create_interaction_features(dataframe):
    """
    Create interaction features (multiplication of feature pairs).
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added interaction features
    """
    df_interact = dataframe.copy()
    
    # Your code here:
    # Create feature interactions (e.g., feature1 * feature2)
    
    return df_interact

# Combine all features
def enhance_features(dataframe):
    """
    Apply both polynomial and interaction transformations.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with all enhanced features
    """
    # First add polynomial features
    df_enhanced = create_polynomial_features(dataframe)
    
    # Then add interaction features
    df_enhanced = create_interaction_features(df_enhanced)
    
    return df_enhanced

# Apply feature enhancement
enhanced_df = enhance_features(df)

# TODO: Complete this visualization to compare original vs. enhanced features
def visualize_features(original_df, enhanced_df):
    """
    Create visualizations comparing original and enhanced features.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Original features visualization
    axes[0, 0].scatter(original_df['feature1'], original_df['feature2'], 
                       c=original_df['target'], cmap='viridis', alpha=0.6)
    axes[0, 0].set_title('Original Features: feature1 vs feature2')
    axes[0, 0].set_xlabel('feature1')
    axes[0, 0].set_ylabel('feature2')
    
    # TODO: Add three more visualizations showing your enhanced features
    # Suggestion: Show interaction features, polynomial features, and a combination
    
    # Example (uncomment and modify):
    # axes[0, 1].scatter(enhanced_df['feature1_squared'], enhanced_df['feature2'], 
    #                   c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    # axes[0, 1].set_title('Enhanced Features: feature1_squared vs feature2')
    # axes[0, 1].set_xlabel('feature1_squared')
    # axes[0, 1].set_ylabel('feature2')
    
    plt.tight_layout()
    plt.savefig('polynomial_features_visualization.png')
    plt.show()

# Visualization of features
visualize_features(df, enhanced_df)

# TODO: Analyze the correlation of features with the target
def analyze_feature_importance(enhanced_df):
    """
    Calculate and display correlation of features with target.
    """
    # Your code here:
    # 1. Calculate correlation of all features with target
    
    # 2. Sort correlations in descending order
    
    # 3. Display the top features
    
    pass

# Feature importance analysis
analyze_feature_importance(enhanced_df)

# TODO: Create one domain-specific feature of your own design
def create_custom_feature(dataframe):
    """
    Create a custom feature that might be relevant for this dataset.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added custom feature
    """
    df_custom = dataframe.copy()
    
    # Your code here:
    # Create a custom feature that you think might be useful
    # For example: distance from origin, angle, or another transformation
    
    return df_custom

# Apply your custom feature
final_df = create_custom_feature(enhanced_df)

# Save the enhanced dataset
final_df.to_csv('dataset_with_polynomial_features.csv', index=False)
print("\nEnhanced dataset saved as 'dataset_with_polynomial_features.csv'")

# BONUS: Try using scikit-learn's PolynomialFeatures
# Compare your manual implementation with scikit-learn's implementation
def compare_with_sklearn(original_df):
    """
    Compare manual polynomial features with scikit-learn's implementation.
    """
    # Extract features (exclude target)
    X = original_df.drop('target', axis=1).values
    
    # Create polynomial features using scikit-learn
    poly = PolynomialFeatures(degree=3, include_bias=False)
    X_poly = poly.fit_transform(X)
    
    # Create DataFrame with sklearn's polynomial features
    feature_names = poly.get_feature_names_out(['feature1', 'feature2'])
    df_sklearn_poly = pd.DataFrame(X_poly, columns=feature_names)
    df_sklearn_poly['target'] = original_df['target'].values
    
    print("\nScikit-learn PolynomialFeatures Output:")
    print(df_sklearn_poly.head())
    
    return df_sklearn_poly

# Uncomment to compare with scikit-learn
# sklearn_poly_df = compare_with_sklearn(df)