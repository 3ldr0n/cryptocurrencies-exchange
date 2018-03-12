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

from bs4 import BeautifulSoup
import requests

class Currency:

    def __init__(self, currency):
        self.currency = currency.lower()

    def get_exchange(self):
        try:
            if self.currency == "euro":
                r = requests.get("http://www.dolarhoje.com/euro")
            else:
                r = requests.get("http://www.dolarhoje.com/")
            data = r.text
        except:
            print("Yo just got damned")

        data = BeautifulSoup(data, 'html.parser')
        data = data.find(id="nacional")['value']

        print("{currency}: R$ {price}".format(
                                currency=self.currency.capitalize(), price=data))
