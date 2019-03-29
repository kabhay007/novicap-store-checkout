# Novicap Store Checkout
========================

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