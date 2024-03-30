import math

class Circle:
    def __init__(self, radius):
        # Initialize the radius attribute
        self.radius = radius

    # Define a method to calculate the area
    def calculate_area(self):
        # Calculate the area using the formula pi * r^2
        area = math.pi * (self.radius ** 2)
        return area

# Example usage:
# Create a new circle with a radius of 5
my_circle = Circle(5)

# Calculate the area
area = my_circle.calculate_area()

# Print the result
print("The area of the circle is:", area)