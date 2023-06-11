import pandas as pd
import numpy as np
customers = {
    "CustomerId":[1,2,3,4],
    "FirstName":["Emre","Rümeysa","Mehmet","Tuğba"],
    "LastName":["Tekin","Koyun","Demiraslan","Aktaş"]
}
orders = {
    "OrderId":[10,11,12,13],
    "CustomerId":[1,2,5,8],
    "OrderDate":["2015-06-27","2013-03-06","2018-11-14","2011-05-18"]
}
df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])
result = pd.merge(df_customers,df_orders,how="inner")
result = pd.merge(df_customers,df_orders,how="left")
result = pd.merge(df_customers,df_orders,how="right")
result = pd.merge(df_customers,df_orders,how="outer")
# print(df_customers)
# print(df_orders)
# print(result)

customersA = {
    "CustomerId":[1,2,3,4],
    "FirstName":["Emre","Rümeysa","Mehmet","Tuğba"],
    "LastName":["Tekin","Koyun","Demiraslan","Aktaş"]
}
customersB = {
    "CustomerId":[5,6,7,8],
    "FirstName":["Zeynep","Abdullah","İsmet","Oktay"],
    "LastName":["Akçay","Güldoğan","Yağlı","Özcan"]
}
df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])
result = pd.concat([df_customersA,df_customersB]) # axis = 0 => Satıra göre concat
result = pd.concat([df_customersA,df_customersB],axis=1) # axis = 1 => Sütuna göre concat
print(result)