"""
Categorical Feature Encoding
----------------------------
This script demonstrates various techniques for encoding categorical variables
for machine learning algorithms.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from category_encoders import BinaryEncoder, TargetEncoder
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Create a synthetic dataset with categorical features
n_samples = 1000

# Create categorical features
colors = ['red', 'blue', 'green', 'yellow', 'orange']
sizes = ['small', 'medium', 'large']
countries = ['USA', 'Canada', 'UK', 'France', 'Germany', 'Japan', 'China', 'India', 'Brazil', 'Australia']
ordered_ratings = ['poor', 'fair', 'good', 'excellent']

# Generate random categorical data
color_data = np.random.choice(colors, size=n_samples, p=[0.3, 0.3, 0.2, 0.1, 0.1])
size_data = np.random.choice(sizes, size=n_samples, p=[0.2, 0.5, 0.3])
country_data = np.random.choice(countries, size=n_samples)
rating_data = np.random.choice(ordered_ratings, size=n_samples, p=[0.1, 0.2, 0.4, 0.3])

# Create a numerical target variable (for target encoding example)
base_values = {'red': 10, 'blue': 20, 'green': 15, 'yellow': 5, 'orange': 25,
               'small': 5, 'medium': 15, 'large': 25,
               'poor': 5, 'fair': 10, 'good': 15, 'excellent': 20}

# Generate target variable with some noise
target = np.zeros(n_samples)
for i in range(n_samples):
    target[i] = base_values[color_data[i]] + base_values[size_data[i]] + base_values[rating_data[i]]
    # Add country effect (some countries have higher values)
    if country_data[i] in ['USA', 'Japan', 'Germany']:
        target[i] += 15
    # Add noise
    target[i] += np.random.normal(0, 10)

# Create DataFrame
df = pd.DataFrame({
    'color': color_data,
    'size': size_data,
    'country': country_data,
    'rating': rating_data,
    'target': target
})

print("Original Dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nCategorical Value Counts:")
for col in ['color', 'size', 'country', 'rating']:
    print(f"\n{col.capitalize()} value counts:")
    print(df[col].value_counts())

# 1. Label Encoding
# Good for binary categories or ordinal categories
label_encoder = LabelEncoder()
df['color_label'] = label_encoder.fit_transform(df['color'])
print("\n1. Label Encoding Results:")
print("Color mapping:", dict(zip(label_encoder.classes_, range(len(label_encoder.classes_)))))

# Reset label encoder for rating to get new mapping
rating_encoder = LabelEncoder()
df['rating_label'] = rating_encoder.fit_transform(df['rating'])
print("Rating mapping:", dict(zip(rating_encoder.classes_, range(len(rating_encoder.classes_)))))

# For properly ordered ordinal encoding, we need OrdinalEncoder with specified categories
ordinal_encoder = OrdinalEncoder(categories=[ordered_ratings])
df['rating_ordinal'] = ordinal_encoder.fit_transform(df[['rating']])

# 2. One-Hot Encoding
# Good for nominal categories with few levels
one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
color_one_hot = one_hot_encoder.fit_transform(df[['color']])

# Get the actual feature names from the encoder
one_hot_feature_names = one_hot_encoder.get_feature_names_out(['color'])
color_one_hot_df = pd.DataFrame(color_one_hot, columns=one_hot_feature_names)

# Using Pandas get_dummies for one-hot (often simpler)
size_one_hot_df = pd.get_dummies(df['size'], prefix='size', drop_first=True)

# Combine with original dataframe
df = pd.concat([df, color_one_hot_df, size_one_hot_df], axis=1)

print("\n2. One-Hot Encoding Results:")
print("One-hot feature names:", one_hot_feature_names)
print("First few rows with color one-hot encoded:")
print(df[['color'] + list(one_hot_feature_names)].head())

# 3. Binary Encoding
# Efficient for high-cardinality nominal features
binary_encoder = BinaryEncoder(cols=['country'])
country_binary = binary_encoder.fit_transform(df[['country']])
country_binary.columns = [f'country_bin_{i}' for i in range(len(country_binary.columns))]

# Combine with original dataframe
df = pd.concat([df, country_binary], axis=1)

print("\n3. Binary Encoding Results:")
print("Country binary encoded (first few rows):")
print(df[['country'] + list(country_binary.columns)].head())

# 4. Target Encoding
# Good for high-cardinality features with target correlation
target_encoder = TargetEncoder(cols=['country'])
df['country_target'] = target_encoder.fit_transform(df[['country']], df['target'])

print("\n4. Target Encoding Results:")
print("Country target encoded (showing mean target value per country):")
country_target_means = df.groupby('country')['target'].mean().sort_values(ascending=False)
print(country_target_means)
print("\nTarget-encoded values (first few rows):")
print(df[['country', 'country_target']].head())

# Visualize the different encoding methods
# 1. Compare original vs. encoded values
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Original categorical distribution
sns.countplot(x='color', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Original Color Distribution')
axes[0, 0].set_ylabel('Count')
axes[0, 0].tick_params(axis='x', rotation=45)

# Label encoded
sns.countplot(x='color_label', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Label Encoded Colors')
axes[0, 1].set_xlabel('Encoded Value')
axes[0, 1].set_ylabel('Count')

# One-hot encoded (visualized differently)
one_hot_sum = df[one_hot_feature_names].sum()
axes[1, 0].bar(one_hot_sum.index, one_hot_sum.values)
axes[1, 0].set_title('One-Hot Encoded Colors (Sum of Each Column)')
axes[1, 0].set_ylabel('Count')
axes[1, 0].tick_params(axis='x', rotation=45)

# Target encoding visualization
country_target_means = df.groupby('country')['target'].mean().sort_values()
axes[1, 1].barh(country_target_means.index, country_target_means.values)
axes[1, 1].set_title('Target Encoded Countries (Mean Target Value)')
axes[1, 1].set_xlabel('Mean Target Value')

plt.tight_layout()
plt.savefig('categorical_encoding_comparison.png')
plt.close()

# 2. Visualize relationship between encoded features and target
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Original categorical vs target
sns.boxplot(x='color', y='target', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Original Categories vs Target')
axes[0, 0].tick_params(axis='x', rotation=45)

# Label encoded vs target
sns.scatterplot(x='color_label', y='target', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Label Encoded vs Target')
axes[0, 1].set_xlabel('Color (Label Encoded)')

# Ordinal encoded vs target
sns.scatterplot(x='rating_ordinal', y='target', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Ordinal Encoded Rating vs Target')
axes[1, 0].set_xlabel('Rating (Ordinal Encoded)')

# Target encoded vs target
sns.scatterplot(x='country_target', y='target', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Target Encoded Country vs Target')
axes[1, 1].set_xlabel('Country (Target Encoded)')

plt.tight_layout()
plt.savefig('encoding_vs_target.png')
plt.close()

# Summary of encoding methods and their use cases
print("\nEncoding Methods Summary:")
print("1. Label Encoding:")
print("   - Assigns a unique integer to each category")
print("   - Best for: Binary categories or ordered categories")
print("   - Warning: Creates false ordinality for nominal categories")
print("\n2. One-Hot Encoding:")
print("   - Creates binary columns for each category")
print("   - Best for: Nominal categories with few levels")
print("   - Warning: Creates many features with high-cardinality variables")
print("\n3. Binary Encoding:")
print("   - Represents categories as binary digits")
print("   - Best for: High-cardinality nominal features")
print("   - Advantage: More memory-efficient than one-hot for high-cardinality")
print("\n4. Target Encoding:")
print("   - Replaces categories with mean target value")
print("   - Best for: High-cardinality features with target correlation")
print("   - Warning: Risk of overfitting; requires cross-validation")
print("\n5. Ordinal Encoding:")
print("   - Assigns ordered integers based on category order")
print("   - Best for: Categorical variables with clear ordering")

# Save the encoded dataset
df.to_csv('encoded_features_dataset.csv', index=False)
print("\nEncoded dataset saved as 'encoded_features_dataset.csv'")