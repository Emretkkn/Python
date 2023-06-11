import pandas as pd
import numpy as np
data = pd.read_csv("nba/salary.csv")
df = pd.DataFrame(data=data)
# 1- İlk 10 kaydı getiriniz.
result = df.head(10)
# 2- Toplam kaç kayıt vardır.
result = len(df.index)
# 3- Tüm oyuncuların toplam maaş ortalaması nedir?
result = df["season17_18"].mean()
# 4- En yüksek maaş ne kadardır ?
result = df["season17_18"].max()
# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df[df["season17_18"]==df["season17_18"].max()]["Player"].iloc[0]

data2 = pd.read_csv("nba/Seasons_Stats.csv")
df2 = pd.DataFrame(data=data2)
# 6- Yaşı 20 ile 25 arasında olan oyuncuların ismini ve oynadıkları takımları azalan şekilde sıralayın.
result = df2[(df2["Age"]>=20) & (df2["Age"]<=25)][["Player","Tm","Age"]].sort_values("Age",ascending=False)
# 7- 'Stephen Curry' isimli oyuncunun oynadığı takım hangisidir.
result = df2[df2["Player"] == "Stephen Curry"]["Tm"]
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = df.groupby("Tm",as_index=True,sort=False).mean("season17_18")
# 9- Kaç farklı takım mevcuttur ?
result = len(df.groupby("Tm").count())
result = df["Tm"].nunique()
# 10- Her takımda kaç oyuncu oynamaktadır ?
result2 = df.groupby("Tm")["Player"].count()
result = df["Tm"].value_counts()
# 11- İsmi İçinde and geçen kayıtları bulunuz ?
df.dropna()
result = df[df["Player"].str.contains("and")]
# OR
def str_find(name):
    if "and" in name.lower():
        return True
    return False
result = df[df["Player"].apply(str_find)]
print(result)
