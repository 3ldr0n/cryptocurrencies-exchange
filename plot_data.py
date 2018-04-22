import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

ethereum_data = pd.read_csv('data/ethereum_data.csv')

fig, axis = plt.subplots()

axis.plot(ethereum_data['date'], ethereum_data['price'], 'r')
axis.set_ylabel('Price (Dollars)')
axis.set_xlabel('Date')

doge_data = pd.read_csv('data/dogecoin_data.csv')

axis.plot(doge_data['date'], doge_data['price'], 'r')
plt.show()
