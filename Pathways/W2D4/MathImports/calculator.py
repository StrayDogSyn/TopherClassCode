# This file is called calculator.py
# It uses the functions from math_helpers.py

# This line imports the functions from the other file
from math_helpers import add, subtract, multiply

# Now we can use those functions
print("Welcome to the Simple Calculator!")

# Use the add function
result1 = add(5, 3)
print(f"5 + 3 = {result1}")
print(add(2,5))

# Use the subtract function
result2 = subtract(10, 4)
print(f"10 - 4 = {result2}")

# Use the multiply function
result3 = multiply(6, 7)
print(f"6 × 7 = {result3}")

print("Thank you for using the Simple Calculator!")