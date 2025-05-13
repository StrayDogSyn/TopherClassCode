# Example 1: Basic Data Model for a Student Record System
# This demonstrates the fundamental concept of data modeling - organizing information

# A simple data model for a student in our system
student1 = {
    "id": 101,
    "first_name": "Emma",
    "last_name": "Johnson",
    "grade": 10,
    "subjects": ["Math", "Science", "English"],
    "gpa": 3.8
}

student2 = {
    "id": 102,
    "first_name": "Daniel",
    "last_name": "Smith",
    "grade": 11,
    "subjects": ["History", "Art", "Computer Science"],
    "gpa": 3.5
}

# student2 = {
#     "StudentID": 101,
#     "name": "John Doe",
#     "yr": "10th",
#     "subjects": "Math,Science,English",
#     "GPA": "3.8"
# }

# Using our data model
print(f"Student: {student1['first_name']} {student1['last_name']}")
print(f"Grade: {student1['grade']}")
print(f"Subjects: {', '.join(student1['subjects'])}")

# Adding new data to our model
student1["email"] = "emma.j@school.edu"
print(f"Contact: {student1['email']}")

# This is a very simple way to model data in Python using dictionaries
# We can easily store, retrieve, and modify information about our students
# In real applications, we'd use more structured approaches like classes