import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv('AAPL.csv')                             #read csv
data['operDate']=pd.DatetimeIndex(data['Date']).month      #append new column operDateDate
data['operYear']=pd.DatetimeIndex(data['Date']).year       #append new column operYear

data.set_index('Date',inplace=True)                        #set new index in current dataframe
data2=data.filter(['Volume','operDate','operYear'])
data2019=data2['2019-01-01':'2019-31-01']
data2019sum=data2019.groupby('operDate')['Volume'].sum()
data2019sum.plot.bar()
plt.show()
#data2019sum.to_csv('APPL2.csv')                               #save to csv
#data2.plot(2,0,kind='bar')

#x = data2019.operDate
#y = data2019.Volume
#plt.bar(x,y)
#plt.show()

