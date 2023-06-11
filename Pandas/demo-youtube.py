import pandas as pd
import numpy as np
data = pd.read_csv("youtube/USvideos.csv")
df = pd.DataFrame(data=data)
# # 1- İlk 10 kaydı getiriniz.
# result = df.head(10)
# # 2- İkinci 5 kaydı getiriniz.
# result = df[5:10].head()
# # 3- Datasette bulunan kolon isimleri ve sayısını bulunuz.
# result = df.columns
# result = len(df.columns)
# # 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyin
# # (thumbnail_link,comments_disabled,ratings_disabled)
# result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled"],axis=1)
# # 5- Beğenme(likes) ve beğenmeme(dislikes) ortalamalarını bulunuz.
# result = df[["likes","dislikes"]].mean()
# # 6- İlk 50 videonun like ve dislike kolonlarını getiriniz.
# result = df.head(50)[["likes","dislikes"]]
# # 7- En çok görüntülenen(views) video hangisidir ?.
# result = df[df["views"].max() == df["views"]][["title","views"]].iloc[0]
# # 8- En düşük görüntülenen(views) video hangisidir ?.
# result = df[df["views"].min() == df["views"]]["title"].iloc[0]
# # 9- En fazla görüntülenen(views) ilk 10 video hangisidir ?.
# result = df.sort_values("views",axis=0,ascending=False).head(10)["title"]
# # 10- Kategoriye göre beğeni ortalamalarını sıralı bir şekilde getiriniz.
# result = df.groupby("category_id").mean(numeric_only=True).sort_values("likes")["likes"]
# # 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)
# # 12- Her kategoride kaç video vardır ?
# result = df["category_id"].value_counts()
# # 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# df["title_length"] = df["title"].apply(len)
# result = df.head(10)
# # 14- Her video için kullanılan tag sayısını yeni bir kolonda gösteriniz
df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))
# 15- En popüler videoları like dislike oranına göre listeleyiniz.

def likedislikeorani(df):
    likeList = list(df["likes"])
    dislikeList = list(df["dislikes"])

    liste = list(zip(likeList,dislikeList))    
    oranlistesi = []
    for like,dislike in liste:  
        if like + dislike == 0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    return oranlistesi
df["like_rate"] = likedislikeorani(df=df)
result = df.sort_values("like_rate",ascending=False)[["title","likes","dislikes","like_rate"]]
print(result)