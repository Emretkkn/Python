import pandas as pd
import numpy as np
def kupal(x):
    return x**3

kareal = lambda x:x**2 # Lambda expression

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,20,45,56],
    "Column3":["abeeb","bcaa","ad","cba","dea"]
}
df = pd.DataFrame(data,columns=["Column1","Column2","Column3"])
result = df["Column2"].unique()
result = df["Column3"].nunique()
result = df["Column2"].value_counts()
result = df["Column1"].apply(kupal)
result = df["Column1"].apply(kareal)
result = df["Column1"].apply(lambda x:x**4)
result = df["Column3"].apply(len)
df["Kareler"] = df["Column1"].apply(lambda x:x*x)
df["Kupler"] = df["Column1"].apply(kupal)
result = len(df.columns)
result = df.info
result = df.sort_values("Column2")
result = df.sort_values("Column2",ascending=False)
# print(result)

data = {
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir":[20,30,15,14,32,42,12,36,52]
}
df = pd.DataFrame(data,columns=["Ay","Kategori","Gelir"])
pivot = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")
print(df)
print(pivot)