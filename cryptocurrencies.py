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

from bs4 import BeautifulSoup
import requests

class Cryptocurrency:

    def __init__(self, currency, save):
        self.currency = currency
        self.save = save


    def get_coins(self):
        # Try to connect to the server.
        try:
            r = requests.get("https://coinmarketcap.com/currencies/{}/"
                                                    .format(self.currency))
            coin_data = r.text
        except:
            print("Can't connect to the server")
            return False

        # Gets the data.
        coin_data = BeautifulSoup(coin_data, 'html.parser')
        coin_data = coin_data.find(id="quote_price")
        coin_data = coin_data.get('data-usd')

        # Saves the data retrieved in a csv file.
        if self.save is True:
            folder = os.path.dirname(os.path.abspath(__file__))
            file = folder + "/data/{}_data.csv".format(self.currency)
            with open(file, "a") as file:
                date = time.strftime("%x-%X")
                price = [date, coin_data]
                write = csv.writer(file)
                write.writerow(price)

        print("{currency}: ${price}".format(
                        currency=self.currency.capitalize(), price=coin_data))

        return coin_data


    def coin_to_dollar(self, number_of_coins):
        """
        This function takes a certain cryptocurrency and exchange
        it to dollars.
        """
        price = self.get_coins()
        coin_in_dollar = number_of_coins * price
        print(coin_in_dollar)
