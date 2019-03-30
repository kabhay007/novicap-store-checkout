# Novicap Store Checkout

## Setup

Clone the repo. You will need Python 3. Using a Virtual environment is recommended.
Pytest used for unit testing. Install it from requirements.txt file.
```
$ pip install -r requirements.txt 
```

## Usage

``` {.sourceCode .python}
>>> from src.checkout import Checkout
>>> from src.discount import TwoForOneDiscount, BulkPurchaseDiscount
>>> pricing_rules = [TwoForOneDiscount('VOUCHER'), BulkPurchaseDiscount('TSHIRT', 3, 1.00)]
>>> co = Checkout(pricing_rules)
>>> co.scan("VOUCHER")
>>> co.scan("VOUCHER")
>>> co.scan("TSHIRT")
>>> price = co.total
```

## Tests
To run the tests.
```
$ pytest
```

## Notes

The checkout process is implemented in Python 3.

The code implements checkout class with multiple discount schemes. Only 3 products are added at the moment. The products can be scanned/added in any order. Some assumptions made in this approach are.

- Only products available in the catalog should be allowed to be ordered. Ideally, the list of products should be read from DB or from a file. I have added them in a JSON file **products.json** just to make things simple. If any new product needs to be added, one can just add it to the file along with it's price.
- In an ideal scenario there will be a storefront which will have a list of active products and only these products can be ordered. Omitted extra complications for simplicity.
- Application of discount could have been done per product or per order. I have chosen to apply discount scheme on the order object rather than calculating per product because I believe generally discounts depend on the collection and not per product.
- To add a new promotion scheme, subclass the `Discount` class and implement the `get_discount` method.
- `Product` class defines a Product instance. When a product is ordered with certain number of quantities, the data is stored in `ProductOrder`. A list of Product orders constitute an `Order` class. `Checkout` class implements the checkout functionality of checkout. Everytime a product is scanned, an order object is created along with the ProductOrder and Product instances.
- `Product.scan` is used to scan a product and `Product.total` to get the final discounted amount.