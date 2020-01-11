#to display 1 bar char
import pandas as  pd
import matplotlib.pyplot as plt 

df=pd.read_csv('AAPL.csv',index_col='Dates',parse_dates=True)
x=df.index
y=df.Volume
plt.xlabel('Date Volume')
plt.ylabel=("APPL Volume")
plt.title("APPL Stock Market")
plt.bar(x,y)
plt.show()




