"""
test_order.py
~~~~~~~~~~~~~~~
This module defines tests for order.py module.
"""
import pytest
from src.order import Order


class TestOrder:

    def test_add_product(self):
        order = Order()
        order.add_product('MUG')
        assert 'MUG' in order.product_orders
        assert order.product_orders.get('MUG').quantity == 1
        