"""
Edison Neto, This software simply gets data from some cryptocurrencies.
Copyright (C) 2018 Edison Neto

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from cryptocurrency import Cryptocurrency

cryptocurrencies = [
    "bitcoin",
    "ethereum",
    "litecoin",
    "dash",
    "dogecoin"
]


def get_data():
    for crypto in cryptocurrencies:
        cryptocurrency = Cryptocurrency(crypto, False)
        cryptocurrency.get_coins()


def save_data():
    for crypto in cryptocurrencies:
        cryptocurrency = Cryptocurrency(crypto, True)
        cryptocurrency.get_coins()


def get_certain_currency(currency, save):
    cryptocurrency = Cryptocurrency(currency, save)
    cryptocurrency.get_coins()
    return True
