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
    '''
    Here, df_poly is a pandas DataFrame. You already have two columns, feature1 and feature2. These two lines create two entirely new columns:

    feature1_squared

    feature2_squared

    And each new column is simply the original feature multiplied by itself (that’s what ** 2 does in Python: raises to the power of 2).

Why square features?

    Non‑linear relationships: Sometimes your target variable (what you’re trying to predict) doesn’t change in a straight line with your features. By adding squared terms, you give your model license to fit curves—think banana‑shaped or parabolic patterns instead of just a straight snub‑nose rifle shot.

    Feature engineering boost: It’s like equipping Cortana with a second GPU—same data, more computational horsepower to catch subtleties.

When to use it?

    Polynomial regression: If you suspect a quadratic effect—maybe doubling feature1 quadruples the outcome—you want squared terms.

    Interaction with other features: You can go further and create cross‑terms (e.g., feature1 * feature2) or even cubes (** 3) if the phenomenon demands it. Just remember: every new feature increases complexity and the risk of overfitting (your model memorizing training data instead of generalizing).
    '''
    
    # 2. Create cubic features (feature1^3, feature2^3)
    df_poly['feature1_cubed'] = df_poly['feature1'] ** 3
    df_poly['feature2_cubed'] = df_poly['feature2'] ** 3
    
    '''
    Why add cubed features?

    Capture even more complex curves: If your relationship isn’t just a simple bend (quadratic) but more of a wiggle or S‑curve, cubic terms let your model bend and twist to match.

    Polynomial flexibility: Cubic gives you that extra degree of freedom—think of it as upgrading from a Magnum to the Spartan Laser for pinpoint nonlinear fits.

When to use it?

    Higher‑order polynomial regression: When you suspect three‑stage effects (e.g., doubling → eight‑fold change).

    Modeling inflection points: Cubics can create those “turning points” where the curve changes direction.

    But watch out: More power = more risk. Overfitting lurks in the shadows if you pile on too many polynomial terms without regularization.
    '''
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
    '''
    What are interaction features?
    
    Think of interactions as "synergy effects" between features. Sometimes the combined effect 
    of two features is more than the sum of their individual effects.
    
    Real-world example: 
    - Height alone might predict basketball performance
    - Weight alone might predict basketball performance  
    - But Height × Weight (a proxy for overall size) might be even more predictive!
    
    Mathematical intuition:
    - Linear model: y = w1*x1 + w2*x2 + b
    - With interaction: y = w1*x1 + w2*x2 + w3*(x1*x2) + b
    
    The x1*x2 term lets the model capture when features work together in non-obvious ways.
    '''
    
    # Additional interaction with polynomial features if they exist
    if 'feature1_squared' in df_interact.columns:
        # Mixing polynomial and original features
        df_interact['feature1_squared_x_feature2'] = df_interact['feature1_squared'] * df_interact['feature2']
        df_interact['feature1_x_feature2_squared'] = df_interact['feature1'] * df_interact['feature2_squared']
        
        '''
        Advanced interactions: Polynomial × Linear
        
        These create even more complex relationships:
        - feature1² × feature2: Quadratic effect of feature1 modulated by feature2
        - feature1 × feature2²: Linear effect of feature1 modulated by quadratic feature2
        
        Think of it like adjusting the "sensitivity" of one feature based on another's value.
        
        Example scenario (moons dataset):
        - Maybe the curvature (feature1²) matters more when feature2 is large
        - Or the linear trend in feature1 becomes stronger when feature2² is high
        
        Use cases:
        - Physics: Force = mass × acceleration (interaction of two linear quantities)
        - Economics: Demand might depend on price × income interaction
        - ML: When feature importance changes based on other feature values
        '''
    
    return df_interact

# Combine all features
def enhance_features(dataframe):
    """
    Apply both polynomial and interaction transformations.
    
    This is our "feature engineering pipeline" - a systematic approach to creating
    more sophisticated features from our raw data.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with all enhanced features
    """
    print("🔧 Starting feature enhancement pipeline...")
    
    # First add polynomial features
    print("   Step 1: Adding polynomial features (x², x³)...")
    df_enhanced = create_polynomial_features(dataframe)
    print(f"   ✅ Polynomial features added. Shape: {df_enhanced.shape}")
    
    # Then add interaction features
    print("   Step 2: Adding interaction features (x₁×x₂, x₁²×x₂, etc.)...")
    df_enhanced = create_interaction_features(df_enhanced)
    print(f"   ✅ Interaction features added. Shape: {df_enhanced.shape}")
    
    '''
    Why this order matters:
    
    1. Polynomials first: Creates x₁², x₂², x₁³, x₂³
    2. Interactions second: Can use both original AND polynomial features
    
    This gives us a rich feature space:
    - Original: x₁, x₂
    - Polynomial: x₁², x₂², x₁³, x₂³  
    - Basic interactions: x₁×x₂
    - Advanced interactions: x₁²×x₂, x₁×x₂²
    
    Feature engineering best practices:
    ✅ Start simple (linear features)
    ✅ Add complexity gradually (polynomials, then interactions)
    ✅ Monitor for overfitting (more features ≠ always better)
    ✅ Domain knowledge helps (what relationships make sense?)
    
    The moons dataset benefits from this approach because:
    - It has curved decision boundaries (polynomials help)
    - The curves interact between dimensions (interactions help)
    - We're transforming a linearly non-separable problem into a richer space
    '''
    
    print("🎉 Feature enhancement pipeline complete!")
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
    
    This function helps us understand how feature transformations change the 
    data distribution and class separability.
    """
    print("📊 Creating 2x2 visualization grid...")
    print("   Each plot shows how different feature transformations affect class separation")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Original features visualization
    print("   🔹 Plot 1: Original features (baseline)")
    axes[0, 0].scatter(original_df['feature1'], original_df['feature2'], 
                       c=original_df['target'], cmap='viridis', alpha=0.7, s=50)
    axes[0, 0].set_title('Original Features: feature1 vs feature2\n(Notice the curved decision boundary)', 
                        fontsize=12, pad=15)
    axes[0, 0].set_xlabel('feature1')
    axes[0, 0].set_ylabel('feature2')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Visualization of polynomial features (squared)
    print("   🔹 Plot 2: Squared features (polynomial transformation)")
    axes[0, 1].scatter(enhanced_df['feature1_squared'], enhanced_df['feature2_squared'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.7, s=50)
    axes[0, 1].set_title('Polynomial Features: feature1² vs feature2²\n(Amplifies distances, changes clustering)', 
                        fontsize=12, pad=15)
    axes[0, 1].set_xlabel('feature1²')
    axes[0, 1].set_ylabel('feature2²')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Visualization of interaction features
    print("   🔹 Plot 3: Interaction features (cross-product)")
    axes[1, 0].scatter(enhanced_df['feature1_x_feature2'], enhanced_df['feature2'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.7, s=50)
    axes[1, 0].set_title('Interaction Features: (feature1 × feature2) vs feature2\n(New axis reveals hidden patterns)', 
                        fontsize=12, pad=15)
    axes[1, 0].set_xlabel('feature1 × feature2 (interaction)')
    axes[1, 0].set_ylabel('feature2')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Visualization of cubic features
    print("   🔹 Plot 4: Cubic features (higher-order polynomial)")
    axes[1, 1].scatter(enhanced_df['feature1_cubed'], enhanced_df['feature2_cubed'], 
                      c=enhanced_df['target'], cmap='viridis', alpha=0.7, s=50)
    axes[1, 1].set_title('Cubic Features: feature1³ vs feature2³\n(Even stronger amplification effects)', 
                        fontsize=12, pad=15)
    axes[1, 1].set_xlabel('feature1³')
    axes[1, 1].set_ylabel('feature2³')
    axes[1, 1].grid(True, alpha=0.3)
    
    # Add a colorbar to explain the class colors
    plt.colorbar(axes[0, 0].collections[0], ax=axes, label='Class (0=Purple, 1=Yellow)')
    
    plt.tight_layout()
    plt.savefig('polynomial_features_visualization.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved visualization as 'polynomial_features_visualization.png'")
    plt.show()
    
    '''
    What to look for in these plots:
    
    🎯 Class Separation: 
    - Original: Classes follow curved moons shape (hard to separate with a line)
    - Squared: Distance amplification may spread classes further apart
    - Interaction: New dimension might reveal linear separability
    - Cubic: Even stronger amplification, but watch for outliers
    
    📈 Distribution Changes:
    - Polynomial features change the scale (squared values are larger)
    - Interactions create new relationships between original features  
    - Higher orders can create extreme values (need normalization?)
    
    🔍 Decision Boundary Insights:
    - Original: Needs curved boundary (SVM with RBF, or neural network)
    - Enhanced: Might allow linear classifier to work in transformed space
    - This is the core idea behind kernel methods!
    
    ⚠️ Potential Issues:
    - Outliers become more extreme with higher powers
    - Feature scaling becomes crucial
    - Risk of overfitting with too many features
    '''

# Visualization of features
print("\n" + "="*60)
print("CREATING VISUALIZATIONS")
print("="*60)
visualize_features(df, enhanced_df)

# TODO: Analyze the correlation of features with the target
def analyze_feature_importance(enhanced_df):
    """
    Calculate and display correlation of features with target.
    
    Correlation analysis helps us understand which transformed features have 
    the strongest linear relationship with our target variable.
    """
    print("🔍 Starting correlation analysis...")
    print("   Calculating Pearson correlation coefficients for all features...")
    
    # 1. Calculate correlation of all features with target
    correlations = enhanced_df.corr()['target'].drop('target')  # Remove self-correlation
    
    # 2. Sort correlations in descending order by absolute value
    sorted_correlations = correlations.abs().sort_values(ascending=False)
    
    print(f"   ✅ Analyzed {len(correlations)} features")
    
    # 3. Display the top features
    print("\n📊 Feature Correlations with Target (sorted by absolute value):")
    print("-" * 70)
    print(f"{'Feature Name':<30} {'Correlation':<12} {'Absolute':<10} {'Strength'}")
    print("-" * 70)
    
    for feature, corr_abs in sorted_correlations.items():
        actual_corr = correlations[feature]
        # Categorize correlation strength
        if corr_abs >= 0.7:
            strength = "Strong 💪"
        elif corr_abs >= 0.4:
            strength = "Moderate 📊"
        elif corr_abs >= 0.2:
            strength = "Weak 📉"
        else:
            strength = "Very Weak 🤏"
            
        direction = "↗️" if actual_corr > 0 else "↘️"
        print(f"{feature:<30} {actual_corr:>8.4f} {direction}   {corr_abs:>6.4f}     {strength}")
    
    '''
    Understanding Correlation Values:
    
    📈 Correlation Range: -1.0 to +1.0
    - +1.0 = Perfect positive correlation (as X increases, Y increases)
    - -1.0 = Perfect negative correlation (as X increases, Y decreases)  
    -  0.0 = No linear correlation
    
    🎯 Interpretation Guidelines:
    - |r| > 0.7  = Strong correlation (feature is highly predictive)
    - |r| > 0.4  = Moderate correlation (useful feature)
    - |r| > 0.2  = Weak correlation (might help in combination)
    - |r| < 0.2  = Very weak (might be noise or non-linear relationship)
    
    ⚠️ Important Caveats:
    - Correlation ≠ Causation (classic warning!)
    - Only measures LINEAR relationships
    - Non-linear relationships might show low correlation but still be useful
    - Feature combinations might be powerful even if individual correlations are low
    '''
    
    # Visualize top correlations with enhanced styling
    print("\n🎨 Creating correlation visualization...")
    
    plt.figure(figsize=(14, 8))
    top_features = sorted_correlations.head(10)  # Top 10 features for better visibility
    top_actual_corr = [correlations[feature] for feature in top_features.index]
    
    # Create more sophisticated bar plot
    bars = plt.bar(range(len(top_features)), top_actual_corr, alpha=0.8, edgecolor='black', linewidth=0.8)
    
    # Enhanced styling
    plt.xticks(range(len(top_features)), top_features.index, rotation=45, ha='right', fontsize=10)
    plt.ylabel('Correlation with Target', fontsize=12, fontweight='bold')
    plt.title('Top 10 Features by Correlation Strength with Target\n(Green=Positive, Red=Negative)', 
             fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Enhanced color coding with correlation strength
    for i, bar in enumerate(bars):
        corr_val = top_actual_corr[i]
        corr_abs = abs(corr_val)
        
        if corr_val >= 0:
            # Positive correlation: varying shades of green
            if corr_abs >= 0.6:
                bar.set_color('#006400')  # Dark green for strong positive
            elif corr_abs >= 0.3:
                bar.set_color('#32CD32')  # Lime green for moderate positive
            else:
                bar.set_color('#90EE90')  # Light green for weak positive
        else:
            # Negative correlation: varying shades of red
            if corr_abs >= 0.6:
                bar.set_color('#8B0000')  # Dark red for strong negative
            elif corr_abs >= 0.3:
                bar.set_color('#DC143C')  # Crimson for moderate negative
            else:
                bar.set_color('#FFB6C1')  # Light pink for weak negative
        
        # Add value labels on bars
        plt.text(i, corr_val + (0.02 if corr_val >= 0 else -0.05), 
                f'{corr_val:.3f}', ha='center', va='bottom' if corr_val >= 0 else 'top',
                fontweight='bold', fontsize=9)
    
    # Add horizontal reference lines
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)
    plt.axhline(y=0.5, color='green', linestyle='--', alpha=0.5, label='Moderate Positive')
    plt.axhline(y=-0.5, color='red', linestyle='--', alpha=0.5, label='Moderate Negative')
    
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('feature_correlations.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved correlation plot as 'feature_correlations.png'")
    plt.show()
    
    # Summary insights
    strongest_feature = sorted_correlations.index[0]
    strongest_corr = correlations[strongest_feature]
    print(f"\n🏆 KEY INSIGHTS:")
    print(f"   • Strongest predictor: {strongest_feature}")
    print(f"   • Correlation strength: {strongest_corr:.4f}")
    print(f"   • Total features analyzed: {len(correlations)}")
    print(f"   • Features with |r| > 0.3: {sum(sorted_correlations > 0.3)}")
    
    return sorted_correlations

# Feature importance analysis
print("\n" + "="*60)
print("ANALYZING FEATURE IMPORTANCE")
print("="*60)
correlations = analyze_feature_importance(enhanced_df)

# TODO: Create one domain-specific feature of your own design
def create_custom_feature(dataframe):
    """
    Create domain-specific custom features that might be relevant for this dataset.
    
    This function demonstrates creative feature engineering based on understanding
    the geometric properties of the moons dataset.
    
    Args:
        dataframe: The input pandas DataFrame
        
    Returns:
        DataFrame with added custom features
    """
    print("🎨 Creating custom domain-specific features...")
    print("   Applying geometric and mathematical transformations...")
    
    df_custom = dataframe.copy()
    
    # Custom feature 1: Distance from origin (Euclidean distance)
    print("\n   🔹 Feature 1: Radial Distance")
    df_custom['distance_from_origin'] = np.sqrt(df_custom['feature1']**2 + df_custom['feature2']**2)
    '''
    Why distance from origin?
    
    🎯 Geometric Intuition: 
    - Converts Cartesian (x,y) to polar coordinates (r,θ)
    - Distance = √(x² + y²) captures how far each point is from center
    - Useful for data with circular/radial patterns
    
    🌙 Moons Dataset Application:
    - Each "moon" might have different distance distributions
    - One moon might be closer to origin than the other
    - Creates a feature that ignores direction, focuses on magnitude
    
    📊 Mathematical Properties:
    - Always positive (≥ 0)
    - Scale-invariant transformation
    - Reduces 2D information to 1D (dimensionality reduction)
    
    🔍 When to use:
    - Circular/radial decision boundaries
    - When orientation matters less than magnitude
    - Anomaly detection (outliers have large distances)
    '''
    
    # Custom feature 2: Angle/direction from origin
    print("   🔹 Feature 2: Angular Direction")
    df_custom['angle_from_origin'] = np.arctan2(df_custom['feature2'], df_custom['feature1'])
    '''
    Why angle from origin?
    
    🎯 Geometric Intuition:
    - Complements distance: now we have full polar coordinates (r,θ)
    - arctan2(y,x) gives angle in radians [-π, π]
    - Captures directional information, ignoring magnitude
    
    🌙 Moons Dataset Application:
    - Moons are oriented in different angular regions
    - Might separate classes based on angular sectors
    - Could reveal curved boundaries as angular patterns
    
    📊 Mathematical Properties:
    - Range: [-π, π] radians (≈ [-3.14, 3.14])
    - Periodic: θ and θ+2π represent same direction
    - Discontinuity at π/-π boundary (feature engineering gotcha!)
    
    🔍 When to use:
    - Rotational patterns in data
    - Time series with cyclical components
    - Image data with rotational invariance needs
    '''
    
    # Custom feature 3: Sum and difference of features  
    print("   🔹 Feature 3 & 4: Linear Combinations")
    df_custom['feature_sum'] = df_custom['feature1'] + df_custom['feature2']
    df_custom['feature_diff'] = df_custom['feature1'] - df_custom['feature2']
    '''
    Why sum and difference?
    
    🎯 Geometric Intuition:
    - Sum: x₁ + x₂ creates diagonal axis (slope = 1)
    - Difference: x₁ - x₂ creates orthogonal diagonal (slope = -1)
    - Rotates coordinate system by 45°
    
    🌙 Moons Dataset Application:
    - Might align better with the natural "tilt" of the moons
    - Linear transformation that could simplify curved boundaries
    - Creates new axes where classes might be more separable
    
    📊 Mathematical Properties:
    - Linear combinations preserve linearity
    - No information loss (invertible transformation)
    - Changes orientation of feature space
    
    🔍 When to use:
    - Data aligned along diagonal axes
    - Principal Component Analysis (PCA) applications
    - When original axes don't align with natural data structure
    '''
    
    # Custom feature 4: Asymmetric interaction (feature1² × feature2)
    print("   🔹 Feature 5: Asymmetric Polynomial Interaction")
    df_custom['asymmetric_interaction'] = df_custom['feature1']**2 * df_custom['feature2']
    '''
    Why asymmetric interaction?
    
    🎯 Mathematical Intuition:
    - Goes beyond simple x₁ × x₂ interaction
    - x₁² × x₂ creates non-symmetric relationship
    - One feature has quadratic influence, other linear
    
    🌙 Moons Dataset Application:
    - Captures situations where feature1's effect depends on feature2
    - But the dependence is quadratic in feature1
    - Might model curved interactions between the moons
    
    📊 Mathematical Properties:
    - Degree 3 polynomial feature
    - Non-symmetric: f(x₁,x₂) ≠ f(x₂,x₁)
    - Can capture complex curved relationships
    
    🔍 When to use:
    - Asymmetric relationships between features
    - Physics: Force depends on velocity² × mass
    - Economics: Diminishing returns scenarios
    '''
    
    # Custom feature 5: Normalized radial coordinate
    print("   🔹 Feature 6: Normalized Radial Position")
    max_distance = df_custom['distance_from_origin'].max()
    df_custom['normalized_distance'] = df_custom['distance_from_origin'] / max_distance
    '''
    Why normalized distance?
    
    🎯 Practical Benefit:
    - Scales distance to [0,1] range
    - Prevents distance from dominating other features
    - Easier for algorithms to handle
    
    🔍 Feature Engineering Best Practice:
    - Always consider feature scaling
    - Different features should have comparable ranges
    - Helps with gradient-based algorithms (neural networks, SVM)
    '''
    
    # Custom feature 6: Quadrant indicator (categorical → numerical)
    print("   🔹 Feature 7: Quadrant Encoding")
    df_custom['quadrant'] = (
        (df_custom['feature1'] >= 0).astype(int) * 2 + 
        (df_custom['feature2'] >= 0).astype(int)
    )
    '''
    Quadrant encoding explanation:
    - Quadrant 0: x < 0, y < 0 (bottom-left)
    - Quadrant 1: x < 0, y ≥ 0 (top-left)  
    - Quadrant 2: x ≥ 0, y < 0 (bottom-right)
    - Quadrant 3: x ≥ 0, y ≥ 0 (top-right)
    
    This creates a categorical feature that might help separate
    moons that occupy different quadrants of the coordinate space.
    '''
    
    print("\n✅ Custom features summary:")
    print("   1. distance_from_origin: √(feature1² + feature2²) - radial distance")
    print("   2. angle_from_origin: arctan2(feature2, feature1) - angular direction") 
    print("   3. feature_sum: feature1 + feature2 - diagonal axis")
    print("   4. feature_diff: feature1 - feature2 - orthogonal diagonal")
    print("   5. asymmetric_interaction: feature1² × feature2 - complex interaction")
    print("   6. normalized_distance: distance/max_distance - scaled [0,1]")
    print("   7. quadrant: categorical position encoding [0,1,2,3]")
    
    # Show statistics for new features
    print(f"\n📊 New feature statistics:")
    new_features = ['distance_from_origin', 'angle_from_origin', 'feature_sum', 
                   'feature_diff', 'asymmetric_interaction', 'normalized_distance', 'quadrant']
    
    for feature in new_features:
        mean_val = df_custom[feature].mean()
        std_val = df_custom[feature].std()
        min_val = df_custom[feature].min()
        max_val = df_custom[feature].max()
        print(f"   {feature:25s}: μ={mean_val:7.3f}, σ={std_val:6.3f}, range=[{min_val:6.3f}, {max_val:6.3f}]")
    
    '''
    🎓 Feature Engineering Lessons:
    
    ✅ Domain Knowledge Matters:
    - Understanding your data's geometry helps create meaningful features
    - Moons → polar coordinates make sense
    - Time series → seasonal features make sense
    - Images → edge/texture features make sense
    
    ✅ Transformation Types:
    - Geometric: distance, angle, rotation
    - Mathematical: polynomials, interactions, logs
    - Statistical: normalization, standardization
    - Categorical: binning, encoding
    
    ✅ Feature Engineering Process:
    1. Understand the problem domain
    2. Visualize the data
    3. Hypothesize what patterns might exist
    4. Create features to capture those patterns
    5. Test and validate feature effectiveness
    
    ⚠️ Common Pitfalls:
    - Creating too many features (curse of dimensionality)
    - Features that leak information from the future
    - Features that are too correlated with existing ones
    - Not scaling features appropriately
    '''
    
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