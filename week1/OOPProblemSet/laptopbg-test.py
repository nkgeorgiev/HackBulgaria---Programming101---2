import unittest

from Laptopbg import Product, Laptop, Smartphone, Store


class LaptopbgTest(unittest.TestCase):
    def test_Product_init(self):
        product = Product("test", 100, 150)
        self.assertEqual("test", product.name)
        self.assertEqual(100, product.stock_price)
        self.assertEqual(150, product.final_price)

    def test_product_profit(self):
        product = Product("test", 100, 150)
        self.assertEqual(50, product.profit())

    def test_laptop_init(self):
        laptop = Laptop("test", 100, 150, 1000, 8)
        self.assertEqual("test", laptop.name)
        self.assertEqual(100, laptop.stock_price)
        self.assertEqual(150, laptop.final_price)
        self.assertEqual(1000, laptop.diskspace)
        self.assertEqual(8, laptop.RAM)

    def test_smartphone_init(self):
        smartphone = Smartphone("test", 100, 150, 6, 13)
        self.assertEqual("test", smartphone.name)
        self.assertEqual(100, smartphone.stock_price)
        self.assertEqual(150, smartphone.final_price)
        self.assertEqual(6, smartphone.display_size)
        self.assertEqual(13, smartphone.mega_pixels)

    def test_store_init(self):
        store = Store("test")
        self.assertEqual("test", store.name)
        self.assertDictEqual({}, store.products)
        self.assertEqual(0, store.total)

    def test_store_load_new_products(self):
        store = Store("test")
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        store.load_new_products(smartphone, 10)
        store.load_new_products(laptop, 20)
        d = {laptop: 20, smartphone: 10}
        self.assertDictEqual(d, store.products)

    def test_store_list_products(self):
        store = Store("test")
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        store.load_new_products(laptop, 20)
        string = store.list_products(laptop)
        self.assertEqual(laptop.name + " - " + str(store.products[laptop]),
                         string)
        self.assertTrue(store.list_products(laptop))
        self.assertFalse(store.list_products(smartphone))

    def test_store_sell_product(self):
        store = Store("test")
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        store.load_new_products(laptop, 1)
        self.assertFalse(store.sell_product(smartphone))
        self.assertTrue(store.sell_product(laptop))
        self.assertFalse(store.sell_product(laptop))

    def test_store_total_income(self):
        store = Store("test")
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        laptop = Laptop('HP HackBook', 1000, 1250, 1000, 4)
        store.load_new_products(laptop, 5)
        for i in range(3):
            store.sell_product(laptop)
        self.assertEqual(750, store.total_income())


if __name__ == '__main__':
    unittest.main()
