# Histogram Exercise

## Overview
# In this exercise, you'll create and interpret histograms to analyze daily temperature distributions across different seasons.

## Instructions
# 1. Use the provided mock temperature data in the starter code
# 2. Create histograms to visualize temperature distributions
# 3. Experiment with different bin sizes and normalization
# 4. Create separate histograms to compare seasonal distributions
# 5. Answer the questions below based on your visualizations

## Questions
# 1. What shape does the overall temperature distribution have? Is it normal, skewed, bimodal, or something else?
# 2. How does changing the number of bins affect your interpretation of the data?
# 3. How do the temperature distributions differ between winter and summer?
# 4. Which season shows the widest spread of temperatures?
# 5. Based on the histogram, what temperature range occurs most frequently in the dataset?

## Starter Code
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('seasons.csv')

# Your code begins here:
# 1. Create a histogram of overall temperature distribution


# 2. Create histograms with different bin sizes


# 3. Create histograms comparing seasonal distributions


# 4. Save your figures (use savefig instead of plt.show())
# plt.savefig('histogram_filename.png')