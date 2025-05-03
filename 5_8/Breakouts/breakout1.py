# Load your cleaned weather dataset from yesterday's session
# Create at least three different types of plots:
# A line plot showing temperature over time
# A scatter plot showing the relationship between temperature and humidity
# A histogram or box plot showing the distribution of a weather variable
# Apply appropriate customization to each plot:
# Meaningful titles and axis labels
# Custom colors, markers, and line styles
# Grid lines and legends as needed
# Save at least one plot as a PNG file


cleaned_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # All in °F (converted 32°C to 89.6°F)
    'humidity': [65, 70, 68, 67, 66],  # All as percentages
    'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # All in mm (converted inches to mm)
}
