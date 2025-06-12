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
    
    # 1. Create squared features (feature1^2, feature2^2)
    df_poly['feature1_squared'] = df_poly['feature1'] ** 2
    df_poly['feature2_squared'] = df_poly['feature2'] ** 2
    
    # 2. Create cubic features (feature1^3, feature2^3)
    df_poly['feature1_cubed'] = df_poly['feature1'] ** 3
    df_poly['feature2_cubed'] = df_poly['feature2'] ** 3
    
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
    
    # Create feature interactions (e.g., feature1 * feature2)
    df_interact['feature1_x_feature2'] = df_interact['feature1'] * df_interact['feature2']
    
    # Additional interaction with polynomial features if they exist
    if 'feature1_squared' in df_interact.columns:
        df_interact['feature1_squared_x_feature2'] = df_interact['feature1_squared'] * df_interact['feature2']
        df_interact['feature1_x_feature2_squared'] = df_interact['feature1'] * df_interact['feature2_squared']
    
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
print("\n" + "="*60)
print("APPLYING FEATURE ENHANCEMENTS")
print("="*60)
enhanced_df = enhance_features(df)
print(f"Enhanced dataframe shape: {enhanced_df.shape}")
print("New polynomial features added:")
print("- feature1_squared, feature2_squared")
print("- feature1_cubed, feature2_cubed")
print("- feature1_x_feature2")
print("- feature1_squared_x_feature2, feature1_x_feature2_squared")

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
    
    # Visualization of polynomial features (squared)
    axes[0, 1].scatter(enhanced_df['feature1_squared'], enhanced_df['feature2_squared'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[0, 1].set_title('Polynomial Features: feature1² vs feature2²')
    axes[0, 1].set_xlabel('feature1²')
    axes[0, 1].set_ylabel('feature2²')
    
    # Visualization of interaction features
    axes[1, 0].scatter(enhanced_df['feature1_x_feature2'], enhanced_df['feature2'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[1, 0].set_title('Interaction Features: (feature1 × feature2) vs feature2')
    axes[1, 0].set_xlabel('feature1 × feature2')
    axes[1, 0].set_ylabel('feature2')
    
    # Visualization of cubic features
    axes[1, 1].scatter(enhanced_df['feature1_cubed'], enhanced_df['feature2_cubed'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.6)
    axes[1, 1].set_title('Cubic Features: feature1³ vs feature2³')
    axes[1, 1].set_xlabel('feature1³')
    axes[1, 1].set_ylabel('feature2³')
    
    plt.tight_layout()
    plt.savefig('polynomial_features_visualization.png')
    plt.show()

# Visualization of features
print("\n" + "="*60)
print("CREATING VISUALIZATIONS")
print("="*60)
visualize_features(df, enhanced_df)

# TODO: Analyze the correlation of features with the target
def analyze_feature_importance(enhanced_df):
    """
    Calculate and display correlation of features with target.
    """
    # 1. Calculate correlation of all features with target
    correlations = enhanced_df.corr()['target'].drop('target')  # Remove self-correlation
    
    # 2. Sort correlations in descending order by absolute value
    sorted_correlations = correlations.abs().sort_values(ascending=False)
    
    # 3. Display the top features
    print("\nFeature Correlations with Target (sorted by absolute value):")
    print("-" * 60)
    for feature, corr_value in sorted_correlations.items():
        actual_corr = correlations[feature]
        print(f"{feature:25s}: {actual_corr:8.4f} (|{corr_value:.4f}|)")
    
    # Visualize top correlations
    plt.figure(figsize=(12, 6))
    top_features = sorted_correlations.head(8)  # Top 8 features
    top_actual_corr = [correlations[feature] for feature in top_features.index]
    
    bars = plt.bar(range(len(top_features)), top_actual_corr)
    plt.xticks(range(len(top_features)), top_features.index, rotation=45, ha='right')
    plt.ylabel('Correlation with Target')
    plt.title('Top Features by Correlation with Target')
    plt.grid(True, alpha=0.3)
    
    # Color bars based on positive/negative correlation
    for i, bar in enumerate(bars):
        if top_actual_corr[i] >= 0:
            bar.set_color('green')
        else:
            bar.set_color('red')
    
    plt.tight_layout()
    plt.savefig('feature_correlations.png')
    plt.show()
    
    return sorted_correlations

# Feature importance analysis
print("\n" + "="*60)
print("ANALYZING FEATURE IMPORTANCE")
print("="*60)
correlations = analyze_feature_importance(enhanced_df)

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
    
    # Custom feature 1: Distance from origin (Euclidean distance)
    # This can help capture radial patterns in the data
    df_custom['distance_from_origin'] = np.sqrt(df_custom['feature1']**2 + df_custom['feature2']**2)
    
    # Custom feature 2: Angle/direction from origin
    # This can help capture angular patterns in the data
    df_custom['angle_from_origin'] = np.arctan2(df_custom['feature2'], df_custom['feature1'])
    
    # Custom feature 3: Sum and difference of features
    # These can capture diagonal patterns
    df_custom['feature_sum'] = df_custom['feature1'] + df_custom['feature2']
    df_custom['feature_diff'] = df_custom['feature1'] - df_custom['feature2']
    
    # Custom feature 4: Asymmetric interaction (feature1² × feature2)
    # This creates a more complex interaction than simple multiplication
    df_custom['asymmetric_interaction'] = df_custom['feature1']**2 * df_custom['feature2']
    
    print("\nCustom features created:")
    print("1. distance_from_origin: √(feature1² + feature2²)")
    print("2. angle_from_origin: arctan2(feature2, feature1)")
    print("3. feature_sum: feature1 + feature2")
    print("4. feature_diff: feature1 - feature2")
    print("5. asymmetric_interaction: feature1² × feature2")
    
    return df_custom

# Apply your custom feature
print("\n" + "="*60)
print("CREATING CUSTOM FEATURES")
print("="*60)
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

# Compare with scikit-learn implementation
print("\n" + "="*60)
print("BONUS: Comparing with Scikit-learn PolynomialFeatures")
print("="*60)
sklearn_poly_df = compare_with_sklearn(df)

# Display comparison of feature counts
manual_features = len(final_df.columns) - 1  # Exclude target
sklearn_features = len(sklearn_poly_df.columns) - 1  # Exclude target

print(f"\nFeature comparison:")
print(f"Manual implementation: {manual_features} features")
print(f"Scikit-learn implementation: {sklearn_features} features")
print(f"Final dataset shape: {final_df.shape}")
print(f"Scikit-learn dataset shape: {sklearn_poly_df.shape}")

# Final summary and analysis
print("\n" + "="*60)
print("FINAL SUMMARY AND INSIGHTS")
print("="*60)

print(f"\nDataset Evolution:")
print(f"Original features: 2 (feature1, feature2)")
print(f"After polynomial features: {len(enhanced_df.columns)-1}")
print(f"After custom features: {len(final_df.columns)-1}")

print(f"\nTop 3 Most Correlated Features with Target:")
top_3_features = correlations.abs().head(3)
for i, (feature, corr_abs) in enumerate(top_3_features.items(), 1):
    actual_corr = correlations[feature]
    print(f"{i}. {feature}: {actual_corr:.4f}")

print(f"\nFeature Engineering Insights:")
print("- Polynomial features help capture non-linear relationships")
print("- Interaction features reveal relationships between feature combinations")
print("- Custom features like distance and angle can capture geometric patterns")
print("- The moons dataset benefits from features that capture its curved structure")

print(f"\nFiles saved:")
print("- dataset_with_polynomial_features.csv (enhanced dataset)")
print("- polynomial_features_visualization.png (feature visualizations)")
print("- feature_correlations.png (correlation analysis)")

print(f"\nAssignment completed successfully! 🎉")
print("All required functions have been implemented with comprehensive comments.")