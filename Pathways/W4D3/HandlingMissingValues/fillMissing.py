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

# Fill with a specific value
filled_df = weather_df.fillna(0)
print("DataFrame after filling missing values with 0:")
print(filled_df)

# Fill with column mean
filled_df2 = weather_df.fillna(weather_df.mean())
print("\nDataFrame after filling missing values with column means:")
print(filled_df2)

# Fill with column median
filled_df3 = weather_df.fillna(weather_df.median())

# Fill with different values for different columns
fill_values = {'temperature': 32.0, 'humidity': 65, 'precipitation': 0.0}
filled_df4 = weather_df.fillna(value=fill_values)

