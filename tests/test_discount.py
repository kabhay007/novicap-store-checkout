"""
test_discount.py
~~~~~~~~~~~~~~~
This module defines tests for discount.py module.
"""
import pytest
from src.discount import TwoForOneDiscount, BulkPurchaseDiscount
from src.order import Order


class TestTwoForOneDiscount:

    def test_get_discount_when_no_discount_applies(self):
        order = Order()
        products = ['VOUCHER', 'TSHIRT', 'MUG']
        for product in products:
            order.add_product(product)
        discount = TwoForOneDiscount('VOUCHER')
        assert discount.get_discount(order) == 0.0
    
    def test_get_discount_when_discount_applies(self):
        order = Order()
        products = ['VOUCHER', 'TSHIRT', 'VOUCHER']
        for product in products:
            order.add_product(product)
        discount = TwoForOneDiscount('VOUCHER')
        assert discount.get_discount(order) == 5.0


class TestBulkPurchaseDiscount:

    def test_get_discount_when_no_discount_applies(self):
        order = Order()
        products = ['VOUCHER', 'TSHIRT', 'MUG', 'MUG']
        for product in products:
            order.add_product(product)
        discount = BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        assert discount.get_discount(order) == 0.0
    
    def test_get_discount_when_discount_applies(self):
        order = Order()
        products = ['TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT']
        for product in products:
            order.add_product(product)
        discount = BulkPurchaseDiscount('TSHIRT', 3, 1.00)
        assert discount.get_discount(order) == 4.0
