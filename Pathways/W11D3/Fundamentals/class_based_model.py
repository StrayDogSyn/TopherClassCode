# Example 2: Class-based Data Model
# This demonstrates how we can use Python classes to create more structured data models

class Student:
    # Initialize a student with their basic information
    def __init__(self, id, first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.subjects = []
        self.gpa = 0.0
        self.email = None
    
    # Get the student's full name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Add a subject to the student's list
    def add_subject(self, subject):
        self.subjects.append(subject)
        print(f"Added {subject} to {self.get_full_name()}'s subjects")
    
    # Update the student's GPA
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"Updated {self.get_full_name()}'s GPA to {self.gpa}")
    
    # Display student information
    def display_info(self):
        print(f"Student ID: {self.id}")
        print(f"Name: {self.get_full_name()}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"GPA: {self.gpa}")
        if self.email:
            print(f"Email: {self.email}")
        print("-" * 30)

# Create student objects
emma = Student(101, "Emma", "Johnson", 10)
daniel = Student(102, "Daniel", "Smith", 11)

# Add data to our student objects
emma.add_subject("Math")
emma.add_subject("Science")
emma.add_subject("English")
emma.update_gpa(3.8)
emma.email = "emma.j@school.edu"

daniel.add_subject("History")
daniel.add_subject("Art")
daniel.add_subject("Computer Science")
daniel.update_gpa(3.5)

# Display student information
emma.display_info()
daniel.display_info()

# This class-based approach gives us more structure and functionality
# than using simple dictionaries