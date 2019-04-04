"""
checkout.py
~~~~~~~~~~~~~~~
This module contains the Checkout class which is used to scan products and calculate total.
"""
from .order import Order
from .discount import TwoForOneDiscount, BulkPurchaseDiscount


class Checkout:
    """Checkout class

    :param pricing_rules: List of discount objects applicable on checkout
    """

    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.order = Order()
        self.discount_array = []

    def scan(self, product_code):
        """
        Method to scan product. Adds the product order to the list of orders.

        :param product_code: Code of the product to scan.
        """
        self.order.add_product(product_code)

    @property
    def total(self):
        """
        Attribute which calculates the total amount on the order after deducting discounts.
        """
        total_price = self.get_total_amount()
        discounts = self.get_total_discount()

        return total_price - discounts

    def get_total_amount(self):
        """
        Returns the total amount of the order without discounts.
        """
        total_price = 0.00

        for k, v in self.order.product_orders.items():
            total_price += v.quantity * v.product.price

        return total_price

    def get_total_discount(self):
        """
        Calculates total discount applicable on this order.
        """
        total_discount = 0.00

        for promotion in self.pricing_rules:
            discount = promotion.get_discount(self.order)
            total_discount += discount

        return total_discount

    def get_discount_array(self):
        discount_array = []

        for promotion in self.pricing_rules:
            discount = promotion.get_discount(self.order)
            if discount > 0:
                discount_array.append(
                    {
                        'name': type(promotion).__name__,
                        'amount': discount,
                        'metadata': promotion.get_meta_data()
                    }
                )

        return discount_array

    def get_total_display(self):
        """
        Return total but in a pretty format with Euro sign.
        """
        total = self.total
        return '%.2f\N{euro sign}' % total

    def get_receipt(self):
        receipt = {
            'total': self.get_total_amount(),
            'discount': self.get_discount_array(),
            'discounted_amount': self.get_total_discount(),
            'final_amount': self.total
        }

        return receipt
