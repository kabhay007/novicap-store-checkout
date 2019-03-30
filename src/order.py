"""
order.py
~~~~~~~~~~~~~~~
This module contains the ProductOrder and Order objects.
"""
from .product import Product


class ProductOrder:
    """
    When a product is ordered

    :param product_code: Code of product ordered.
    :param quantity: Quantity of product ordered.
    """

    def __init__(self, product_code, quantity):
        self.product = Product(product_code)
        self.quantity = quantity


class Order:
    """
    Order object
    Contains a list of ProductOrder objects.

    """

    def __init__(self):
        self.product_orders = {}

    def add_product(self, product_code):
        """Adds a product to an order object

        :param product_code: Product code to be added to the order.
        """

        if product_code in self.product_orders:
            self.product_orders[product_code].quantity += 1
        else:
            product_order = ProductOrder(product_code, 1)
            self.product_orders[product_code] = product_order
