class Student:
    def __init__(self, name, registration_number):
        # Initialize the name and registration_number attributes
        self.name = name
        self.registration_number = registration_number
        self.age = None
        self.grades = []

    # Define a method to display the student information
    def display_information(self):
        print(f"Name: {self.name}, Registration Number: {self.registration_number}, Age: {self.age}")
        print("Grades:")
        for grade in self.grades:
            print(grade)

    # Define a method to set the age
    def set_age(self, age):
        self.age = age

    # Define a method to set the grades
    def set_grades(self, grades):
        self.grades = grades

# Example usage:
my_student = Student("Sofia", "23190439")

# Set the age
my_student.set_age(15)

# Set the grades
my_student.set_grades([15, 19, 12])

# Display the student information
my_student.display_information()