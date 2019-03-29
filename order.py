from product import Product


class ProductOrder:

    def __init__(self, product_code, quantity):
        self.product = Product(product_code)
        self.quantity = quantity


class Order:

    def __init__(self):
        self.product_orders = {}

    def add_product(self, product_code):

        if product_code in self.product_orders:
            self.product_orders[product_code].quantity += 1
        else:
            product_order = ProductOrder(product_code, 1)
            self.product_orders[product_code] = product_order
