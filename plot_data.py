import pandas as pd
import matplotlib.pyplot as plt

btc_data = pd.read_csv("data/bitcoin_data.csv")
eth_data = pd.read_csv("data/ethereum_data.csv")
pd.to_numeric(btc_data["price"])
pd.to_numeric(eth_data["price"])

btc_data["date"] = pd.to_datetime(
    btc_data["date"], format="%m/%d/%y-%H:%M:%S")
eth_data["date"] = pd.to_datetime(
    eth_data["date"], format="%m/%d/%y-%H:%M:%S")

axis = plt.axes()

axis.plot(btc_data["date"], btc_data["price"])
axis.plot(eth_data["date"], eth_data["price"])
axis.set_title("Bitcoin and Ethereum price since " + str(btc_data["date"][0]))
axis.set_ylabel("Price (USD)")
axis.set_xlabel("Date")

plt.show()
