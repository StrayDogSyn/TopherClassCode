"First, let's see how to identify missing values in a DataFrame:"
import pandas as pd
import numpy as np

# Sample weather data with missing values
data = {
    'date': pd.date_range('2023-01-01', periods=7),
    'temperature': [32.5, 31.8, np.nan, 33.2, 32.7, np.nan, 34.1],
    'humidity': [65, np.nan, 70, 68, np.nan, 67, 66],
    'precipitation': [0.0, 0.2, 0.5, np.nan, 0.0, 0.1, 0.0]
}

weather_df = pd.DataFrame(data)
print(weather_df)

"Now let's check for missing values using different methods:"
# Check for missing values
print("Missing values per column:")
print(weather_df.isna().sum())

# Percentage of missing values per column
print("\nPercentage of missing values per column:")
print(weather_df.isna().mean() * 100)

# Visual representation of missing values
print("\nMissing value map:")
print(weather_df.isna())

# Total number of missing values
total_missing = weather_df.isna().sum().sum()
print(f"\nTotal missing values: {total_missing}")
