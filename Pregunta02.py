# Request a string of grades separated by commas
grades_string = input("Enter a list of grades separated by commas: ")

# Split the string into a list of individual grades
grades_list = grades_string.split(',')

# Initialize an empty list to store the integer grades
integer_grades = []

# Loop through each grade in the list
for grade in grades_list:
    # Try to convert the grade to an integer
    try:
        integer_grade = int(grade)
        integer_grades.append(integer_grade)
    # If the conversion fails, print an error message
    except ValueError:
        print(f"Invalid grade: {grade}")

# Print the list of integer grades
print(integer_grades)