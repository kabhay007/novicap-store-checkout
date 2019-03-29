

class Discount:

    def __init__(self):
        pass

    def get_discount(self, order):
        return NotImplementedError()


class TwoForOneDiscount(Discount):

    def __init__(self, product_code):
        self.product_code = product_code

    def get_discount(self, order):
        discount = 0.00
        product_orders = order.product_orders
        product_order = product_orders.get(self.product_code)

        if product_order:
            quantity = product_order.quantity
            num_free_items = quantity // 2
            discount = num_free_items * product_order.product.price

        return discount


class BulkPurchaseDiscount(Discount):

    def __init__(self, product_code, min_amount, discount_per_unit):
        self.product_code = product_code
        self.min_amount = min_amount
        self.discount_per_unit = discount_per_unit

    def get_discount(self, order):
        discount = 0.00
        product_orders = order.product_orders
        product_order = product_orders.get(self.product_code)

        if product_order:
            quantity = product_order.quantity

            if quantity >= self.min_amount:
                discount = self.discount_per_unit * quantity

        return discount
