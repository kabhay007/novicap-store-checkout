"""
test_product.py
~~~~~~~~~~~~~~~
This module defines tests for product.py module.
"""
import pytest
from src.product import Product, get_product_price_mapping
from src.exceptions import InvalidProductException


class TestProduct:

    def test_price(self):
        product_price_map = get_product_price_mapping()

        for code in product_price_map.keys():
            product = Product(code)
            assert product.price == product_price_map.get(code)
    
    def test_create_invalid_product(self):
        code = 'INVALID'
        with pytest.raises(InvalidProductException):
            Product(code)
        