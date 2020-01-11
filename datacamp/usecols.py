import pandas as pd 
cols = ['Date','Open','Volume']
data = pd.read_csv('AAPL.csv', usecols=cols)
data.to_csv('usecols.csv')
