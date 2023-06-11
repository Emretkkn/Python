import pandas as pd
import numpy as np
data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data,index=["a","c","e","f","h"],columns=["Column1","Column2","Column3"])
df = df.reindex(["a","b","c","d","e","f","g","h"])
result = df.drop("Column1",axis=1)
result = df.drop(["Column1","Column2"],axis=1)
result = df.drop("a",axis=0)
result = df.drop(["a","b"],axis=0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["Column1"].isnull().sum()
newColumn = [np.nan,12,np.nan,21,np.nan,76,np.nan,43]
df["Column4"] = newColumn
result = df["Column1"].isnull()
result = df[df["Column1"].isnull()][["Column3","Column4"]]
result = df[df["Column1"].notnull()]["Column1"]
result = df["Column1"].notnull().argmax()
result = df.dropna() # axis = 0 => Satır
result = df.dropna(axis=1) # axis = 1 => Sütun
result = df.dropna(axis=0,how="any")
result = df.dropna(axis=0,how="all")
result = df.dropna(subset=["Column1","Column2"],how="all")
result = df.dropna(subset=["Column3","Column4"],how="any")
result = df.dropna(thresh=2) # en az sayıda normal veri
result = df.dropna(thresh=4)
result = df.fillna(value="No input")
result = df.isnull().sum()
def ortalama(df):
    value_sum = df.sum().sum()
    size = df.size
    null_size = df.isnull().sum().sum()
    mean = value_sum/(size - null_size)
    return mean

result = df.fillna(value=ortalama(df=df))
print(result)