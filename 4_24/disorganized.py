"""
BAD WEATHER APP - Example of poorly organized code
This is what NOT to do when writing Python programs!
"""

import requests
import json
import os
from datetime import datetime
import random

# Bad Practice #1: Hardcoding sensitive information directly in your code
API_KEY = "eaf68ffb413d707283399af330d02c3f"

# Bad Practice #2: Using global variables that can be changed from anywhere
city_name = ""
current_temp = 0
save_to_file = True

# Bad Practice #3: Function that does too many different things at once
def get_weather_and_save_and_print(city):
    global city_name  # Bad Practice #4: Modifying global variables inside functions
    global current_temp
    
    # Get weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    # Process the data
    if response.status_code == 200:
        data = response.json()
        city_name = data.get("name", "Unknown")
        current_temp = data.get("main", {}).get("temp", 0)
        weather_desc = data.get("weather", [{}])[0].get("description", "")
        
        # Save the data (mixed with getting and processing)
        if save_to_file:
            folder = "data"
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            time_now = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"{folder}/{city}_{time_now}.json"
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Saved data to {filename}")
        
        # Print a report (also mixed with the other tasks)
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {current_temp}°C")
        print(f"Conditions: {weather_desc}")
        
        # Bad Practice #5: Inconsistent return values
        if random.choice([True, False]):  # Sometimes returns one thing, sometimes another!
            return f"It's {current_temp}°C in {city_name}"
        else:
            return data
    else:
        print(f"Error: Couldn't get weather. Code: {response.status_code}")
        return None

# Bad Practice #6: Confusing function name that doesn't explain what it does
def do_stuff_with_weather():
    for i in range(3):  # Hard-coded number of retries
        try:
            user_city = input("Enter a city name: ")
            result = get_weather_and_save_and_print(user_city)
            
            # Bad Practice #7: Deeply nested code that's hard to follow
            if result:
                if isinstance(result, dict):
                    if "main" in result:
                        if "humidity" in result["main"]:
                            humidity = result["main"]["humidity"]
                            print(f"Humidity: {humidity}%")
                            
                            # Bad Practice #8: Magic numbers with no explanation
                            if humidity > 80:
                                print("It's very humid today!")
                            elif humidity < 30:
                                print("It's very dry today!")
            
            # Stop the loop if we got here without errors
            break
            
        except Exception as e:
            # Bad Practice #9: Catching all exceptions and not handling them specifically
            print(f"Something went wrong: {e}")
            print("Let's try again...")
    
    # Bad Practice #10: Confusing logic flow - saving history at the end for no reason
    if city_name:  # Using the global variable
        save_search_history(city_name)

# Another function that does too much and uses global variables
def save_search_history(city):
    history_file = "search_history.txt"
    
    try:
        # Read existing history
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = f.readlines()
        else:
            history = []
        
        # Add new entry
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append(f"{time_now}: {city} - {current_temp}°C\n")  # Using global variable
        
        # Keep only last 10 entries
        if len(history) > 10:
            history = history[-10:]
        
        # Write back to file
        with open(history_file, 'w') as f:
            f.writelines(history)
            
        print(f"Updated search history in {history_file}")
    except:
        # Bad Practice #11: Empty except block with no specific handling
        pass

# Main program - everything in one place
def main():
    print("=== WEATHER APP ===")
    
    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Change settings")
        print("3. Exit")
        
        # Bad Practice #12: No input validation
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            do_stuff_with_weather()  # Unclear function name
        elif choice == "2":
            # Bad Practice #13: Mixing UI and logic
            global save_to_file
            print("\nSettings:")
            print(f"Currently saving data to files: {'Yes' if save_to_file else 'No'}")
            new_setting = input("Save data to files? (y/n): ")
            if new_setting.lower() in ['y', 'yes']:
                save_to_file = True
                print("Will save data to files")
            else:
                save_to_file = False
                print("Will not save data to files")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Program starts here
if __name__ == "__main__":
    main()