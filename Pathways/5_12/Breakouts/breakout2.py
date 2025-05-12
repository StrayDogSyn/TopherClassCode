# Dispersion Analysis - Breakout Room Exercise
# ===========================================
#
# INSTRUCTIONS:
# In this exercise, you will analyze weather data variability using different
# measures of dispersion and detect potential weather anomalies.
# 
# Your tasks:
# 1. Calculate various dispersion measures (range, variance, standard deviation, IQR)
# 2. Identify and discuss months/seasons with high/low variability
# 3. Detect potential weather anomalies using IQR and Z-score methods
# 4. Create visualizations to represent your findings
# 5. Interpret your results and prepare to present them to the class
#
# Remember to consider:
#   - Which weather variables show the most/least variability
#   - How different seasons compare in terms of weather variability
#   - Which outlier detection method worked better for your data and why

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample monthly temperature data for a city (°C)
monthly_temps = {
    'January': [2.3, 1.5, 0.8, -5.2, 3.1, -7.8, 2.9, 1.7, 0.5, -2.1, 
                1.3, 2.5, 1.1, -0.9, 3.4, 2.2, 1.8, 0.3, -1.5, 4.2],
    'April': [15.2, 16.8, 14.5, 15.9, 17.2, 16.3, 15.7, 14.9, 16.1, 17.5, 
              15.3, 16.5, 14.7, 15.8, 16.9, 15.1, 16.2, 15.6, 14.3, 16.7],
    'July': [28.5, 29.1, 27.8, 30.2, 29.4, 31.5, 28.9, 29.7, 28.2, 29.9, 
             36.8, 28.7, 29.5, 27.9, 30.3, 29.2, 28.1, 29.8, 37.5, 29.6],
    'October': [18.1, 17.5, 19.2, 17.8, 16.9, 18.7, 17.3, 18.9, 16.5, 17.1, 
                18.5, 16.8, 17.6, 19.5, 18.3, 17.4, 16.2, 17.9, 18.6, 17.2]
}

# Sample precipitation data for the same months (mm)
monthly_precip = {
    'January': [35.2, 42.1, 0.0, 28.5, 15.3, 52.7, 0.0, 31.8, 45.2, 22.6, 
                39.4, 0.0, 18.7, 25.3, 48.9, 37.1, 0.0, 29.6, 33.5, 41.2],
    'April': [62.5, 58.2, 71.4, 0.0, 53.7, 47.8, 59.6, 0.0, 66.3, 49.5, 
              55.8, 61.7, 52.9, 0.0, 57.3, 63.4, 50.1, 68.9, 54.2, 0.0],
    'July': [10.2, 0.0, 5.7, 15.3, 0.0, 8.9, 12.5, 0.0, 7.6, 4.8, 
             82.5, 0.0, 6.3, 11.7, 0.0, 9.4, 7.1, 0.0, 95.8, 8.2],
    'October': [43.7, 39.5, 0.0, 46.2, 50.8, 0.0, 37.1, 44.6, 52.3, 0.0, 
                41.9, 47.5, 36.8, 0.0, 48.9, 53.4, 0.0, 40.2, 45.7, 38.3]
}

# TODO: Create a DataFrame for each dataset
# Example: temp_df = pd.DataFrame(monthly_temps)
# precipitation_df = pd.DataFrame(monthly_precip)


# TODO: Calculate basic dispersion measures for each month's temperature
# For each month, calculate:
# - Range
# - Variance
# - Standard deviation
# - Interquartile range (IQR)


# TODO: Create a summary table of all dispersion measures for temperature
# Format it to 2 decimal places for readability


# TODO: Calculate the same dispersion measures for precipitation data


# TODO: Create a summary table for precipitation


# TODO: Visualize the dispersion of temperature data
# Hint: Box plots are great for showing dispersion and potential outliers


# TODO: Visualize the dispersion of precipitation data
# Consider using both box plots and histograms


# TODO: Detect temperature outliers using the IQR method
# For each month, determine which temperatures are outliers
# Remember: Outliers are typically defined as values that fall below Q1 - 1.5*IQR 
# or above Q3 + 1.5*IQR


# TODO: Detect temperature outliers using the Z-score method
# For each month, calculate Z-scores and identify outliers
# Typically, values with |Z| > 3 are considered outliers


# TODO: Compare the outliers detected by each method
# Do both methods identify the same outliers? If not, why might that be?


# TODO: Based on your analysis, determine:
# 1. Which month shows the highest temperature variability and why?
# 2. Which month shows the highest precipitation variability and why?
# 3. Is there a relationship between the variability of temperature and precipitation?
# 4. Which outlier detection method seems more appropriate for this weather data?


# PRESENTATION PREPARATION:
# Be ready to share:
# 1. Your summary tables of dispersion measures
# 2. Your visualizations showing the dispersion of both variables
# 3. The outliers you detected and which method you think worked better
# 4. Your interpretation of seasonal weather variability