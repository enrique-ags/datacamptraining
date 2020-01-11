import pandas as pd
csv='/home/devops/Desktop/datacamp/addresses.csv'

data = pd.read_csv(csv)
print(data)

labels=['name','last_name','Address','City','State','ZIP']
data2 = pd.read_csv(csv,header=0,names=labels)
print("Data with headers")
print(data2)
