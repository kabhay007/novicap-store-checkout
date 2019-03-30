"""
test_checkout.py
~~~~~~~~~~~~~~~
This module defines tests for checkout.py module.
"""
import pytest
from src.checkout import Checkout
from src.discount import TwoForOneDiscount, BulkPurchaseDiscount


class TestCheckout:

    def test_scan(self):
        code = 'VOUCHER'
        pricing_rules = [
            TwoForOneDiscount('VOUCHER'),
            BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        ]
        checkout = Checkout(pricing_rules)
        checkout.scan(code)

        assert code in checkout.order.product_orders
        assert checkout.order.product_orders[code].quantity == 1

    def test_get_total_amount(self):
        pricing_rules = [
            TwoForOneDiscount('VOUCHER'),
            BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        ]
        checkout = Checkout(pricing_rules)
        products = ['TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT']

        for product in products:
            checkout.scan(product)

        assert checkout.get_total_amount() == 65.0

    def test_get_total_discount(self):
        pricing_rules = [
            TwoForOneDiscount('VOUCHER'),
            BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        ]
        checkout = Checkout(pricing_rules)
        products = ['TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'MUG']

        for product in products:
            checkout.scan(product)

        assert checkout.get_total_discount() == 3.0

    def test_total(self):
        pricing_rules = [
            TwoForOneDiscount('VOUCHER'),
            BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        ]
        checkout = Checkout(pricing_rules)
        products = ['TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT']

        for product in products:
            checkout.scan(product)

        assert checkout.total == 81.0
        assert checkout.get_total_display() == '81.00\N{euro sign}'

    def test_all_discounts(self):
        pricing_rules = [
            TwoForOneDiscount('VOUCHER'),
            BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        ]
        checkout = Checkout(pricing_rules)
        products = 5*['TSHIRT'] + 2*['MUG'] + 5*['VOUCHER']
        for product in products:
            checkout.scan(product)

        assert checkout.total == 125
