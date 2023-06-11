import pandas as pd
# df = pd.DataFrame()
# df = pd.DataFrame([0,1,2,3,4])
# df = pd.DataFrame([["Emre",50],["Rümeysa",60],["Ahmet",70],["Mahmut",80]])
data = [["Emre",50],["Rümeysa",60],["Ahmet",70],["Mahmut",80]]
dict = {"Name":["Emre","Ahmet","Rumeysa","Ali"],"Grade":[50,60,70,80]}
# df = pd.DataFrame(dict,index=["232","233","234","235"])
dict_list = [
    {"Name":"Emre","Grade":50},
    {"Name":"Ahmet","Grade":60},
    {"Name":"Rumeysa","Grade":70},
    {"Name":"Mahmut","Grade":80},
]
df = pd.DataFrame(dict_list,index=["232","233","234","235"])
# df = pd.DataFrame(data,columns=["Names","Grades"],index=[1,2,3,4])
print(df)
# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])
# data = dict(bananas = s1,apples = s2)
# df = pd.DataFrame(data)
# print(df)
