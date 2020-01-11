import pandas as pd 

cities=['austin','dallas','austin','dallas']
signups=[7,12,3,5]
visitors=[139,237,326,456]
weekdays=['Sun','Sun','Mon','Mon']
list_labels=['cities','signups','visitors','weekdays']
list_cols=[cities,signups,visitors,weekdays]
zipped=list(zip(list_labels,list_cols))
print(zipped)

users = pd.DataFrame(zipped)
print(users)
