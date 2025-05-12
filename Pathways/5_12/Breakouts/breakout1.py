# Central Tendency Analysis - Breakout Room Exercise
# ================================================
#
# INSTRUCTIONS:
# In this exercise, you will analyze temperature data for different cities,
# calculate measures of central tendency, and interpret the results.
# 
# Your tasks:
# 1. Calculate the mean, median, and mode for each city's temperature data
# 2. Determine which measure is most appropriate for each city's data
# 3. Identify cities with unusual patterns or potential outliers
# 4. Prepare a brief explanation of your findings to share with the class
#
# Remember to consider:
#   - How the three measures compare for each city
#   - Which cities might have outliers or extreme values
#   - How you would communicate these findings to a non-technical audience

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Temperature data for different cities (°C)
city_temps = {
    'Phoenix': [28.5, 29.2, 30.1, 31.5, 42.8, 29.8, 30.2],
    'Seattle': [12.3, 13.1, 12.9, 13.2, 12.8, 11.9, 13.0],
    'Miami': [26.5, 26.8, 27.2, 45.1, 26.9, 27.3, 26.5],
    'Chicago': [18.2, 3.5, 16.8, 17.2, 16.5, 17.9, 18.1],
    'Denver': [15.6, 16.2, 2.3, 14.8, 15.9, 16.3, -3.7]
}

# TODO: Create a DataFrame from the city temperature data
# Hint: Use pd.DataFrame(city_temps)


# TODO: For each city, calculate:
#  - Mean temperature
#  - Median temperature
#  - Mode temperature
# Store these values in separate dictionaries or lists


# TODO: Create a table (DataFrame) that shows all three measures for each city
# This will help you compare the measures across cities


# TODO: Create visualizations to help understand the temperature distributions
# Suggestion: Use boxplots to visualize the data and identify potential outliers


# TODO: Based on your analysis, determine which measure of central tendency 
# is most appropriate for each city and explain why
# Think about: presence of outliers, data distribution, etc.


# TODO: For each city, write a brief interpretation of the results
# For example: "Phoenix shows a large difference between mean and median due to..."


# BONUS: If you have time, try to identify outliers numerically using the IQR method
# Hint: Outliers are often defined as values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR


# PRESENTATION PREPARATION:
# Be ready to share:
# 1. Your table of calculated measures
# 2. At least one visualization
# 3. Your interpretation of which measure is most appropriate for each city
# 4. How you would explain these findings to someone without statistical knowledge