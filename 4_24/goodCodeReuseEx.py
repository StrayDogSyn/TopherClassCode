def calculate_grade(average):
    """Return letter grade based on numerical average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def process_student(name, score1, score2, score3):
    """Process and display a student's grades."""
    total = score1 + score2 + score3
    average = total / 3
    
    print(f"\nStudent: {name}")
    print(f"Scores: {score1}, {score2}, {score3}")
    print(f"Average: {average}")
    print(f"Grade: {calculate_grade(average)}")

def main():
    """Main function to run the program."""
    print("Welcome to the Student Grade Calculator")
    
    # Process each student using the same function
    process_student("Alex", 85, 90, 78)
    process_student("Taylor", 92, 88, 95)
    process_student("Jordan", 76, 82, 79)
    
    print("\nThank you for using the Student Grade Calculator!")

# Run the program
if __name__ == "__main__":
    main()