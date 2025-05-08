from grade_calculator import calculate_grade

def process_student(name, score1, score2, score3):
    """Process and display a student's grades."""
    total = score1 + score2 + score3
    average = total / 3
    
    print(f"\nStudent: {name}")
    print(f"Scores: {score1}, {score2}, {score3}")
    print(f"Average: {average}")
    print(f"Grade: {calculate_grade(average)}")