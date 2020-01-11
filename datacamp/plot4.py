import pandas as pd 
import matplotlib.pyplot as plt 

ds = pd.read_csv('AAPL.csv',index_col='Date',parse_dates=True)
plt.xlabel("Close Date")
plt.title("APPL Stock Market")
plt.plot()
plt.show()
