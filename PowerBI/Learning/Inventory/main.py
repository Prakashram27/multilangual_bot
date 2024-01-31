import os

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            self.create_inventory_file()
        self.products = self.load_inventory()

    def create_inventory_file(self):
        with open(self.filename, 'w') as file:
            file.write("")

    def load_inventory(self):
        products = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name = data[0]
                    quantity = int(data[1])
                    product = Product(name, quantity)
                    products.append(product)
        except FileNotFoundError:
            print("Inventory file not found. Starting with an empty inventory.")
        return products

    def save_inventory(self):
        with open(self.filename, 'w') as file:
            for product in self.products:
                file.write(f"{product.name},{product.quantity}\n")

    def add_product(self, name, quantity):
        product = self.get_product(name)
        if product:
            product.quantity += quantity
        else:
            new_product = Product(name, quantity)
            self.products.append(new_product)

    def remove_product(self, name, quantity):
        product = self.get_product(name)
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
            else:
                print("Insufficient quantity.")
        else:
            print("Product not found.")

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products:
            print(f"Product: {product.name}, Quantity: {product.quantity}")


# Example usage:
inventory = Inventory("inventory.txt")

# Adding products to inventory
inventory.add_product("Apple", 10)
inventory.add_product("Banana", 5)
inventory.add_product("Orange", 7)
inventory.add_product("Apple", 5)  # Adding more quantity to existing product

# Removing products from inventory
inventory.remove_product("Apple", 2)
inventory.remove_product("Pineapple", 10)  # Trying to remove a non-existent product
inventory.add_product("unknown",20)
# Displaying current inventory
inventory.display_inventory()

# Saving the inventory to the file
inventory.save_inventory()



