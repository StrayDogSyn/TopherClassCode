import pandas as pd

# Sample data with inconsistent types
data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', '32°C', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}

messy_df = pd.DataFrame(data)
print("Original messy DataFrame:")
print(messy_df)
print("\nData types:")
print(messy_df.dtypes)

# Convert date column to datetime
messy_df['date'] = pd.to_datetime(messy_df['date'], errors='coerce')
print("After date conversion:")
print(messy_df)
