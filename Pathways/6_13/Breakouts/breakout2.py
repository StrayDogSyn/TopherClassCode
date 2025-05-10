"""
BREAKOUT ROOM 2: BUILDING SIMPLE WEATHER FORECASTING MODELS

In this activity, you'll work in groups to:
1. Use the preprocessed weather dataset
2. Implement simple forecasting models to predict temperature
3. Evaluate the models using appropriate time series metrics
4. Compare results and discuss model limitations

Follow the instructions below and complete the code where indicated.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # For Arch Linux compatibility 
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Part 1: Load and Prepare the Dataset
# -----------------------------------
# Let's use the preprocessed dataset from the previous session
# This time we'll focus on building forecasting models

# TODO: Load the processed weather dataset (weather_processed.csv)
# If you don't have the processed file, we'll create a synthetic dataset
# HINT: Use pd.read_csv() or the provided generate_data() function

def generate_data(days=365):
    """Generate synthetic temperature data with seasonal patterns"""
    # Create dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(days)]
    
    # Generate temperatures with seasonal pattern
    temperatures = []
    for date in dates:
        # Day of year normalized to [0,1]
        day_of_year = (date.timetuple().tm_yday - 1) / 365
        # Seasonal component (coldest in January, warmest in July)
        seasonal = -np.cos(2 * np.pi * day_of_year)
        # Add random noise
        noise_val = np.random.normal(0, 3)
        # Calculate temperature
        temp = 15 + 15 * seasonal + noise_val
        temperatures.append(temp)
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'temperature': temperatures
    })
    
    # Set date as index
    df.set_index('date', inplace=True)
    
    # Add features useful for forecasting
    df['month'] = df.index.month
    df['day_of_year'] = df.index.dayofyear
    df['day_sin'] = np.sin(2 * np.pi * df.index.dayofyear / 365)
    df['day_cos'] = np.cos(2 * np.pi * df.index.dayofyear / 365)
    df['temp_lag1'] = df['temperature'].shift(1)  # Yesterday's temperature
    df['temp_lag7'] = df['temperature'].shift(7)  # Temperature 1 week ago
    df['temp_ma7'] = df['temperature'].rolling(window=7).mean()  # 7-day average
    
    # Drop rows with NaN values
    df = df.dropna()
    
    return df

# Your code here:
try:
    # Try to load from file if it exists
    weather_data = pd.read_csv('weather_processed.csv', index_col='date', parse_dates=True)
    print("Loaded processed weather data from file.")
except FileNotFoundError:
    # Generate synthetic data if file doesn't exist
    weather_data = generate_data()
    print("Generated synthetic weather data.")

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(weather_data.head())

# Split into training and testing sets (80% train, 20% test)
train_size = int(len(weather_data) * 0.8)
train_data = weather_data.iloc[:train_size]
test_data = weather_data.iloc[train_size:]

# Basic info about the split
print(f"\nTraining data: {len(train_data)} days")
print(f"Testing data: {len(test_data)} days")


# Part 2: Implement a Baseline Model - Persistence Forecast
# --------------------------------------------------------
# The simplest forecasting method: tomorrow's temperature will be the same as today's

# TODO: Implement the persistence model (tomorrow = today)
# HINT: Use the lag1 feature that represents yesterday's temperature

# Your code here:



# TODO: Evaluate the persistence model
# HINT: Calculate MAE, RMSE, and MAPE between actual and predicted values

# Your code here:



# TODO: Visualize the persistence forecast
# HINT: Plot actual vs predicted temperatures

# Your code here:



# Part 3: Implement a Statistical Model - Moving Average
# -----------------------------------------------------
# A slightly more complex approach that uses an average of past values

# TODO: Implement a moving average model with a 7-day window
# HINT: Use the rolling() function with a window of 7 days

# Your code here:



# TODO: Evaluate the moving average model
# HINT: Calculate the same metrics as for the persistence model

# Your code here:



# TODO: Visualize the moving average forecast
# HINT: Plot the moving average forecast alongside the actual values and persistence forecast

# Your code here:



# Part 4: Implement a Machine Learning Model - Linear Regression
# ------------------------------------------------------------
# Now let's try a more complex approach using features to predict temperature

# TODO: Define features for the linear regression model
# HINT: Use day_sin, day_cos, and some lag features

# Your code here:



# TODO: Train a Linear Regression model
# HINT: Use sklearn's LinearRegression class, fit on training data

# Your code here:



# TODO: Make predictions on the test set
# HINT: Use model.predict() with the test features

# Your code here:



# TODO: Evaluate the linear regression model
# HINT: Calculate the same metrics as before

# Your code here:



# TODO: Examine the coefficients of the linear regression model
# HINT: Create a DataFrame with feature names and their coefficients

# Your code here:



# Part 5: Implement an Advanced Model - Random Forest
# -------------------------------------------------
# Let's try a more complex model that can capture non-linear relationships

# TODO: Train a Random Forest model
# HINT: Use RandomForestRegressor with n_estimators=100

# Your code here:



# TODO: Make predictions with the Random Forest model
# HINT: Use the same approach as with linear regression

# Your code here:



# TODO: Evaluate the Random Forest model
# HINT: Calculate the same metrics as before

# Your code here:



# TODO: Examine feature importance in the Random Forest model
# HINT: Access the feature_importances_ attribute

# Your code here:



# Part 6: Compare All Models
# ------------------------
# Now let's compare all the models we've built

# TODO: Create a DataFrame to compare all models
# HINT: Include each model and its evaluation metrics

# Your code here:



# TODO: Visualize the comparison
# HINT: Create a bar chart of MAE and RMSE values for each model

# Your code here:



# TODO: Plot all model predictions on a single chart
# HINT: Use different colors and line styles for each model

# Your code here:



# Part 7: Forecast for the Next Week
# --------------------------------
# Let's use our best model to forecast temperatures for the next 7 days

# TODO: Generate a 7-day forecast with the best model
# HINT: You'll need to implement a loop that uses each day's prediction for the next day

# Your code here:



# Part 8: Discussion Questions
# --------------------------
# Answer these questions with your group

"""
1. Which model performed the best according to the metrics? Why do you think that is?



2. What are the strengths and limitations of each forecasting approach?



3. How would you improve the best-performing model?



4. What additional features would be useful for temperature forecasting?



5. How would your approach change if you were forecasting:
   a) Precipitation instead of temperature?
   b) Hourly temperatures instead of daily?
   c) Temperatures 14 days ahead instead of 1 day ahead?



6. What other challenges might you face when working with real-world weather data?


"""

print("\nCompleted the Building Forecasting Models activity!")