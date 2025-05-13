import requests
import json

# Simulate a malformed response without the "temp" field
malformed_response = '{"name": "New York", "main": {"temp": "15"}, "weather": [{"description": "clear sky"}]}'
response = requests.Response()
response._content = malformed_response.encode('utf-8')
response.status_code = 200

# Check if request was successful
if response.status_code == 200:
    # Directly parse the JSON string
    weather_data = json.loads(response._content)

    # Extract and display some data with checks
    city = weather_data.get("name", "Unknown City")
    main_data = weather_data.get("main", {})
    temperature = main_data.get("temp", "Unknown Temperature")
    weather_list = weather_data.get("weather", [])
    weather = weather_list[0].get("description", "Unknown Conditions") if weather_list else "Unknown Conditions"

    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Conditions: {weather}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")