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

from cryptocurrencies import Cryptocurrency
from currencies import Currency

def get_data():
    Currency.get_dolar()
    Currency.get_euro()
    cryptocurrency = Cryptocurrency('bitcoin', False)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('dogecoin', False)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('ethereum', False)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('litecoin', False)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('dash', False)
    cryptocurrency.get_coins()


def save_data():
    Currency.get_dolar()
    Currency.get_euro()
    cryptocurrency = Cryptocurrency('bitcoin', True)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('dogecoin', True)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('ethereum', True)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('litecoin', True)
    cryptocurrency.get_coins()
    cryptocurrency = Cryptocurrency('dash', True)
    cryptocurrency.get_coins()

if __name__ == '__main__':
    all_data = str(input("Do you want to get all data?[Y/n]"))

    # Checks if user wants to get all data or just a certain currency.
    if all_data == "Y" or all_data == "y":
        save_data()
        response = str(input("Save data? [Y/n] "))

        if response == "Y" or response == "y":
            save_data()
        else:
            get_data()

    elif all_data == "N" or all_data == "n":
        currency = str(input("Which cryptocurrency do you want to get?"))
        save = str(input("Do you want to save the data?[Y/n]"))

        if save == "Y" or save == "y":
            cryptocurrency = Cryptocurrency(currency, True)
            cryptocurrency.get_coins()
        else:
            cryptocurrency = Cryptocurrency(currency, False)
            cryptocurrency.get_coins()
