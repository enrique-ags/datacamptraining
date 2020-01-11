import pandas as pd 
import matplotlib.pyplot  as plt

data = pd.read_csv('AAPL.csv',index_col='Date',parse_dates=True)

close_arr = data['Close'].values
plt.plot(close_arr)
plt.title="APPLE Stock Market"
plt.xlabel="Days"
plt.ylabel="Closed"
plt.show()
