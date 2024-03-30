class Product:
    def __init__(self, name, year, price):
        # Initialize the name, year, and price attributes
        self.name = name
        self.year = year
        self.price = price

    # Define a method to display the product details
    def display_product(self):
        print(f"Name: {self.name}, Year: {self.year}, Price: {self.price}")

class Catalog:
    def __init__(self):
        # Initialize an empty list to store the products
        self.products = []

    # Define a method to add a product
    def add_product(self, product):
        self.products.append(product)

    # Define a method to display the list of products
    def show_products(self):
        print("Products:")
        for product in self.products:
            product.display_product()

    # Define a method to filter the products by year
    def filter_by_year(self, year):
        print(f"Products from year {year}:")
        for product in self.products:
            if product.year == year:
                product.display_product()

# Example usage:
my_catalog = Catalog()

# Add products to the catalog
my_catalog.add_product(Product("Tire", 2015, 100))
my_catalog.add_product(Product("Battery", 2018, 50))
my_catalog.add_product(Product("Muffler", 2019, 200))

# Display the list of products
my_catalog.show_products()

# Filter the products by year
my_catalog.filter_by_year(2018)