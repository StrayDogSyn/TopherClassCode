import pandas as pd

# Load the weather data
df = pd.read_csv('weather_data.csv')

# Convert temperature from Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9
df['temperature'] = (df['temperature'] - 32) * 5/9

# Round to 1 decimal place for cleaner data
df['temperature'] = df['temperature'].round(1)

# Save the updated data back to the CSV file
df.to_csv('weather_data.csv', index=False)

print("Temperature conversion complete!")
print("First few rows with Celsius temperatures:")
print(df.head())
print(f"\nTemperature range: {df['temperature'].min():.1f}°C to {df['temperature'].max():.1f}°C")
