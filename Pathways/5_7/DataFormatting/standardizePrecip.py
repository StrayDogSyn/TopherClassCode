import pandas as pd

# Sample data with inconsistent types
data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', '32°C', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}

# Function to standardize precipitation to millimeters
def standardize_precipitation(value):
    if pd.isna(value):
        return np.nan
    
    # Extract numeric value
    import re
    match = re.search(r'(\d+\.?\d*)', str(value))
    if not match:
        return np.nan
    
    amount = float(match.group(1))
    
    # Convert based on unit
    if 'in' in str(value) or '"' in str(value):
        return amount * 25.4  # Inches to mm
    else:
        return amount  # Assume mm if no unit or explicit mm

# Apply to precipitation column
messy_df['precipitation_mm'] = messy_df['precipitation'].apply(standardize_precipitation)
print("After standardizing precipitation to mm:")
print(messy_df)
