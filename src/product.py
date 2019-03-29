"""
product.py
~~~~~~~~~~~~~~~
This module defines the Product class. Also, active products in the catalog 
is defined as a list instead of fetching from a DB or file.
"""
from .exceptions import InvalidProductException

ITEMS = ['VOUCHER', 'TSHIRT', 'MUG']
PRICE_MAPPING = {
    'VOUCHER': 5.00,
    'TSHIRT': 20.00,
    'MUG': 7.50
}


class Product:
    """
    Product object

    :param code: Code of the product.
    """

    def __init__(self, code):
        if code not in ITEMS:
            raise InvalidProductException('Product not in Catalog')
        self.code = code

    @property
    def price(self):
        """
        Returns the price of the product.
        """
        return PRICE_MAPPING.get(self.code)
