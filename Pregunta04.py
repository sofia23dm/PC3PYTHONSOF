class Rectangle:
    def __init__(self, length, width):
        # Initialize the length and width attributes
        self.length = length
        self.width = width

    # Define a method to calculate the area
    def calculate_area(self):
        # Calculate the area using the formula length * width
        area = self.length * self.width
        return area

# Example usage:
# Create a new rectangle with a length of 5 and a width of 10
my_rectangle = Rectangle(5, 10)

# Calculate the area
area = my_rectangle.calculate_area()

# Print the result
print("The area of the rectangle is:", area)