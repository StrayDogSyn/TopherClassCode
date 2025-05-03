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

# Drop rows with any missing values
clean_df = weather_df.dropna()
print("DataFrame after dropping rows with missing values:")
print(clean_df)

# Drop rows where all values are missing
clean_df2 = weather_df.dropna(how='all')
print("DataFrame after dropping rows where all values are missing:")
print(clean_df2)

# Drop rows where at least 2 values are non-null
clean_df3 = weather_df.dropna(thresh=2)
print("DataFrame after dropping rows where less than 2 values are non-null:")
print(clean_df3)

# Drop only if specific columns have missing values
clean_df4 = weather_df.dropna(subset=['temperature'])
print("DataFrame after dropping rows where 'temperature' is missing:")
print(clean_df4)