"""
discount.py
~~~~~~~~~~~~~~~
This module contains the base discount class and discounts schemes applicable.
To add a new discount scheme, a new class should subclass the base Discount class.
"""


class Discount:
    """Base Discount object
    """

    def __init__(self):
        pass

    def get_discount(self, order):
        return NotImplementedError()


class TwoForOneDiscount(Discount):
    """
    2-for-1 promotion object

    :param product_code: Code of product on which 2-for-1 special will be applicable.
    """

    def __init__(self, product_code):
        self.product_code = product_code

    def get_discount(self, order):
        """
        Calculates the total discount on the order.

        :param order: Order object.
        """
        discount = 0.00
        product_orders = order.product_orders
        product_order = product_orders.get(self.product_code)

        if product_order:
            quantity = product_order.quantity
            num_free_items = quantity // 2
            discount = num_free_items * product_order.product.price

        return discount


class BulkPurchaseDiscount(Discount):
    """
    Bulk purchase promotion object

    :param product_code: Code of product on which 2-for-1 special will be applicable.
    :param min_amount: Minimum quantity of product needed to apply the discount.
    :param discount_per_unit: Discount applicable per unit of the product.
    """

    def __init__(self, product_code, min_amount, discount_per_unit):
        self.product_code = product_code
        self.min_amount = min_amount
        self.discount_per_unit = discount_per_unit

    def get_discount(self, order):
        """
        Calculates the total discount on the order.

        :param order: Order object.
        """
        discount = 0.00
        product_orders = order.product_orders
        product_order = product_orders.get(self.product_code)

        if product_order:
            quantity = product_order.quantity

            if quantity >= self.min_amount:
                discount = self.discount_per_unit * quantity

        return discount
