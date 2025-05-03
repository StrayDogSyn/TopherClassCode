# Step 1: Initialize the list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Step 2: Prompt for fellow input
user_input = input("Enter a number: ")
try:
    num = int(user_input)
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()

# Step 3: Use conditional logic to modify the list
if num in numbers:
    numbers.remove(num)
    print(f"{num} was found and removed.")
else:
    numbers.append(num)
    print(f"{num} was not found and has been added.")

# Step 4: Return the final list and its length (here we use print to output)
def final_output(lst):
    return lst, len(lst)

updated_list, list_length = final_output(numbers)
print("Updated list:", updated_list)
print("List length:", list_length)