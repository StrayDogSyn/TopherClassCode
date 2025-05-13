user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type something (or 'exit' to quit): ")
    if user_input.lower() != "exit":
        print("You typed:", user_input)
print("Goodbye!")


# user_input = ""
# while True:
#     if user_input.lower() == "exit":
#         break
#     user_input = input("Type something (or 'exit' to quit): ")
#     print("You typed:", user_input)
# print("Goodbye!")