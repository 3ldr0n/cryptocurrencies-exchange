import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

data = pd.read_csv('data/ethereum_data.csv')

fig, axis = plt.subplots()

axis.plot(data['date'], data['price'], 'r')
axis.title("Ethereum")
axis.set_ylabel('Price (Dollars)')
axis.set_xlabel('Date')
plt.show()
