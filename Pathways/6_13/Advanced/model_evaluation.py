"""
Topic 5: Model Evaluation for Weather Forecasting

This example demonstrates specific evaluation techniques for weather time series forecasting,
focusing on temperature prediction.

Key concepts covered:
1. Time series specific evaluation metrics (MAE, RMSE, MAPE)
2. Importance of forecast horizon (1-day vs 7-day ahead forecasts)
3. Visualizing forecast results
4. Evaluating forecast uncertainty
5. Common pitfalls in weather forecasting evaluation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings

# Configure matplotlib for Arch Linux
matplotlib.use('TkAgg')  # Lightweight backend for Arch Linux

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Part 1: Generate sample weather data for teaching
# ------------------------------------------------
print("Part 1: Preparing weather forecasting data")

# Create 1 year of daily temperature data with seasonal patterns
def generate_seasonal_data(days=365, base_temp=15, variation=15, noise=3):
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
        noise_val = np.random.normal(0, noise)
        # Calculate temperature
        temp = base_temp + variation * seasonal + noise_val
        temperatures.append(temp)
    
    # Create DataFrame
    weather_df = pd.DataFrame({
        'date': dates,
        'temperature': temperatures
    })
    
    # Set date as index
    weather_df.set_index('date', inplace=True)
    
    # Add useful features for forecasting
    weather_df['month'] = weather_df.index.month
    weather_df['day_of_year'] = weather_df.index.dayofyear
    
    # Add lag features (previous values)
    weather_df['temp_lag1'] = weather_df['temperature'].shift(1)  # Yesterday's temperature
    weather_df['temp_lag7'] = weather_df['temperature'].shift(7)  # Temperature 1 week ago
    
    # Add rolling features (moving averages)
    weather_df['temp_ma3'] = weather_df['temperature'].rolling(window=3).mean()  # 3-day average
    weather_df['temp_ma7'] = weather_df['temperature'].rolling(window=7).mean()  # Weekly average
    
    # Create seasonal features
    weather_df['day_sin'] = np.sin(2 * np.pi * weather_df.index.dayofyear / 365)
    weather_df['day_cos'] = np.cos(2 * np.pi * weather_df.index.dayofyear / 365)
    
    # Drop rows with NaN values
    weather_df = weather_df.dropna()
    
    return weather_df

# Generate a year of weather data
weather_data = generate_seasonal_data(days=365)

# Split into training and testing sets (9 months training, 3 months testing)
train_data = weather_data.iloc[:270]
test_data = weather_data.iloc[270:]

print(f"Training data: {len(train_data)} days ({train_data.index[0].strftime('%Y-%m-%d')} to {train_data.index[-1].strftime('%Y-%m-%d')})")
print(f"Testing data: {len(test_data)} days ({test_data.index[0].strftime('%Y-%m-%d')} to {test_data.index[-1].strftime('%Y-%m-%d')})")

# Visualize the data
plt.figure(figsize=(12, 6))
train_data['temperature'].plot(label='Training Data')
test_data['temperature'].plot(label='Testing Data', color='red')
plt.axvline(x=train_data.index[-1], color='black', linestyle='--')
plt.title('Temperature Time Series Train-Test Split')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)


# Part 2: Time Series Specific Evaluation Metrics
# ----------------------------------------------
print("\nPart 2: Time Series Specific Evaluation Metrics")

# Define evaluation metrics function
def calculate_metrics(actual, predicted, name="Model"):
    """Calculate common evaluation metrics for time series forecasting"""
    metrics = {
        'Model': name,
        'MAE': mean_absolute_error(actual, predicted),
        'RMSE': np.sqrt(mean_squared_error(actual, predicted)),
        'MAPE': np.mean(np.abs((actual - predicted) / np.abs(actual + 1e-10))) * 100,
        'R²': r2_score(actual, predicted)
    }
    return metrics

# Train a model for demonstration
# For this teaching example, we'll use a RandomForest
features = ['month', 'day_sin', 'day_cos', 'temp_lag1', 'temp_lag7', 'temp_ma7']
X_train = train_data[features]
y_train = train_data['temperature']
X_test = test_data[features]
y_test = test_data['temperature']

# Train the model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Get predictions
rf_preds = rf_model.predict(X_test)

# Create persistence forecast (tomorrow = today)
persistence_preds = test_data['temp_lag1'].values

# Create climatology forecast (historical average for this day of year)
# Group train data by day of year and calculate mean temperature
climatology = {}
for day in range(1, 366):
    # Get all temperatures for this day of year
    day_temps = train_data[train_data['day_of_year'] == day]['temperature']
    if len(day_temps) > 0:
        climatology[day] = day_temps.mean()
    else:
        # If day not in training data, use closest day
        closest_days = sorted(climatology.keys(), key=lambda x: abs(x - day))
        if closest_days:
            climatology[day] = climatology[closest_days[0]]
        else:
            climatology[day] = train_data['temperature'].mean()  # Fallback to overall mean

# Create climatology predictions
climatology_preds = np.array([climatology.get(day, train_data['temperature'].mean()) 
                              for day in test_data['day_of_year']])

# Calculate metrics for each model
rf_metrics = calculate_metrics(y_test, rf_preds, "Random Forest")
persistence_metrics = calculate_metrics(y_test, persistence_preds, "Persistence")
climatology_metrics = calculate_metrics(y_test, climatology_preds, "Climatology")

# Combine metrics into a DataFrame
all_metrics = pd.DataFrame([rf_metrics, persistence_metrics, climatology_metrics])
all_metrics = all_metrics.set_index('Model')

# Display metrics
print("\nEvaluation metrics comparison:")
print(all_metrics)

# Explain each metric
print("\nMetric explanations:")
print("1. MAE (Mean Absolute Error):")
print("   - Average of absolute differences between predictions and actual values")
print("   - In same units as the temperature (°C)")
print("   - Easier to interpret but doesn't penalize large errors heavily")

print("\n2. RMSE (Root Mean Squared Error):")
print("   - Square root of the average of squared differences")
print("   - In same units as the temperature (°C)")
print("   - Penalizes large errors more heavily than MAE")
print("   - More sensitive to outliers")

print("\n3. MAPE (Mean Absolute Percentage Error):")
print("   - Average of percentage errors")
print("   - Unit-free, making it useful for comparing different scales")
print("   - Can be problematic when actual values are close to zero")

print("\n4. R² (Coefficient of Determination):")
print("   - Proportion of variance explained by the model")
print("   - 1 indicates perfect predictions, 0 indicates predictions no better than mean")
print("   - Can be negative if predictions are worse than using the mean")


# Part 3: Importance of Forecast Horizon
# -------------------------------------
print("\nPart 3: Importance of Forecast Horizon")

# Function to generate forecasts for different horizons
def forecast_at_horizon(model, df, features, horizon):
    """Generate forecasts at a specific horizon"""
    results = []
    
    # We'll use a simple approach for teaching purposes
    # In production, you would use true walk-forward validation
    for i in range(len(df) - horizon):
        # Get features at current step
        X_current = df.iloc[i:i+1][features]
        
        # Make prediction
        pred = model.predict(X_current)[0]
        
        # Store actual value at horizon and prediction
        if i + horizon < len(df):
            actual = df.iloc[i + horizon]['temperature']
            
            results.append({
                'date': df.index[i + horizon],
                'actual': actual,
                'predicted': pred,
                'horizon': horizon
            })
    
    return pd.DataFrame(results)

# Generate forecasts at different horizons
horizons = [1, 3, 7, 14]
horizon_results = {}

for h in horizons:
    print(f"Generating {h}-day ahead forecasts...")
    horizon_results[h] = forecast_at_horizon(rf_model, test_data, features, h)
    
    # Calculate metrics for this horizon
    metrics = calculate_metrics(
        horizon_results[h]['actual'], 
        horizon_results[h]['predicted'],
        f"{h}-day ahead"
    )
    
    print(f"  MAE: {metrics['MAE']:.2f}°C, RMSE: {metrics['RMSE']:.2f}°C")

# Collect all horizon metrics
horizon_metrics = []
for h in horizons:
    metrics = calculate_metrics(
        horizon_results[h]['actual'], 
        horizon_results[h]['predicted'],
        f"{h}-day ahead"
    )
    horizon_metrics.append(metrics)

# Create DataFrame with metrics by horizon
horizon_df = pd.DataFrame(horizon_metrics).set_index('Model')

# Plot metrics by horizon
plt.figure(figsize=(10, 6))
plt.plot(horizons, horizon_df['MAE'], 'o-', label='MAE')
plt.plot(horizons, horizon_df['RMSE'], 's-', label='RMSE')
plt.title('Error Increases with Forecast Horizon')
plt.xlabel('Forecast Horizon (days)')
plt.ylabel('Error (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()

print("\nKey insights about forecast horizon:")
print("1. Errors typically increase with longer forecast horizons")
print("2. Always evaluate models at the specific horizon they'll be used for")
print("3. Comparing a 1-day model to a 7-day model is inappropriate")
print("4. Different models may perform best at different horizons")
print("5. Weather forecasts beyond 7-10 days are typically much less reliable")


# Part 4: Visualizing Forecast Results
# ----------------------------------
print("\nPart 4: Visualizing Forecast Results")

# We'll focus on 1-day and 7-day horizons for visualization
forecast_1d = horizon_results[1]
forecast_7d = horizon_results[7]

# Create a time series plot comparing actual vs predicted
plt.figure(figsize=(12, 6))
plt.plot(forecast_1d['date'], forecast_1d['actual'], label='Actual', color='black')
plt.plot(forecast_1d['date'], forecast_1d['predicted'], label='1-day Forecast', 
         linestyle='--', color='blue')
plt.plot(forecast_7d['date'], forecast_7d['predicted'], label='7-day Forecast', 
         linestyle=':', color='red')
plt.title('Actual vs Predicted Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Create scatter plots of actual vs predicted
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1-day forecast
axes[0].scatter(forecast_1d['actual'], forecast_1d['predicted'], alpha=0.5)
axes[0].plot([min(forecast_1d['actual']), max(forecast_1d['actual'])], 
         [min(forecast_1d['actual']), max(forecast_1d['actual'])], 
         'r--')
axes[0].set_title('1-day Forecast')
axes[0].set_xlabel('Actual Temperature (°C)')
axes[0].set_ylabel('Predicted Temperature (°C)')
axes[0].grid(True)

# 7-day forecast
axes[1].scatter(forecast_7d['actual'], forecast_7d['predicted'], alpha=0.5)
axes[1].plot([min(forecast_7d['actual']), max(forecast_7d['actual'])], 
         [min(forecast_7d['actual']), max(forecast_7d['actual'])], 
         'r--')
axes[1].set_title('7-day Forecast')
axes[1].set_xlabel('Actual Temperature (°C)')
axes[1].set_ylabel('Predicted Temperature (°C)')
axes[1].grid(True)

plt.tight_layout()

# Create error distribution plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Calculate errors
errors_1d = forecast_1d['predicted'] - forecast_1d['actual']
errors_7d = forecast_7d['predicted'] - forecast_7d['actual']

# 1-day error distribution
sns.histplot(errors_1d, kde=True, ax=axes[0])
axes[0].axvline(x=0, color='red', linestyle='--')
axes[0].set_title('1-day Forecast Errors')
axes[0].set_xlabel('Error (°C)')
axes[0].grid(True)

# 7-day error distribution
sns.histplot(errors_7d, kde=True, ax=axes[1])
axes[1].axvline(x=0, color='red', linestyle='--')
axes[1].set_title('7-day Forecast Errors')
axes[1].set_xlabel('Error (°C)')
axes[1].grid(True)

plt.tight_layout()

print("\nKey insights for visualizing forecasts:")
print("1. Time series plots show overall trends and pattern matching")
print("2. Scatter plots reveal systematic biases and error distribution")
print("3. Error histograms help understand the distribution of errors")
print("4. Visual assessment often reveals issues not captured by metrics alone")
print("5. Always compare visualizations across different forecast horizons")


# Part 5: Forecast Uncertainty
# --------------------------
print("\nPart 5: Evaluating Forecast Uncertainty")

# Function to generate prediction intervals using Random Forest
def rf_prediction_interval(model, X, percentile=90):
    """Get prediction intervals from a Random Forest model"""
    preds = []
    for tree in model.estimators_:
        preds.append(tree.predict(X))
    preds = np.column_stack(preds)
    
    lower = np.percentile(preds, (100 - percentile) / 2, axis=1)
    upper = np.percentile(preds, 100 - (100 - percentile) / 2, axis=1)
    mean = np.mean(preds, axis=1)
    
    return mean, lower, upper

# Generate predictions with uncertainty for the last 30 days
last_30_days = test_data.iloc[-30:]
X_last30 = last_30_days[features]
y_last30 = last_30_days['temperature']

# Get prediction intervals
mean_pred, lower_pred, upper_pred = rf_prediction_interval(rf_model, X_last30, percentile=90)

# Plot forecast with uncertainty
plt.figure(figsize=(12, 6))
plt.plot(last_30_days.index, y_last30, label='Actual', linewidth=2)
plt.plot(last_30_days.index, mean_pred, label='Forecast', linestyle='--', color='red')
plt.fill_between(last_30_days.index, lower_pred, upper_pred, color='red', alpha=0.2, 
                 label='90% Prediction Interval')
plt.title('Temperature Forecast with Uncertainty')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Calculate interval coverage (% of actual values within the interval)
coverage = np.mean((y_last30.values >= lower_pred) & (y_last30.values <= upper_pred)) * 100
interval_width = np.mean(upper_pred - lower_pred)

print(f"\nPrediction interval statistics:")
print(f"- Interval coverage: {coverage:.1f}% (target: 90%)")
print(f"- Average interval width: {interval_width:.2f}°C")

print("\nImportance of forecast uncertainty:")
print("1. Point forecasts alone are insufficient for decision-making")
print("2. Prediction intervals help understand the range of likely outcomes")
print("3. Uncertainty typically increases with forecast horizon")
print("4. Calibrated intervals should contain the actual value at the target frequency")
print("5. Weather forecasts should always include uncertainty information")


# Part 6: Common Pitfalls in Weather Forecasting Evaluation
# -------------------------------------------------------
print("\nPart 6: Common Pitfalls in Weather Forecasting Evaluation")

# Example of incorrect cross-validation for time series
incorrect_splits = [
    {'train_start': 90, 'train_end': 270, 'test_start': 0, 'test_end': 89}, # Future -> Past
    {'train_start': 0, 'train_end': 89, 'test_start': 180, 'test_end': 270}, # Gap in between
    {'train_start': 0, 'train_end': 270, 'test_start': 90, 'test_end': 180},  # Test in middle
]

correct_splits = [
    {'train_start': 0, 'train_end': 89, 'test_start': 90, 'test_end': 119},   # Correct
    {'train_start': 0, 'train_end': 119, 'test_start': 120, 'test_end': 149}, # Correct
    {'train_start': 0, 'train_end': 149, 'test_start': 150, 'test_end': 179}, # Correct
]

# Visualize proper vs improper cross-validation
plt.figure(figsize=(12, 8))

# Plot incorrect splits
for i, split in enumerate(incorrect_splits):
    plt.subplot(2, 3, i+1)
    plt.plot(range(split['train_start'], split['train_end']+1), [1]*len(range(split['train_start'], split['train_end']+1)), 'b-', linewidth=6, label='Train')
    plt.plot(range(split['test_start'], split['test_end']+1), [0.5]*len(range(split['test_start'], split['test_end']+1)), 'r-', linewidth=6, label='Test')
    plt.title(f'Incorrect Split {i+1}')
    plt.ylim(0, 1.5)
    plt.yticks([])
    if i == 0:
        plt.legend()

# Plot correct splits
for i, split in enumerate(correct_splits):
    plt.subplot(2, 3, i+4)
    plt.plot(range(split['train_start'], split['train_end']+1), [1]*len(range(split['train_start'], split['train_end']+1)), 'b-', linewidth=6, label='Train')
    plt.plot(range(split['test_start'], split['test_end']+1), [0.5]*len(range(split['test_start'], split['test_end']+1)), 'r-', linewidth=6, label='Test')
    plt.title(f'Correct Split {i+1}')
    plt.ylim(0, 1.5)
    plt.yticks([])
    if i == 0:
        plt.legend()

plt.tight_layout()

print("\nCommon Pitfalls in Weather Forecasting Evaluation:")
print("\n1. Data Leakage:")
print("   - Using future information in the training data")
print("   - Not respecting time order in cross-validation")
print("   - Using features that would not be available at prediction time")

print("\n2. Inappropriate Baselines:")
print("   - Not comparing against simple baselines like persistence or climatology")
print("   - Using overly complex models without justification")
print("   - Failing to justify model complexity with performance gains")

print("\n3. Ignoring Seasonality:")
print("   - Not accounting for seasonal patterns in evaluation")
print("   - Training on summer data and testing on winter data")
print("   - Not evaluating performance across different seasons")

print("\n4. Neglecting Forecast Horizon:")
print("   - Not clearly specifying the forecast horizon")
print("   - Using different horizons for training and evaluation")
print("   - Failing to evaluate at the operational forecast horizon")

print("\n5. Overlooking Uncertainty:")
print("   - Focusing only on point forecasts without uncertainty estimates")
print("   - Not evaluating the calibration of prediction intervals")
print("   - Failing to communicate uncertainty to end-users")

print("\nBest Practices for Weather Forecasting Evaluation:")
print("1. Always use walk-forward validation for time series")
print("2. Compare against appropriate baselines")
print("3. Evaluate across multiple forecast horizons")
print("4. Use domain-appropriate metrics")
print("5. Include and assess forecast uncertainty")
print("6. Consider the needs of the end-user when selecting metrics")
print("7. Evaluate across all seasons to account for seasonality")

# Show all plots
plt.show()