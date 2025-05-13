# Example 3: Data Models with Relationships
# This demonstrates how to model relationships between different types of data

class Student:
    def __init__(self, id, first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.enrolled_courses = []  # List to store relationships to Course objects
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def enroll_in_course(self, course):
        # Create a relationship between Student and Course
        self.enrolled_courses.append(course)
        # Update the course's student list (bi-directional relationship)
        course.add_student(self)
        print(f"{self.get_full_name()} enrolled in {course.name}")
    
    def list_courses(self):
        print(f"\n{self.get_full_name()}'s courses:")
        for course in self.enrolled_courses:
            print(f"- {course.name} taught by {course.teacher}")


class Course:
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher
        self.students = []  # List to store relationships to Student objects
    
    def add_student(self, student):
        # This method is called by Student.enroll_in_course
        self.students.append(student)
    
    def list_students(self):
        print(f"\nStudents enrolled in {self.name}:")
        for student in self.students:
            print(f"- {student.get_full_name()} (Grade {student.grade})")


# Create some students
emma = Student(101, "Emma", "Johnson", 10)
daniel = Student(102, "Daniel", "Smith", 11)
sophia = Student(103, "Sophia", "Garcia", 10)

# Create some courses
math_course = Course("MATH101", "Algebra", "Mrs. Peterson")
science_course = Course("SCI101", "Biology", "Mr. Rivera")
english_course = Course("ENG101", "Literature", "Ms. Thompson")

# Create relationships between students and courses
emma.enroll_in_course(math_course)
emma.enroll_in_course(science_course)
daniel.enroll_in_course(math_course)
daniel.enroll_in_course(english_course)
sophia.enroll_in_course(science_course)
sophia.enroll_in_course(english_course)

# Now we can navigate the relationships
emma.list_courses()
daniel.list_courses()

math_course.list_students()
science_course.list_students()

# This demonstrates a many-to-many relationship:
# - A student can enroll in multiple courses
# - A course can have multiple students enrolled
# This type of relationship is common in database design!