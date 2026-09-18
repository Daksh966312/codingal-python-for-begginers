class Product:
    def __init__(self):
        self.__price = 20000

    def sell(self):
        print(f"Product is sold at: {self.__price}")

    def set_price(self, amount):
        self.__price = amount

laptop = Product()
laptop.sell()
laptop.set_price(10000)
laptop.sell()