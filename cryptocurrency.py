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

import os
import csv
import time

from urllib.error import HTTPError

import requests


class Cryptocurrency:

    def __init__(self, currency, save):
        self.currency = currency.lower()
        self.save = save

    def get_coins(self):
        try:
            r = requests.get(
                "https://api.coinmarketcap.com/v1/ticker/{}"
                .format(self.currency))
            coin_data = r.json()
            coin_data = coin_data[0]
        except HTTPError:
            print("Can't connect to the server")
            return False

        if float(coin_data["price_usd"]) > 1:
            price = float("{:.2f}".format(float(coin_data["price_usd"])))
        else:
            price = float(coin_data["price_usd"])

        # Saves the data retrieved in a csv file.
        if self.save is True:
            folder = os.path.dirname(os.path.abspath(__file__))
            file = folder + "/data/{}_data.csv".format(self.currency)

            with open(file, "a") as file:
                date = time.strftime("%x-%X")
                data = [date, price]
                write = csv.writer(file)
                write.writerow(data)

        print("{currency} ({symbol}): ${price}".format(
            currency=coin_data['name'],
            symbol=coin_data['symbol'],
            price=price))

        return float(coin_data["price_usd"])

    def coin_to_dollar(self, number_of_coins):
        """This function takes a certain cryptocurrency and exchange
        it to dollars.
        """
        price = self.get_coins()
        coin_in_dollar = number_of_coins * price
        print(coin_in_dollar)
