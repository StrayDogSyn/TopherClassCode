# Box Plot Exercise

## Overview
# In this exercise, you'll create and interpret box plots to analyze temperature distributions across different months.

## Instructions
# 1. Use the provided mock temperature data in the starter code
# 2. Create box plots to visualize the temperature distribution by month
# 3. Customize your box plot with appropriate labels and title
# 4. Answer the questions below based on your visualization

## Questions
# 1. Which month shows the highest median temperature?
# 2. Which month has the widest temperature range (most variability)?
# 3. Are there any outliers visible in the data? If so, in which months?
# 4. Compare summer and winter months. How do their temperature distributions differ?
# 5. Based on the box plot, which month appears to have the most consistent temperatures?

## Starter Code
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('seasons.csv')

# Your code begins here:
# 1. Create a box plot of the temperature by month


# 2. Add appropriate labels and title


# 3. Display the plot
plt.savefig('plot.png')