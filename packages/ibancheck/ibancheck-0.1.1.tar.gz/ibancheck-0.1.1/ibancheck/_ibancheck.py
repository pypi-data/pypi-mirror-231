#
# iban-check validates IBAN bank account numbers
# Copyright (C) 2023  Thijs Janssen (https://thijsj.nl)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

__all__ = ["is_valid", "create_iban"]

from ._specs import specs_per_country

def remove_spaces(a_string):
    return ''.join(c for c in a_string.strip() if not c in {' ', '\n', '\t'})

def iban_repr(iban):
    s = remove_spaces(iban)
    return ' '.join(s[i:i+4] for i in range(0, len(s), 4))

def get_spec(country):
    try:
        return specs_per_country[country]
    except KeyError:
        raise ValueError(f'Country code {country!r} is unknown.')

def _length_valid(spec, bban, iban):
    if len(bban) != spec.bban_length:
        raise ValueError(f'Length of {iban_repr(iban)!r} not correct.')

def is_valid(full_iban):
    full_iban = remove_spaces(full_iban)
    country = full_iban[:2]
    checksum = full_iban[2:4]
    bban = full_iban[4:]
    spec = get_spec(country)
    _length_valid(spec, bban, full_iban)
    c = as_number(bban+country+checksum) % 97
    if c != 1:
        raise ValueError(f'Inccorrect checksum in {iban_repr(full_iban)!r}.')
    return True

def as_number(a_str):
    return  int(''.join(char if char.isdigit() else str(ord(char) - ord('A') + 10) for char in a_str))

def create_iban(country, bban):
    spec = get_spec(country)
    bban = remove_spaces(bban)
    if (diff := spec.bban_length - len(bban)) > 0:
        bban = ('0' * diff) + bban
    _length_valid(spec, bban, bban)
    checksum = '{0:02d}'.format(98 - as_number(bban+country+'00') % 97)
    return iban_repr(country+checksum+bban)


def run_tests():
    def eq(a,b):
        assert a == b, f'Expected {a} == {b}'

    examples = [ # from fakeiban.org
        "DE54 5502 0000 8837 8132 12",
        "NL80 ABNA 4353 3681 41",
        "MC32 1450 8000 4077 3871 9884 O33",
        "GB21 BARC 2003 5368 3548 42",
        "TR43 0006 2917 8739 8979 8834 33",
    ]
    for iban in examples:
        assert is_valid(iban), iban

    def raises_valueerror(iban, ve=None):
        try:
            is_valid(iban)
        except ValueError as e:
            if ve is not None:
                eq(ve, str(e))
            return
        raise AssertionError(f'Expected ValueError, for "{iban}"')

    raises_valueerror('NL12BANK12345678', "Length of 'NL12 BANK 1234 5678' not correct.")
    raises_valueerror("DE55 5502 0000 8837 8132 12")
    raises_valueerror("NL81 ABNA 4353 3681 41")
    raises_valueerror("MC33 1450 8000 4077 3871 9884 O33")
    raises_valueerror("GB22 BARC 2003 5368 3548 42")
    raises_valueerror("TR44 0006 2917 8739 8979 8834 33", "Inccorrect checksum in 'TR44 0006 2917 8739 8979 8834 33'.")
    raises_valueerror("XX03 0004 0005 0006", "Country code 'XX' is unknown.")
    eq(10, as_number('A'))
    eq(1102, as_number('1A2'))
    eq(1, as_number("550200008837813212DE54") % 97)

    eq('ABCD E', iban_repr('ABCDE'))
    for iban in examples:
        eq(iban, iban_repr(iban))

    eq("NL80 ABNA 4353 3681 41", create_iban("NL", "ABNA 4353 3681 41"))
    eq("NL80 ABNA 4353 3681 41", create_iban("NL", "ABNA4353368141"))

    eq("TR43 0006 2917 8739 8979 8834 33", create_iban("TR", "6291 7873 9897 9883 433"))

    countries_with_incorrect_format_example = {'BI', 'EG', 'LY', 'SV', 'VA'}
    countries_with_invalid_checksum_example = {'NI', 'RU', 'ST'}
    for spec in specs_per_country.values():
        expected = spec.examples['iban_format']
        if spec.country in countries_with_incorrect_format_example:
            expected = iban_repr(expected)
        elif spec.country in countries_with_invalid_checksum_example:
            raises_valueerror(expected)
            continue
        eq(expected, create_iban(spec.country, spec.examples['iban'][4:]))



run_tests()
