# Example 2: Comparing Different Bin Sizes and Normalization
# This example shows how bin size affects histogram interpretation and demonstrates normalization

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data - simulate exam scores (slightly right-skewed)
# We'll create a mixture of two normal distributions to get a more interesting shape
scores_group1 = np.random.normal(70, 10, 70)   # 70 students scoring around 70%
scores_group2 = np.random.normal(85, 5, 30)    # 30 students scoring around 85%
scores = np.concatenate([scores_group1, scores_group2])

# Clip scores to be between 0 and 100
scores = np.clip(scores, 0, 100)

# Create a figure with 2 rows and 2 columns of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Different numbers of bins to compare
bins_options = [5, 10, 20, 50]

# Create histograms with different bin sizes
for i, bins in enumerate(bins_options):
    axes[i].hist(scores, bins=bins, edgecolor='black', alpha=0.7)
    axes[i].set_title(f'Histogram with {bins} bins')
    axes[i].set_xlabel('Exam Score')
    axes[i].set_ylabel('Frequency')
    axes[i].grid(True, linestyle='--', alpha=0.5)

# Add an overall title
fig.suptitle('Effect of Bin Size on Histogram Appearance', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Make room for the overall title

# Create a new figure for normalized histogram
plt.figure(figsize=(10, 6))

# Create a normalized histogram (probability density)
# density=True normalizes the histogram so the area equals 1
plt.hist(scores, bins=15, density=True, edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Exam Score')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram of Exam Scores')
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.savefig('plot.png')

# Important concepts:
# - Too few bins can hide important patterns
# - Too many bins can make the histogram noisy and harder to interpret
# - The "right" number of bins depends on your data and goals
# - Normalization (density=True) converts counts to probability density
# - Normalized histograms have total area = 1, useful for comparing distributions