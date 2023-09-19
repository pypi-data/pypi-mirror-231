# IBAN Check

![Python Package Check](https://github.com/thijsj/iban-check/actions/workflows/python-package.yml/badge.svg)

Use ibancheck to validate IBAN bank account numbers.

### Usage

There are currently to main purposes of this module:

 1. Validating an IBAN number: `is_valid("NL00 BANK 1122 3344 55")`. Will return True or raise a ValueError.
 1. Creating an IBAN number and create a checksum: `create_iban("NL", "BANK1122334455")`.


### Testing

Testing is done in a _selftest_ manner. So tests are in the code and are run on import. To test manually do `python3 -c 'import ibancheck'`

### References

The International Bank Account Number is described by [European Committee For Banking Standards](https://ecbs.org) in [EBS204 v3.2 August 2003](https://www.ecbs.org/Download/EBS204_V3.2.pdf)
The official registry is in [ISO 13616](https://www.swift.com/sites/default/files/documents/iban_registry_0.pdf)
