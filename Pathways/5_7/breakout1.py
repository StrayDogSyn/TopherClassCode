# Instructions:
# Load the provided weather dataset with artificially introduced missing values
# Identify the extent and pattern of missing values
# Apply at least three different strategies for handling the missing values
# Compare the results of different approaches
# Recommend the best approach for this specific dataset and explain why

data = {
    'date': pd.date_range('2023-02-01', periods=7),
    'temperature': [29.5, np.nan, 30.3, 28.8, np.nan, 29.1, 30.7],
    'humidity': [75, 72, np.nan, 74, 71, np.nan, 73],
    'precipitation': [0.0, 0.2, 0.0, np.nan, 0.4, 0.0, 0.2]
}
