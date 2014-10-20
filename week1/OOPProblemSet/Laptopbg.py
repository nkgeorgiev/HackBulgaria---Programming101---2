class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        Product.__init__(self, name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        Product.__init__(self, name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.total = 0

    def load_new_products(self, product, count):
        if product in self.products.keys():
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        if product_class in self.products.keys():
            return product_class.name + " - " + str(self.products[product_class])

    def sell_product(self, product):
        if product not in self.products.keys() or self.products[product] == 0:
            return False

        self.products[product] -= 1
        self.total += product.profit()

        return True

    def total_income(self):
        return self.total
