def main():
    while True:
        print("\nGrocery List Manager")
        print("--------------------")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Display the list")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == "3":
            print("Current Grocery List:")
            for itm in display_list():
                print("- " + itm)
        elif choice == "4":
            print("Thank you for using the Grocery List Manager!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")