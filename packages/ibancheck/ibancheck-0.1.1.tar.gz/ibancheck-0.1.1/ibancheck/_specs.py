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
from pkg_resources import resource_stream
import json

__all__ = ['specs_per_country']

specs_per_country = {}

class Spec:
    def __init__(self, country, country_name, bban_length, **remainder):
        self.country = country
        if len(country) != 2 or not isinstance(country, str) or not set(country).issubset('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise TypeError("Incorrect format")
        self.name = country_name
        if not isinstance(country_name, str) or len(country_name) < 4:
            raise TypeError("Incorrect format")
        self.bban_length = bban_length
        self.full_length = bban_length + 4 # country 2, checksum 2, bban
        if bban_length < 10 or bban_length > 30:
            raise TypeError("Incorrect format")
        specs_per_country[country] = self
        self.examples = {}
        for k,v in remainder.items():
            if k.endswith('_example'):
                self.examples[k.replace("_example", '')] = v

# Specification is based on https://www.swift.com/sites/default/files/documents/iban_registry_0.pdf

for spec in json.load(resource_stream('ibancheck', 'registry_data.json')):
    Spec(**spec)

# TODO extract all spec from registry af SWIFT
