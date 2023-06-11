import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,4), index=["A","B","C","D"], columns=["Column1","Column2","Column3","Column4"])
result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]
# loc["row","column"] => loc["row"] => loc[:,"column"]
# result = df.loc["B"]
# result = type(df.loc["C"])
# result = df.iloc[0]
# result = df.iloc[0:2,:3]
# result = df.iloc[0:1,2:3]
# result = df.iloc[0,2]
# result = df.iloc[[0,1],[2,3]]
df["Column5"] = pd.Series(np.random.rand(4),index=["A","B","C","D"])
df["Column6"] = df["Column1"] + df["Column2"]
# result = df.drop("Column6",axis=1)
# print(result)
# df.drop("Column6",axis=1,inplace=True)
# result = df.loc[:,"Column2"]
# result = df.loc[:,["Column2","Column3"]]
# result = df.loc[:,"Column2":"Column4"]
# result = df.loc[:,:"Column2"]
# result = df.loc["A":"C","Column1":"Column4"]
# result = df.loc["B":"C","Column2":"Column3"]
# result = df.loc[:"B",["Column2","Column4"]]
result = df["Column1"].loc[:]
print(result)