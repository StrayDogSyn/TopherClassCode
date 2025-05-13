import pandas as pd
import numpy as np

data = {
    'date': pd.date_range('2023-01-01', periods=7),
    'temperature': [32.5, 31.8, np.nan, 33.2, 32.7, np.nan, 34.1],
    'humidity': [65, np.nan, 70, 68, np.nan, 67, 66],
    'precipitation': [0.0, 0.2, 0.5, np.nan, 0.0, 0.1, 0.0]
}

weather_df = pd.DataFrame(data)
print(weather_df)

# Forward fill - use the last valid observation to fill gaps
ffill_df = weather_df.fillna(method='ffill')
print("DataFrame after forward fill:")
print(ffill_df)

# Backward fill - use the next valid observation to fill gaps
bfill_df = weather_df.fillna(method='bfill')
print("\nDataFrame after backward fill:")
print(bfill_df)
