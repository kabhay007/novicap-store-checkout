from order import Order
from discount import TwoForOneDiscount, BulkPurchaseDiscount


class Checkout:

    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.order = Order()

    def scan(self, product_code):
        self.order.add_product(product_code)

    @property
    def total(self):
        total_price = self.get_total_amount()
        discounts = self.get_total_discount()
        
        return total_price - discounts

    def get_total_amount(self):
        total_price = 0.00

        for k, v in self.order.product_orders.items():
            total_price += v.quantity * v.product.price
        
        return total_price

    def get_total_discount(self):
        total_discount = 0.00

        for promotion in self.pricing_rules:
            total_discount += promotion.get_discount(self.order)

        return total_discount
