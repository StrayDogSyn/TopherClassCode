# Instructions:
# Load your cleaned weather dataset from yesterday's session
# Create a multi-panel visualization with at least three subplots that together tell a meaningful story about your data
# Use different plot types for different aspects of the data:
# Consider time series, distributions, relationships between variables
# Use appropriate plot types for each (line, scatter, bar, histogram, etc.)


cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm
}