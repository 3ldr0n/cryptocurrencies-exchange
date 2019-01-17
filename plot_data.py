import sys

import pandas as pd
import matplotlib.pyplot as plt

crypto = sys.argv[1]

data = pd.read_csv("data/{}_data.csv".format(crypto))
pd.to_numeric(data["price"])

data["date"] = pd.to_datetime(
    data["date"], format="%m/%d/%y-%H:%M:%S")

axis = plt.axes()

axis.plot(data["date"], data["price"])
axis.set_title("{} price since {}".format(crypto, data["date"][0]))
axis.set_ylabel("Price (USD)")
axis.set_xlabel("Date")

plt.show()
