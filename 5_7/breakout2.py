# Load the provided messy weather dataset with multiple data quality issues
# Address the following problems:
# Missing values (15% of the dataset)
# Inconsistent date formats
# Temperature readings in mixed units (°F and °C)
# Duplicate records
# Outliers in precipitation measurements
# Inconsistent column names
# Document each step of your cleaning process and the reasoning behind your decisions
# Produce a final, clean dataset suitable for analysis
# Calculate summary statistics before and after cleaning to demonstrate the impact

data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', '32°C', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}
