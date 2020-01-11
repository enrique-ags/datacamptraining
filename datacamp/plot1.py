import pandas as pd 
import matplotlib.pyplot as plt 

apple_data = pd.read_csv('AAPL.csv',index_col='Date',parse_dates=True)
apple_data.info()
print(apple_data.head(6))
