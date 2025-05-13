import pandas as pd

# Sample temperature data with outliers
data = {
    'date': pd.date_range('2023-01-01', periods=10),
    'temperature': [32.5, 31.8, 33.2, 32.7, 120.0, 34.1, 31.9, -50.0, 33.5, 32.8]
}

outlier_df = pd.DataFrame(data)
print("DataFrame with outliers:")
print(outlier_df)

# Statistical method: Z-score
from scipy import stats
z_scores = stats.zscore(outlier_df['temperature'])
print("\nZ-scores:")
print(z_scores)

# Identify outliers using Z-score > 3
outliers_z = outlier_df[abs(z_scores) > 3]
print("\nOutliers identified by Z-score:")
print(outliers_z)

# IQR method
Q1 = outlier_df['temperature'].quantile(0.25)
Q3 = outlier_df['temperature'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nIQR boundaries: [{lower_bound}, {upper_bound}]")
outliers_iqr = outlier_df[(outlier_df['temperature'] < lower_bound) | 
                          (outlier_df['temperature'] > upper_bound)]
print("\nOutliers identified by IQR method:")
print(outliers_iqr)

# Handling outliers - Option 1: Remove them
cleaned_df = outlier_df[(outlier_df['temperature'] >= lower_bound) & 
                        (outlier_df['temperature'] <= upper_bound)]
print("\nDataFrame after removing outliers:")
print(cleaned_df)
