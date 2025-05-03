while True:
    user_input = input("Enter a number (or 'stop' to exit): ")
    if user_input.lower() == "stop":
        print("Exiting the program.")
        break
    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'stop'.")
        continue
    
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")