# BAD EXAMPLE - Repeating the same calculation instead of reusing code

# Convert room temperature from Celsius to Fahrenheit
room_temp_c = 22
room_temp_f = (room_temp_c * 9/5) + 32
print(f"Room temperature: {room_temp_c}°C is {room_temp_f}°F")

# Convert outdoor temperature from Celsius to Fahrenheit
outdoor_temp_c = 15
outdoor_temp_f = (outdoor_temp_c * 9/5) + 32  # Same formula repeated!
print(f"Outdoor temperature: {outdoor_temp_c}°C is {outdoor_temp_f}°F")

# Convert body temperature from Celsius to Fahrenheit
body_temp_c = 37
body_temp_f = (body_temp_c * 9/5) + 32  # Same formula repeated again!
print(f"Body temperature: {body_temp_c}°C is {body_temp_f}°F")