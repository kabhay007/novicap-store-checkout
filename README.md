# Novicap Store Checkout

## Usage

``` {.sourceCode .python}
>>> from checkout import Checkout
>>> from discount import TwoForOneDiscount, BulkPurchaseDiscount
>>> pricing_rules = [TwoForOneDiscount('VOUCHER'), BulkPurchaseDiscount('TSHIRT', 3, 1.00)]
>>> co = Checkout(pricing_rules)
>>> co.scan("VOUCHER")
>>> co.scan("VOUCHER")
>>> co.scan("TSHIRT")
>>> price = co.total
```

## Notes

The checkout process is implemented in Python 3.

The code implements checkout class with multiple discount schemes. Only 3 products are added at the moment. The products can be scanned/added in any order. Some assumptions made in this approach are.
- Only products available in the catalog should be allowed to be ordered. Ideally, the list of products should be read from DB or from a file. I have added them inside a list in product.py file just to make things simple. If any new product needs to be added, one can just add it to the list along with it's price.
- Application of discount could have been done per product or per order. I have chosen to apply a particular discount scheme on the order because I believe generally discounts depend on the collection and not per product. 