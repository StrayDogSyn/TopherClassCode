# bad_code_reuse.py - An example of poor coding practices for beginners

# This program calculates grades for different students
# Notice how similar code is copied and pasted multiple times

print("Welcome to the Student Grade Calculator")

# Calculate grades for student 1
student1_name = "Alex"
student1_score1 = 85
student1_score2 = 90
student1_score3 = 78

student1_total = student1_score1 + student1_score2 + student1_score3
student1_average = student1_total / 3

print(f"\nStudent: {student1_name}")
print(f"Scores: {student1_score1}, {student1_score2}, {student1_score3}")
print(f"Average: {student1_average}")

if student1_average >= 90:
    print("Grade: A")
elif student1_average >= 80:
    print("Grade: B")
elif student1_average >= 70:
    print("Grade: C")
elif student1_average >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Calculate grades for student 2 - same code copied!
student2_name = "Taylor"
student2_score1 = 92
student2_score2 = 88
student2_score3 = 95

student2_total = student2_score1 + student2_score2 + student2_score3
student2_average = student2_total / 3

print(f"\nStudent: {student2_name}")
print(f"Scores: {student2_score1}, {student2_score2}, {student2_score3}")
print(f"Average: {student2_average}")

if student2_average >= 90:
    print("Grade: A")
elif student2_average >= 80:
    print("Grade: B")
elif student2_average >= 70:
    print("Grade: C")
elif student2_average >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Calculate grades for student 3 - same code copied again!
student3_name = "Jordan"
student3_score1 = 76
student3_score2 = 82
student3_score3 = 79

student3_total = student3_score1 + student3_score2 + student3_score3
student3_average = student3_total / 3

print(f"\nStudent: {student3_name}")
print(f"Scores: {student3_score1}, {student3_score2}, {student3_score3}")
print(f"Average: {student3_average}")

if student3_average >= 90:
    print("Grade: A")
elif student3_average >= 80:
    print("Grade: B")
elif student3_average >= 70:
    print("Grade: C")
elif student3_average >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("\nThank you for using the Student Grade Calculator!")