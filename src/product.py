"""
product.py
~~~~~~~~~~~~~~~
This module defines the Product class. Also, active products in the catalog 
is defined as a list instead of fetching from a DB or file.
"""
import os
import json
from .exceptions import InvalidProductException


def get_product_price_mapping():
    """
    Loads products dict from a JSON file.
    """
    json_path = os.path.abspath('src/products.json')
    
    with open(json_path) as f:
        products = json.load(f)
    return products


class Product:
    """
    Product object

    :param code: Code of the product.
    """

    def __init__(self, code):
        self.product_price_map = get_product_price_mapping()
        self.active_products = self.product_price_map.keys()
        if code not in self.active_products:
            raise InvalidProductException('Product not in Catalog')
        self.code = code

    @property
    def price(self):
        """
        Returns the price of the product.
        """
        return self.product_price_map.get(self.code)
