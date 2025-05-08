# GOOD EXAMPLE - Using code reuse with a function

# Define the conversion function once
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Now use this function for all conversions
room_temp_c = 22
room_temp_f = celsius_to_fahrenheit(room_temp_c)
print(f"Room temperature: {room_temp_c}°C is {room_temp_f}°F")

outdoor_temp_c = 15
outdoor_temp_f = celsius_to_fahrenheit(outdoor_temp_c)
print(f"Outdoor temperature: {outdoor_temp_c}°C is {outdoor_temp_f}°F")

body_temp_c = 37
body_temp_f = celsius_to_fahrenheit(body_temp_c)
print(f"Body temperature: {body_temp_c}°C is {body_temp_f}°F")