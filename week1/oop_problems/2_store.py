class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        result = self.final_price - self.stock_price
        return result


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, ram):
        super().__init__(name, stock_price, final_price)
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    products = {}

    def __init__(self, name):
        self.name = name
        Store.products = {}
        # така ли трябва да се дефинира ?

    def load_new_products(self, product, count):
        if product not in self.products:
            self.products[product] = count
        else:
            self.products[product] += count

    def list_products(self, product_class=object):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {} counts".format(product.name, self.products[product]))

    def sell_products(self, product):
        if product in self.products and self.products[product] > 0:
            return True
        else:
            return False

    def total_income(self):
        #има ли други начини за дефиниране на 2те променливи
        total_stock_price = 0
        total_final_price = 0
        for product in self.products:
            total_stock_price += self.products[product] * product.stock_price
            total_final_price += self.products[product] * product.final_price
        income = total_final_price - total_stock_price
        return income

#creat products

lap1 = Laptop('hp', 1200, 1600, 2)
lap2 = Laptop('To-Shiba', 1100, 1500, 4)
lap3 = Laptop('To-ne-Shiba', 1400, 1800, 8)
smart1 = Smartphone("LG", 1000, 1400, 5, 8)
smart2 = Smartphone("Sony", 1000, 1200, 5, 8)
smart = Smartphone("samsung", 500, 700, 3, 5)

#creat store

store = Store("laptop.bg")

#load products

store.load_new_products(smart, 0)
store.load_new_products(lap1, 0)
store.load_new_products(lap2, 2)
store.load_new_products(lap3, 1)
store.load_new_products(smart1, 3)
store.load_new_products(smart2, 3)

#checks/ prints/functions

store.list_products(Smartphone)
print(store.sell_products(smart))
print(store.total_income())
store.load_new_products(lap1, 1)
store.list_products()
print(store.total_income())
