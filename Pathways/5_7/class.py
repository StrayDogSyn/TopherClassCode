import pandas as pd
import numpy as np

# Sample data with inconsistent types
data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', 'thirty-two', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}

messy_df = pd.DataFrame(data)
print("Original messy DataFrame:")
print(messy_df)

# Function to extract numeric values from temperature
def extract_numeric(value):
    if pd.isna(value):
        return np.nan
    elif isinstance(value, (int, float)):
        return float(value)
    else:
        # Extract numeric part using regex
        import re
        match = re.search(r'(\d+\.?\d*)', str(value))
        if match:
            return float(match.group(1))
        return np.nan

# Apply to temperature column
messy_df['temperature_numeric'] = messy_df['temperature'].apply(extract_numeric)
print("After extracting numeric temperature values:")
print(messy_df)