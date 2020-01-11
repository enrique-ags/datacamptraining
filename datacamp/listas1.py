import pandas as pd                                    #import library pandas

lista1 = ['enrique','iliana','andres','sebastian']     # create list1
#print("imprimiendo lista1 " , lista1)
lista2=[41,38,12,6]                                    #create list2 
lista3 = list(zip(lista1,lista2))                      #zip function, merged two list  
print(lista3)                                          #print the new merged list

#list4 = dict(lista3)                                    #create dictionary using list3, check output
#print(list4)                                           #print list4

#df = pd.DataFrame(list4)                                #create data frame from dictionary
#print(df)