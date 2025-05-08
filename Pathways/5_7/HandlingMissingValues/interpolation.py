import pandas as pd
import numpy as np
import scipy.interpolate


data = {
    'date': pd.date_range('2023-01-01', periods=7),
    'temperature': [32.5, 31.8, np.nan, 33.2, 32.7, np.nan, 34.1],
    'humidity': [65, np.nan, 70, 68, np.nan, 67, 66],
    'precipitation': [0.0, 0.2, 0.5, np.nan, 0.0, 0.1, 0.0]
}

weather_df = pd.DataFrame(data)

# Set 'date' as the index
weather_df.set_index('date', inplace=True)
print(weather_df)

# Linear interpolation
interpolated_df = weather_df.interpolate()
print("\nDataFrame after linear interpolation:")
print(interpolated_df)

# Cubic interpolation for curved patterns
interpolated_df2 = weather_df.interpolate(method='cubic')
print("\nDataFrame after cubic interpolation:")
print(interpolated_df2)

# Time-based interpolation, suitable for datetime indices
interpolated_df3 = weather_df.interpolate(method='time')
print("\nDataFrame after time-based interpolation:")
print(interpolated_df3)