import pandas as pd
import numpy as np
personeller = {
    'Çalışan':["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    'Departman':["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Kadıköy"],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(personeller)
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# semtler = df.groupby("Semt")
# for name,group in semtler:
#     print(name)
#     print(group)

# departman = df.groupby("Departman")
# for name,group in departman:
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Tuzla")
result = df.groupby("Departman").get_group("Bilgi İşlem")
result = df.groupby("Departman").sum(["Maaş","Yaş"])
result = df.groupby("Departman").mean(["Maaş","Yaş"])
result = df.groupby("Semt").mean(["Yaş","Maaş"])
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].max()["Bilgi İşlem"]
result = df.groupby("Departman")[["Maaş","Yaş"]].agg([np.sum,np.mean,np.max,np.min]).loc["İnsan Kaynakları"]
print(result)