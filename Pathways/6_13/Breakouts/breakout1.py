"""
BREAKOUT ROOM 1: WEATHER DATA EXPLORATION

In this activity, you'll work in small groups to:
1. Load a weather dataset
2. Clean and preprocess the data
3. Create visualizations that reveal patterns
4. Identify and discuss key patterns found

Follow the instructions below and complete the code where indicated.
"""


# Part 1: Load the Dataset
# -----------------------
# We've provided a CSV file with historical weather data
# The file contains daily weather measurements for a city over one year

# TODO: Load the CSV file 'weather_data.csv' using pandas
# HINT: Use pd.read_csv()

# Your code here:
weather_data = None  # Replace with your code


# Print the first 5 rows to understand the data structure
print("First 5 rows of the dataset:")
# Your code here:


# Part 2: Data Inspection and Cleaning
# -----------------------------------
# Examine the dataset and handle any issues

# TODO: Check basic information about the dataset
# HINT: Use .info() and .describe() methods
# Your code here:


# TODO: Check for missing values in each column and handle them appropriately
# HINT: Use .isna().sum() to count missing values
# Your code here:


# TODO: Convert the 'date' column to datetime format
# HINT: Use pd.to_datetime()
# Your code here:


# TODO: Set the 'date' column as the index
# HINT: Use set_index() method
# Your code here:


# TODO: Check for and handle any outliers in the temperature column
# HINT: Use .clip() or another method to handle extreme values
# Your code here:


# Part 3: Feature Engineering
# --------------------------
# Add useful features for time series analysis

# TODO: Add columns for month and season
# HINT: Extract month from the index and create season using pd.cut()
# Your code here:


# Part 4: Data Visualization
# -------------------------
# Create at least THREE different visualizations that reveal patterns in the data

# TODO: VISUALIZATION 1 - Plot temperature over time
# Create a line plot showing the temperature trends
# HINT: Use plt.figure() and plt.plot() or weather_data['temperature'].plot()
# Your code here:


# TODO: VISUALIZATION 2 - Create a visualization that shows seasonal patterns
# This could be a box plot by month, a seasonal subseries plot, etc.
# Your code here:


# TODO: VISUALIZATION 3 - Create a visualization showing relationships between variables
# This could be a scatter plot, correlation heatmap, etc.
# Your code here:


# BONUS: Create an additional visualization that reveals something interesting
# Be creative! Try to find a pattern that might not be immediately obvious
# Your code here:


# Part 5: Pattern Identification
# ----------------------------
# Analyze your visualizations and identify patterns

"""
Write your observations below:

1. Daily patterns observed:


2. Seasonal trends identified:


3. Relationships between variables:


4. Any anomalies or unusual patterns:


5. How might these patterns affect weather forecasting?


"""

# Save your plots for presentation to the class
# plt.savefig('group_x_visualization.png')  # Replace 'x' with your group number

print("Completed the Weather Data Exploration activity!")