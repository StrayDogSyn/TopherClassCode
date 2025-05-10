"""
BREAKOUT ROOM 2: BUILDING SIMPLE WEATHER FORECASTING MODELS - ANSWER KEY

This file provides complete solutions for the weather forecasting model building activity.
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

# ANSWER: Load or generate weather data
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

# Define a function to calculate all evaluation metrics
def calculate_metrics(actual, predicted, model_name="Model"):
    """Calculate common evaluation metrics for forecasting"""
    metrics = {}
    metrics['Model'] = model_name
    
    # Mean Absolute Error
    metrics['MAE'] = mean_absolute_error(actual, predicted)
    
    # Root Mean Squared Error
    metrics['RMSE'] = np.sqrt(mean_squared_error(actual, predicted))
    
    # Mean Absolute Percentage Error
    # Avoid division by zero by adding a small constant
    metrics['MAPE'] = np.mean(np.abs((actual - predicted) / (np.abs(actual) + 1e-10))) * 100
    
    # R-squared (Coefficient of determination)
    metrics['R²'] = r2_score(actual, predicted)
    
    return metrics

# Split into training and testing sets (80% train, 20% test)
train_size = int(len(weather_data) * 0.8)
train_data = weather_data.iloc[:train_size]
test_data = weather_data.iloc[train_size:]

# Basic info about the split
print(f"\nTraining data: {len(train_data)} days")
print(f"Testing data: {len(test_data)} days")


# Part 2: Implement a Baseline Model - Persistence Forecast
# --------------------------------------------------------
# ANSWER: Implement persistence model
print("\nPart 2: Persistence Forecast Model")

# In persistence model, forecast = previous day's temperature
persistence_preds = test_data['temp_lag1'].values

# ANSWER: Evaluate persistence model
persistence_metrics = calculate_metrics(test_data['temperature'].values, 
                                       persistence_preds, 
                                       "Persistence")

print("\nPersistence Model Metrics:")
for metric, value in persistence_metrics.items():
    if metric != 'Model':
        print(f"{metric}: {value:.4f}")

# ANSWER: Visualize persistence forecast
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data['temperature'], label='Actual', color='black')
plt.plot(test_data.index, persistence_preds, label='Persistence Forecast', 
         linestyle='--', color='blue')
plt.title('Persistence Forecast (Tomorrow = Today)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 3: Implement a Statistical Model - Moving Average
# -----------------------------------------------------
# ANSWER: Implement moving average model
print("\nPart 3: Moving Average Model")

# We can use the pre-calculated 7-day moving average
# But we need to shift it by 1 day to avoid using future data
ma_forecast = train_data['temp_ma7'].iloc[-1]  # Last available MA from training data

# Create a series with the same value for all test days (for simplicity)
ma_preds = np.full(len(test_data), ma_forecast)

# ANSWER: Evaluate moving average model
ma_metrics = calculate_metrics(test_data['temperature'].values, 
                              ma_preds, 
                              "Moving Average")

print("\nMoving Average Model Metrics:")
for metric, value in ma_metrics.items():
    if metric != 'Model':
        print(f"{metric}: {value:.4f}")

# ANSWER: Visualize moving average forecast
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data['temperature'], label='Actual', color='black')
plt.plot(test_data.index, persistence_preds, label='Persistence Forecast', 
         linestyle='--', color='blue', alpha=0.5)
plt.plot(test_data.index, ma_preds, label='Moving Average Forecast', 
         linestyle='-.', color='green')
plt.title('Moving Average Forecast (7-day window)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 4: Implement a Machine Learning Model - Linear Regression
# ------------------------------------------------------------
# ANSWER: Define features for Linear Regression
print("\nPart 4: Linear Regression Model")

# Define features
features = ['month', 'day_sin', 'day_cos', 'temp_lag1', 'temp_lag7', 'temp_ma7']

# Prepare the training and testing data
X_train = train_data[features]
y_train = train_data['temperature']
X_test = test_data[features]
y_test = test_data['temperature']

# ANSWER: Train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# ANSWER: Make predictions
lr_preds = lr_model.predict(X_test)

# ANSWER: Evaluate the model
lr_metrics = calculate_metrics(y_test, lr_preds, "Linear Regression")

print("\nLinear Regression Model Metrics:")
for metric, value in lr_metrics.items():
    if metric != 'Model':
        print(f"{metric}: {value:.4f}")

# ANSWER: Examine coefficients
coefficients = pd.DataFrame({
    'Feature': features,
    'Coefficient': lr_model.coef_
}).sort_values('Coefficient', ascending=False)

print("\nLinear Regression Coefficients:")
print(coefficients)

# ANSWER: Visualize linear regression predictions
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data['temperature'], label='Actual', color='black')
plt.plot(test_data.index, lr_preds, label='Linear Regression Forecast', 
         linestyle='--', color='red')
plt.title('Linear Regression Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 5: Implement an Advanced Model - Random Forest
# -------------------------------------------------
# ANSWER: Train Random Forest model
print("\nPart 5: Random Forest Model")

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# ANSWER: Make predictions
rf_preds = rf_model.predict(X_test)

# ANSWER: Evaluate the model
rf_metrics = calculate_metrics(y_test, rf_preds, "Random Forest")

print("\nRandom Forest Model Metrics:")
for metric, value in rf_metrics.items():
    if metric != 'Model':
        print(f"{metric}: {value:.4f}")

# ANSWER: Examine feature importance
feature_importance = pd.DataFrame({
    'Feature': features,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nRandom Forest Feature Importance:")
print(feature_importance)

# ANSWER: Visualize Random Forest predictions
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data['temperature'], label='Actual', color='black')
plt.plot(test_data.index, rf_preds, label='Random Forest Forecast', 
         linestyle='--', color='purple')
plt.title('Random Forest Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 6: Compare All Models
# ------------------------
# ANSWER: Create comparison DataFrame
print("\nPart 6: Model Comparison")

models = ['Persistence', 'Moving Average', 'Linear Regression', 'Random Forest']
all_preds = [persistence_preds, ma_preds, lr_preds, rf_preds]
all_metrics = [persistence_metrics, ma_metrics, lr_metrics, rf_metrics]

# Combine all metrics into a DataFrame
comparison = pd.DataFrame(all_metrics).set_index('Model')

print("\nModel Comparison:")
print(comparison)

# ANSWER: Visualize metrics comparison
plt.figure(figsize=(12, 10))

# Plot MAE comparison
plt.subplot(2, 1, 1)
plt.barh(comparison.index, comparison['MAE'])
plt.title('Mean Absolute Error (MAE) by Model')
plt.xlabel('MAE (°C)')
plt.grid(axis='x')

# Plot RMSE comparison
plt.subplot(2, 1, 2)
plt.barh(comparison.index, comparison['RMSE'])
plt.title('Root Mean Squared Error (RMSE) by Model')
plt.xlabel('RMSE (°C)')
plt.grid(axis='x')

plt.tight_layout()

# ANSWER: Plot all models on one chart
plt.figure(figsize=(14, 8))
plt.plot(test_data.index, test_data['temperature'], label='Actual', color='black', linewidth=2)
plt.plot(test_data.index, persistence_preds, label='Persistence', linestyle='--', alpha=0.7)
plt.plot(test_data.index, ma_preds, label='Moving Average', linestyle='--', alpha=0.7)
plt.plot(test_data.index, lr_preds, label='Linear Regression', linestyle='--', alpha=0.7)
plt.plot(test_data.index, rf_preds, label='Random Forest', linestyle='--', alpha=0.7)

plt.title('All Forecasting Models Comparison')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()


# Part 7: Forecast for the Next Week
# --------------------------------
# ANSWER: Generate 7-day forecast with the best model (Random Forest)
print("\nPart 7: 7-Day Forecast")

# Identify the last day in our dataset
last_date = test_data.index[-1]
print(f"Last date in dataset: {last_date.strftime('%Y-%m-%d')}")

# Create a 7-day forecast
forecast_days = 7
forecast_dates = [last_date + timedelta(days=i+1) for i in range(forecast_days)]
forecasts = []

# Start with the last available data point
current_data = test_data.iloc[-1:].copy()

# For each day in the forecast period
for i in range(forecast_days):
    # Predict temperature for the current day
    prediction = rf_model.predict(current_data[features])[0]
    
    # Store the forecast
    forecasts.append({
        'date': forecast_dates[i],
        'temperature': prediction
    })
    
    # Create new row for the next day
    next_day = current_data.copy()
    next_day.index = [forecast_dates[i]]
    next_day['temperature'] = prediction
    next_day['month'] = forecast_dates[i].month
    next_day['day_of_year'] = forecast_dates[i].timetuple().tm_yday
    next_day['day_sin'] = np.sin(2 * np.pi * next_day['day_of_year'] / 365)
    next_day['day_cos'] = np.cos(2 * np.pi * next_day['day_of_year'] / 365)
    
    # Update lag features
    next_day['temp_lag1'] = current_data['temperature'].values[0]
    
    if i >= 6:  # Once we have 7 days, we can calculate a proper 7-day lag
        next_day['temp_lag7'] = forecasts[i-6]['temperature']
    else:  # Otherwise use the available historical data
        lag7_date = forecast_dates[i] - timedelta(days=7)
        if lag7_date in test_data.index:
            next_day['temp_lag7'] = test_data.loc[lag7_date, 'temperature']
        else:
            next_day['temp_lag7'] = next_day['temp_lag1']  # Fallback
    
    # Update moving average
    if i >= 6:  # Once we have 7 days, we can calculate a proper MA
        temps = [f['temperature'] for f in forecasts[max(0, i-6):i+1]]
        next_day['temp_ma7'] = sum(temps) / len(temps)
    else:  # Mix of historical and forecast data
        lookback = 7 - i - 1
        hist_dates = [last_date - timedelta(days=j) for j in range(lookback, 0, -1)]
        hist_temps = [test_data.loc[date, 'temperature'] for date in hist_dates if date in test_data.index]
        forecast_temps = [f['temperature'] for f in forecasts[:i+1]]
        all_temps = hist_temps + forecast_temps
        next_day['temp_ma7'] = sum(all_temps) / len(all_temps)
    
    # Use this as the current data for the next iteration
    current_data = next_day

# Create a DataFrame with the forecast
forecast_df = pd.DataFrame(forecasts)
forecast_df.set_index('date', inplace=True)

print("\n7-Day Forecast:")
print(forecast_df)

# Visualize the forecast
plt.figure(figsize=(12, 6))
plt.plot(test_data.index[-30:], test_data['temperature'][-30:], label='Historical Data', color='black')
plt.plot(forecast_df.index, forecast_df['temperature'], label='7-Day Forecast', 
         linestyle='--', marker='o', color='red')
plt.axvline(x=last_date, color='gray', linestyle=':')
plt.title('7-Day Temperature Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Part 8: Discussion Questions - SAMPLE ANSWERS
# --------------------------------------------
"""
1. Which model performed the best according to the metrics? Why do you think that is?

ANSWER: The Random Forest model typically performs best according to MAE, RMSE, and R² metrics.
This is because:
- It can capture non-linear relationships between features and temperature
- It's an ensemble method that combines multiple decision trees, reducing overfitting
- It can handle the complex seasonal and temporal patterns in weather data
- It automatically handles feature interactions, which are important in weather forecasting


2. What are the strengths and limitations of each forecasting approach?

ANSWER:
Persistence Model:
- Strengths: Simple, requires minimal data, easy to implement
- Limitations: Can't capture trends, poor for longer horizons, doesn't use seasonal patterns

Moving Average:
- Strengths: Reduces noise, captures short-term trends, still relatively simple
- Limitations: Lags behind actual changes, doesn't capture seasonality, limited predictive power

Linear Regression:
- Strengths: Captures relationships between features, handles seasonality, relatively interpretable
- Limitations: Can only model linear relationships, sensitive to outliers

Random Forest:
- Strengths: Captures non-linear relationships, handles interactions, robust to outliers
- Limitations: Less interpretable, requires more data, computationally intensive


3. How would you improve the best-performing model?

ANSWER:
- Add more features: humidity, pressure, wind speed, cloud cover
- Incorporate external data: nearby weather stations, satellite data
- Engineer better features: more sophisticated temporal features, harmonics for multiple cycles
- Optimize hyperparameters: tune number of trees, max depth, min samples per leaf
- Implement proper time series cross-validation: use walk-forward validation
- Ensemble with other models: combine with physics-based models or different statistical approaches
- Consider domain-specific validation: focus on extreme events prediction or specific seasons


4. What additional features would be useful for temperature forecasting?

ANSWER:
- Atmospheric conditions: pressure, humidity, cloud cover, precipitation
- Wind features: speed, direction, gust information
- Geographic context: elevation, proximity to water bodies, urban heat island effects
- Solar radiation: sunshine hours, solar intensity, day length
- Long-term climate oscillations: El Niño/La Niña indices, North Atlantic Oscillation
- Historical extremes: record highs/lows for the date
- Multiple lag features: temperatures from 2, 3, 14, 30 days ago
- Neighboring location temperatures: spatial correlations
- Rates of change: temperature gradients over time


5. How would your approach change if you were forecasting:
   a) Precipitation instead of temperature?
   b) Hourly temperatures instead of daily?
   c) Temperatures 14 days ahead instead of 1 day ahead?

ANSWER:
a) For precipitation:
   - Would need to handle zero-inflation (many days with no precipitation)
   - Might use a two-stage model: first predict occurrence, then amount
   - Would need different evaluation metrics (e.g., categorical metrics like precision/recall)
   - Might need to use more spatial features and radar/satellite data

b) For hourly temperatures:
   - Would need to incorporate diurnal cycles (day/night patterns)
   - Would require more granular time features (hour of day, hour sine/cosine)
   - Models would benefit from higher-frequency lag features
   - Data volume would increase significantly, requiring more efficient processing

c) For 14-day forecasts:
   - Would need to focus on longer-term climate patterns rather than short-term weather
   - Would likely have significantly higher uncertainty requiring proper communication
   - Would place more emphasis on seasonal and climatic features than recent observations
   - Would likely need ensemble approaches to better quantify uncertainty
   - Performance expectations would need to be adjusted (less accuracy expected)


6. What other challenges might you face when working with real-world weather data?

ANSWER:
- Data quality issues: missing values, sensor errors, inconsistent measurements
- Spatial heterogeneity: urban vs. rural, elevation differences, microclimate effects
- Extreme event prediction: rare events are harder to forecast but often most important
- Climate change impacts: historical patterns becoming less reliable predictors
- Computational resources: processing large spatiotemporal datasets efficiently
- Combining multiple data sources: integrating ground stations, satellites, radar data
- Handling regime changes: seasonal transitions, weather pattern shifts
- Evaluation challenges: what metrics matter most to end-users?
- Communication of uncertainty: how to present probabilistic forecasts effectively
- Temporal resolution: balancing granularity with computational constraints
"""

# Display all plots
plt.show()

print("Completed the Answer Key for Building Forecasting Models activity!")