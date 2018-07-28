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

import sys

from cryptocurrency import Cryptocurrency
from utils import get_certain_currency, get_data, save_data

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments.")
        exit()

    if sys.argv[1] == "get":
        if sys.argv[2] == "all":
            if sys.argv[3].lower() == "save":
                save_data()
            else:
                get_data()
        else:
            currency = sys.argv[2]

            if sys.argv[3].lower() == "save":
                get_certain_currency(currency, True)
            else:
                get_certain_currency(currency, False)
    elif sys.argv[1] == "exchange":
        currency = Cryptocurrency(sys.argv[2].lower(), False)
        currency.coin_to_dollar(float(sys.argv[3]))
