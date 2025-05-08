"""
Introduction to Derived Features
--------------------------------
This script demonstrates the concept of derived features and their importance
in data analysis and machine learning.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Generate a synthetic dataset
np.random.seed(42)
X, y = make_classification(n_samples=1000, n_features=3, n_informative=2, 
                          n_redundant=0, n_classes=2, random_state=42)

# Create a dataframe for easier manipulation
df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
df['target'] = y

print("Original Dataset:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# Example 1: Creating a ratio feature
df['ratio_1_2'] = df['feature1'] / (df['feature2'] + 1e-10)  # Adding small value to avoid division by zero

# Example 2: Creating a difference feature
df['diff_1_3'] = df['feature1'] - df['feature3']

# Example 3: Creating a statistical feature
df['mean_features'] = df[['feature1', 'feature2', 'feature3']].mean(axis=1)
df['max_features'] = df[['feature1', 'feature2', 'feature3']].max(axis=1)

print("\nDataset with Derived Features:")
print(df.head())

# Visualization to show the discriminative power of derived features
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original features
axes[0, 0].scatter(df['feature1'], df['feature2'], c=df['target'], cmap='viridis', alpha=0.6)
axes[0, 0].set_title('Original Features: feature1 vs feature2')
axes[0, 0].set_xlabel('feature1')
axes[0, 0].set_ylabel('feature2')

# Ratio feature vs original
axes[0, 1].scatter(df['ratio_1_2'], df['feature3'], c=df['target'], cmap='viridis', alpha=0.6)
axes[0, 1].set_title('Derived Feature: ratio_1_2 vs feature3')
axes[0, 1].set_xlabel('ratio_1_2')
axes[0, 1].set_ylabel('feature3')

# Difference feature vs original
axes[1, 0].scatter(df['diff_1_3'], df['feature2'], c=df['target'], cmap='viridis', alpha=0.6)
axes[1, 0].set_title('Derived Feature: diff_1_3 vs feature2')
axes[1, 0].set_xlabel('diff_1_3')
axes[1, 0].set_ylabel('feature2')

# Statistical features
axes[1, 1].scatter(df['mean_features'], df['max_features'], c=df['target'], cmap='viridis', alpha=0.6)
axes[1, 1].set_title('Derived Features: mean_features vs max_features')
axes[1, 1].set_xlabel('mean_features')
axes[1, 1].set_ylabel('max_features')

plt.tight_layout()
plt.savefig('derived_features_visualization.png')

# Example 4: Domain-specific feature - distance from origin (magnitude)
df['distance_from_origin'] = np.sqrt(df['feature1']**2 + df['feature2']**2 + df['feature3']**2)

# Let's check correlation with target
print("\nCorrelation with Target:")
correlations = df.corr()['target'].sort_values(ascending=False)
print(correlations)

# Save the resulting dataset
df.to_csv('dataset_with_derived_features.csv', index=False)
print("\nEnhanced dataset saved as 'dataset_with_derived_features.csv'")