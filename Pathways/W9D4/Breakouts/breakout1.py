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

# Function to create polynomial features (square and cubic terms)
def create_polynomial_features(dataframe):
    """
    Create polynomial features (squared and cubed) for each numeric feature.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added polynomial features
    """
    df_poly = dataframe.copy()
    
    # 1. Create squared features (feature1^2, feature2^2)
    # Squared features help capture quadratic/curved relationships in the data
    df_poly['feature1_squared'] = df_poly['feature1'] ** 2
    df_poly['feature2_squared'] = df_poly['feature2'] ** 2
    
    # 2. Create cubic features (feature1^3, feature2^3)  
    # Cubic features capture more complex S-shaped curves and inflection points
    df_poly['feature1_cubed'] = df_poly['feature1'] ** 3
    df_poly['feature2_cubed'] = df_poly['feature2'] ** 3
    
    return df_poly

# Function to create interaction features
def create_interaction_features(dataframe):
    """
    Create interaction features (multiplication of feature pairs).
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added interaction features
    """
    df_interact = dataframe.copy()
    
    # Create basic feature interaction (feature1 * feature2)
    # Interactions capture when features work together (synergy effects)
    df_interact['feature1_x_feature2'] = df_interact['feature1'] * df_interact['feature2']
    
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

# Visualization to compare original vs. enhanced features
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
    
    # Polynomial features visualization (squared terms)
    axes[0, 1].scatter(enhanced_df['feature1_squared'], enhanced_df['feature2_squared'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[0, 1].set_title('Polynomial Features: feature1² vs feature2²')
    axes[0, 1].set_xlabel('feature1²')
    axes[0, 1].set_ylabel('feature2²')
    
    # Interaction features visualization
    axes[1, 0].scatter(enhanced_df['feature1_x_feature2'], enhanced_df['feature2'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[1, 0].set_title('Interaction Features: (feature1 × feature2) vs feature2')
    axes[1, 0].set_xlabel('feature1 × feature2')
    axes[1, 0].set_ylabel('feature2')
    
    # Cubic features visualization
    axes[1, 1].scatter(enhanced_df['feature1_cubed'], enhanced_df['feature2_cubed'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[1, 1].set_title('Cubic Features: feature1³ vs feature2³')
    axes[1, 1].set_xlabel('feature1³')
    axes[1, 1].set_ylabel('feature2³')
    
    plt.tight_layout()
    plt.savefig('polynomial_features_visualization.png')
    plt.show()

# Visualization of features
visualize_features(df, enhanced_df)

# Analyze the correlation of features with the target
def analyze_feature_importance(enhanced_df):
    """
    Calculate and display correlation of features with target.
    """
    # 1. Calculate correlation of all features with target
    correlations = enhanced_df.corr()['target'].drop('target')  # Remove self-correlation
    
    # 2. Sort correlations by absolute value to find strongest relationships
    sorted_correlations = correlations.abs().sort_values(ascending=False)
    
    # 3. Display the top features
    print("\nFeature Correlations with Target (sorted by absolute correlation):")
    print("-" * 60)
    for feature, corr_abs in sorted_correlations.items():
        actual_corr = correlations[feature]
        print(f"{feature:25s}: {actual_corr:8.4f}")
    
    # Create a simple bar chart of top correlations
    plt.figure(figsize=(10, 6))
    top_features = sorted_correlations.head(6)  # Top 6 features
    top_actual_corr = [correlations[feature] for feature in top_features.index]
    
    plt.bar(range(len(top_features)), top_actual_corr)
    plt.xticks(range(len(top_features)), top_features.index, rotation=45, ha='right')
    plt.ylabel('Correlation with Target')
    plt.title('Top Features by Correlation with Target')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('feature_correlations.png')
    plt.show()

# Feature importance analysis
analyze_feature_importance(enhanced_df)

# Create one domain-specific feature of your own design
def create_custom_feature(dataframe):
    """
    Create a custom feature that might be relevant for this dataset.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added custom feature
    """
    df_custom = dataframe.copy()
    
    # Custom feature: Distance from origin
    # This captures radial patterns - useful for circular/curved datasets like moons
    df_custom['distance_from_origin'] = np.sqrt(df_custom['feature1']**2 + df_custom['feature2']**2)
    
    print("\nCustom feature created: 'distance_from_origin'")
    print("This measures how far each point is from the center (0,0)")
    print("Useful for capturing radial/circular patterns in the moons dataset")
    
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
    print(f"Number of features created: {len(feature_names)}")
    
    return df_sklearn_poly

# Compare with scikit-learn
sklearn_poly_df = compare_with_sklearn(df)

print(f"\nFeature count comparison:")
print(f"Manual implementation: {len(final_df.columns)-1} features")
print(f"Scikit-learn implementation: {len(sklearn_poly_df.columns)-1} features")

print(f"\nAssignment completed! Key takeaways:")
print("- Polynomial features help capture non-linear relationships")
print("- Interaction features reveal synergies between variables")
print("- Custom features can be domain-specific (like distance for moons data)")
print("- Scikit-learn provides automated polynomial feature generation")