
import requests

# Set up our request
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

# Get API key from environment variable (or use a placeholder for demo)
api_key = 'eaf68ffb413d707283399af330d02c3f'
 
# Parameters for our request
parameters = {
    "q": "New York,US",         # The city we want weather for
    "appid": api_key,           # API key
    "units": "imperial"           # Get temperature 
    }

# Make the request
response = requests.get(weather_api_url, params=parameters)
print(response.json())
print(response.status_code)

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and display some data
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    
    # print(f"Current weather in {city}:")
    # print(f"Temperature: {temperature}°F")
    # print(f"Conditions: {weather}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)