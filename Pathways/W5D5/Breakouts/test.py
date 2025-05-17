import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import seaborn as sns

# -----------------------------------------------------------------------------
# Exercise 1: Load and Prepare the Weather Data
# -----------------------------------------------------------------------------
# Time series data requires proper datetime formatting to enable time-based operations

# Load the dataset
weather_data = pd.read_csv('weather_data.csv')

# Convert the date column to datetime and set it as the index
# Discussion point: Why is datetime formatting critical for time series analysis?
weather_data['date'] = pd.to_datetime(weather_data['date'])
weather_data.set_index('date', inplace=True)

# Examine the data
print("Dataset overview:")
print(weather_data.head())
print("\nDataset information:")
print(weather_data.info())
print("\nBasic statistics:")
print(weather_data.describe())

# Check the date range
print(f"\nDate range: {weather_data.index.min()} to {weather_data.index.max()}")
print(f"Total days: {len(weather_data)}")