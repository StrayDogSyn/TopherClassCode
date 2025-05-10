"""
Time Series Forecasting Models for Weather Data
This example demonstrates various time series forecasting approaches for temperature prediction.
"""

import matplotlib
matplotlib.use('TkAgg') 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings

# Suppress warning messages for cleaner output
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Part 1: Generate or load sample weather data
# --------------------------------------------
print("Part 1: Preparing sample weather data")

# Generate sample data (in a classroom setting, you'd load actual data)
# Let's create a 2-year daily temperature dataset with seasonal patterns

# Create dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate seasonal temperature pattern with noise
def generate_temp(date):
    # Day of year from 0 to 1
    day_of_year = (date.dayofyear - 1) / 365
    # Seasonal cycle (coldest around January 15, warmest around July 15)
    seasonal_factor = -np.cos(2 * np.pi * day_of_year)
    # Base temperature + seasonal variation + random noise
    return 15 + 15 * seasonal_factor + np.random.normal(0, 3)

# Generate temperatures
temperatures = [generate_temp(date) for date in dates]

# Create DataFrame
df = pd.DataFrame({
    'date': dates,
    'temperature': temperatures
})

# Set date as index
df.set_index('date', inplace=True)

# Add some features that will be useful for machine learning approaches
df['month'] = df.index.month
df['day_of_year'] = df.index.dayofyear
# Create cyclical features to represent seasonality
df['day_sin'] = np.sin(2 * np.pi * df.index.dayofyear / 365)
df['day_cos'] = np.cos(2 * np.pi * df.index.dayofyear / 365)

# Add lag features (previous day, previous week)
df['temp_lag1'] = df['temperature'].shift(1)
df['temp_lag7'] = df['temperature'].shift(7)

# Create moving averages (past 3 days, past week)
df['temp_ma3'] = df['temperature'].rolling(window=3).mean()
df['temp_ma7'] = df['temperature'].rolling(window=7).mean()

# Drop missing values created by lag/rolling features
df = df.dropna()

# Split data into training and testing sets
train_end = '2023-06-30'  # First 1.5 years for training
test_start = '2023-07-01'  # Last 6 months for testing

train_data = df[:train_end]
test_data = df[test_start:]

print(f"Training data shape: {train_data.shape}, from {train_data.index.min()} to {train_data.index.max()}")
print(f"Testing data shape: {test_data.shape}, from {test_data.index.min()} to {test_data.index.max()}")

# Visualize the train-test split
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Testing data', color='red')
plt.axvline(x=train_data.index.max(), color='black', linestyle='--')
plt.title('Train-Test Split for Weather Forecasting')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 2: Classical Time Series Forecasting Methods
# ------------------------------------------------
print("\nPart 2: Classical Time Series Forecasting Methods")

# Method 1: Moving Average Forecast
# ---------------------------------
print("\n1. Moving Average Method")

# Function to generate moving average predictions
def moving_average_forecast(series, window=7):
    """Generate forecasts using simple moving average"""
    # Calculate the moving average on the training data
    rolling_mean = series.rolling(window=window).mean()
    
    # For forecasting, we need the last value of the rolling mean
    last_ma = rolling_mean.iloc[-1]
    
    # Create a Series of predictions filled with the last MA value
    forecast_index = test_data.index
    forecast = pd.Series(last_ma, index=forecast_index)
    
    return forecast

# Create forecasts using 7-day moving average
ma7_forecast = moving_average_forecast(train_data['temperature'], window=7)

# Plot the results
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Actual test data')
ma7_forecast.plot(label='7-day MA forecast', linestyle='--')
plt.title('Moving Average Forecast (7-day window)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Calculate error metrics
ma_mae = mean_absolute_error(test_data['temperature'], ma7_forecast)
ma_rmse = np.sqrt(mean_squared_error(test_data['temperature'], ma7_forecast))
print(f"Moving Average (7-day) - MAE: {ma_mae:.2f}°C, RMSE: {ma_rmse:.2f}°C")


# Method 2: Exponential Smoothing
# -------------------------------
print("\n2. Exponential Smoothing")

# Simple Exponential Smoothing (for data without trend or seasonality)
def simple_exp_smoothing(series, alpha=0.3):
    """Generate forecasts using simple exponential smoothing"""
    # Calculate the exponentially weighted moving average
    ewma = series.ewm(alpha=alpha).mean()
    
    # For forecasting, we need the last value
    last_ewma = ewma.iloc[-1]
    
    # Create a Series of predictions filled with the last EWMA value
    forecast_index = test_data.index
    forecast = pd.Series(last_ewma, index=forecast_index)
    
    return forecast

# Modified Holt-Winters function to handle insufficient data
def holt_winters(series):
    """Generate forecasts using Holt-Winters' method with appropriate settings"""
    try:
        # First attempt with default settings but shorter seasonal period
        model = ExponentialSmoothing(
            series,
            seasonal_periods=30,  # Monthly seasonality instead of annual
            trend='add',
            seasonal='add',
            use_boxcox=False
        )
        model_fit = model.fit()
        
    except ValueError:
        # Fallback if that fails: simple exponential smoothing with trend
        model = ExponentialSmoothing(
            series,
            trend='add',
            seasonal=None,  # Remove seasonality component
            use_boxcox=False
        )
        model_fit = model.fit()
        
        print("Note: Using simpler model without seasonality due to insufficient data")
    
    # Generate forecasts
    forecast = model_fit.forecast(steps=len(test_data))
    return forecast

# Create forecasts using simple exponential smoothing
ses_forecast = simple_exp_smoothing(train_data['temperature'], alpha=0.3)

# Create forecasts using Holt-Winters method
hw_forecast = holt_winters(train_data['temperature'])

# Plot the results
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Actual test data')
ses_forecast.plot(label='Simple Exp Smoothing', linestyle='--')
hw_forecast.plot(label='Holt-Winters (with trend)', linestyle='-.')
plt.title('Exponential Smoothing Forecasts')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Calculate error metrics
ses_mae = mean_absolute_error(test_data['temperature'], ses_forecast)
ses_rmse = np.sqrt(mean_squared_error(test_data['temperature'], ses_forecast))
hw_mae = mean_absolute_error(test_data['temperature'], hw_forecast)
hw_rmse = np.sqrt(mean_squared_error(test_data['temperature'], hw_forecast))

print(f"Simple Exp Smoothing - MAE: {ses_mae:.2f}°C, RMSE: {ses_rmse:.2f}°C")
print(f"Holt-Winters - MAE: {hw_mae:.2f}°C, RMSE: {hw_rmse:.2f}°C")


# Method 3: ARIMA Models
# ----------------------
print("\n3. ARIMA Models")

def arima_forecast(series):
    """Generate forecasts using ARIMA model with error handling"""
    try:
        # For simplicity, we'll use a basic ARIMA model
        # In practice, order should be determined using auto_arima or AIC/BIC
        model = ARIMA(series, order=(5, 1, 0))  # AR(5), differencing(1), MA(0)
        model_fit = model.fit()
        
        # Generate forecasts
        forecast = model_fit.forecast(steps=len(test_data))
        return forecast
    
    except Exception as e:
        print(f"ARIMA model failed with error: {e}")
        print("Using simple moving average as fallback")
        # Fallback to moving average
        forecast = moving_average_forecast(series, window=7)
        return forecast

# Create forecasts using ARIMA
arima_forecast = arima_forecast(train_data['temperature'])

# Plot the results
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Actual test data')
arima_forecast.plot(label='ARIMA forecast', linestyle='--')
plt.title('ARIMA Forecast')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Calculate error metrics
arima_mae = mean_absolute_error(test_data['temperature'], arima_forecast)
arima_rmse = np.sqrt(mean_squared_error(test_data['temperature'], arima_forecast))
print(f"ARIMA - MAE: {arima_mae:.2f}°C, RMSE: {arima_rmse:.2f}°C")


# Part 3: Machine Learning Approaches
# ----------------------------------
print("\nPart 3: Machine Learning Approaches")

# Prepare features and target
X_train = train_data[['month', 'day_sin', 'day_cos', 'temp_lag1', 'temp_lag7', 'temp_ma7']]
y_train = train_data['temperature']
X_test = test_data[['month', 'day_sin', 'day_cos', 'temp_lag1', 'temp_lag7', 'temp_ma7']]
y_test = test_data['temperature']

# Method 4: Linear Regression
# --------------------------
print("\n1. Linear Regression")

# Train the model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Make predictions
lr_preds = lr_model.predict(X_test)

# Plot the results
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Actual test data')
plt.plot(test_data.index, lr_preds, label='Linear Regression forecast', linestyle='--')
plt.title('Linear Regression Forecast')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Calculate error metrics
lr_mae = mean_absolute_error(y_test, lr_preds)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_preds))
print(f"Linear Regression - MAE: {lr_mae:.2f}°C, RMSE: {lr_rmse:.2f}°C")

# Examine feature importance (coefficients)
feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': lr_model.coef_
})
print("\nLinear Regression Coefficients:")
print(feature_importance.sort_values('Coefficient', ascending=False))


# Method 5: Random Forest
# ----------------------
print("\n2. Random Forest")

# Train the model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
rf_preds = rf_model.predict(X_test)

# Plot the results
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training data')
test_data['temperature'].plot(label='Actual test data')
plt.plot(test_data.index, rf_preds, label='Random Forest forecast', linestyle='--')
plt.title('Random Forest Forecast')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Calculate error metrics
rf_mae = mean_absolute_error(y_test, rf_preds)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))
print(f"Random Forest - MAE: {rf_mae:.2f}°C, RMSE: {rf_rmse:.2f}°C")

# Examine feature importance
feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': rf_model.feature_importances_
})
print("\nRandom Forest Feature Importance:")
print(feature_importance.sort_values('Importance', ascending=False))


# Part 4: Comparing Models
# ----------------------
print("\nPart 4: Comparing All Models")

# Create a DataFrame to compare all models
models = ['Moving Average', 'Simple Exp Smoothing', 'Holt-Winters', 'ARIMA', 
          'Linear Regression', 'Random Forest']
mae_values = [ma_mae, ses_mae, hw_mae, arima_mae, lr_mae, rf_mae]
rmse_values = [ma_rmse, ses_rmse, hw_rmse, arima_rmse, lr_rmse, rf_rmse]

comparison = pd.DataFrame({
    'Model': models,
    'MAE': mae_values,
    'RMSE': rmse_values
})

# Sort by MAE (lower is better)
comparison = comparison.sort_values('MAE')
print("\nModel Comparison:")
print(comparison)

# Visualize the comparison
plt.figure(figsize=(12, 10))

# Plot MAE comparison
plt.subplot(2, 1, 1)
plt.barh(comparison['Model'], comparison['MAE'])
plt.title('Mean Absolute Error (MAE) by Model')
plt.xlabel('MAE (°C)')
plt.grid(axis='x')

# Plot RMSE comparison
plt.subplot(2, 1, 2)
plt.barh(comparison['Model'], comparison['RMSE'])
plt.title('Root Mean Squared Error (RMSE) by Model')
plt.xlabel('RMSE (°C)')
plt.grid(axis='x')

plt.tight_layout()

# Plot all forecasts on one chart
plt.figure(figsize=(14, 8))
# Actual data
train_data['temperature'].plot(label='Training data', linewidth=2)
test_data['temperature'].plot(label='Actual test data', linewidth=2)

# Forecasts
plt.plot(test_data.index, ma7_forecast, label='Moving Average', linestyle='--', alpha=0.7)
plt.plot(test_data.index, ses_forecast, label='Simple Exp Smoothing', linestyle='--', alpha=0.7)
plt.plot(test_data.index, hw_forecast, label='Holt-Winters', linestyle='--', alpha=0.7)
plt.plot(test_data.index, arima_forecast, label='ARIMA', linestyle='--', alpha=0.7)
plt.plot(test_data.index, lr_preds, label='Linear Regression', linestyle='--', alpha=0.7)
plt.plot(test_data.index, rf_preds, label='Random Forest', linestyle='--', alpha=0.7)

plt.title('All Forecasting Models Comparison')
plt.ylabel('Temperature (°C)')
plt.legend(loc='upper left')
plt.grid(True)

print("\nIntroduction to Deep Learning for Time Series (Conceptual):")
print("1. Recurrent Neural Networks (RNNs) - Can model sequential dependencies")
print("2. Long Short-Term Memory (LSTM) - Better for capturing long-term patterns")
print("3. 1D Convolutional Neural Networks - Effective for feature extraction")
print("4. Transformer models - State-of-the-art for many time series tasks")
print("\nDeep learning models typically outperform traditional methods when:")
print("- You have large amounts of training data")
print("- The time series has complex, non-linear patterns")
print("- You're working with multivariate data (multiple input variables)")

# For interactive display in a real classroom:
# plt.show()