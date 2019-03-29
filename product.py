from exceptions import InvalidProductException

ITEMS = ['VOUCHER', 'TSHIRT', 'MUG']
PRICE_MAPPING = {
    'VOUCHER': 5.00,
    'TSHIRT': 20.00,
    'MUG': 7.50
}


class Product:

    def __init__(self, code):
        if code not in ITEMS:
            raise InvalidProductException('Product not in Catalog')
        self.code = code

    @property
    def price(self):
        return PRICE_MAPPING.get(self.code)
