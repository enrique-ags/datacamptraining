import pandas as pd 

family_names = ['Enrique','Iliana','Andres','Sebastian']
family_age = [41,38,12,6]
family_city_born = ['Chihuahua','Mexico DF','Aguascalientes','Aguascalientes']
family_gender = ['Male','Female','Male','Male']
family_labels = ['names','age','city','gender']
family_columns = [family_names,family_age,family_city_born,family_gender]
merged_list = list(zip(family_labels,family_columns))
data = dict(merged_list)

#print(merged_list)

df = pd.DataFrame(data)
print(df)
print(df.info())

