import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

data = pd.read_csv("data/bitcoin_data.csv")
pd.to_numeric(data["price"])

axis = plt.axes()

axis.plot(data["date"], data["price"])
axis.set_xticks([
    data["date"][0],
    data["date"][int(len(data["date"])/2)],
    data["date"][len(data["date"])-1]])

axis.grid()
plt.show()
