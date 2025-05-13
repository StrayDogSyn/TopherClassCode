# File: weather_app.py
"""
Weather App - A well-organized example
This shows good organization practices for beginners
"""

import requests
import json
import os
from datetime import datetime

# Keep configuration separate and easy to find
# In a real app, you would load this from a separate file
# or environment variables for better security
API_KEY = "eaf68ffb413d707283399af330d02c3f"  # Replace with your actual API key
UNITS = "metric"  # Use metric units (Celsius)

# 1. KEEP RELATED FUNCTIONS TOGETHER
# API Functions - These functions handle getting data from the internet

def get_weather(city):
    """Get current weather for a city"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Could not get weather data. Status code: {response.status_code}")
        return None

# 2. EACH FUNCTION DOES ONE THING WELL

# Data Processing Functions - These functions handle transforming the data

def extract_weather_info(weather_data):
    """Extract important information from weather data"""
    if not weather_data:
        return None
        
    # Get the information we need from the data
    city_name = weather_data.get("name", "Unknown")
    temperature = weather_data.get("main", {}).get("temp", 0)
    humidity = weather_data.get("main", {}).get("humidity", 0)
    conditions = weather_data.get("weather", [{}])[0].get("description", "Unknown")
    
    # Return a simple dictionary with the information we care about
    return {
        "city": city_name,
        "temperature": temperature,
        "humidity": humidity,
        "conditions": conditions
    }

# File Operations Functions - These functions handle saving and loading data

def save_weather_data(weather_data, city):
    """Save weather data to a file"""
    if not weather_data:
        return False
        
    # Create a directory to store our data if it doesn't exist
    data_dir = "weather_data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Create a filename with the city name and current date/time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{data_dir}/{city}_{timestamp}.json"
    
    # Save the data to a file
    try:
        with open(filename, 'w') as file:
            json.dump(weather_data, file, indent=2)
        return filename
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

# Display Functions - These functions handle showing information to the user

def display_weather_report(weather_info):
    """Display a weather report to the user"""
    if not weather_info:
        print("No weather information available.")
        return
    
    # Format the data in a nice way for the user to read
    print("\n--- WEATHER REPORT ---")
    print(f"City: {weather_info['city']}")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Conditions: {weather_info['conditions']}")
    print("---------------------\n")

# 3. MAIN FUNCTION THAT COORDINATES EVERYTHING

def main():
    """Main function that runs the program"""
    print("Welcome to the Weather App!")
    
    # Get user input
    city = input("Enter a city name: ")
    
    # Step 1: Get the weather data
    weather_data = get_weather(city)
    
    # Step 2: Process the data
    if weather_data:
        weather_info = extract_weather_info(weather_data)
        
        # Step 3: Display the information
        display_weather_report(weather_info)
        
        # Step 4: Save the data
        save_choice = input("Would you like to save this weather data? (y/n): ")
        if save_choice.lower() == 'y':
            filename = save_weather_data(weather_data, city)
            if filename:
                print(f"Data saved to {filename}")
    else:
        print(f"Could not get weather data for {city}.")

# This is the standard way to run the main function when the script is executed
if __name__ == "__main__":
    main()