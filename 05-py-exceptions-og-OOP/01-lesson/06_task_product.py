# Støpeform start
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}: {self.price:.2f}")
# Støpeform slutt

# Objekter i klassen:
apple = Product("Apple", 12.0)
bread = Product("Bread", 35.0)
milk = Product("Milk", 24)

# Objektet kaller metoden show_info()
apple.show_info()
bread.show_info()
milk.show_info()

# Endring av variabelen pris på objekter:
apple.price = 10
milk.price = 20
apple.show_info()
milk.show_info()