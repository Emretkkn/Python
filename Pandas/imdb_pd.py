import pandas as pd
import numpy as np
df = pd.read_json("imdb_data.json",encoding="UTF-8",lines=True)
# 1- Dosya hakkında bilgiler
# result = df.columns
# result = df.info()
# 2- İlk 5 kaydı gösterin.
result = df.head()
# 3- İlk 10 kaydı gösterin.
result = df.head(10)
# 4- Son 5 kaydı gösterin.
result = df.tail()
# 5- Son 10 kaydı gösterin.
result = df.tail(10)
# 6- Sadece movie_name kolonunu alın.
result = df["movie_name"]
# 7- Sadece movie_name kolonunu içeren ilk 5 kaydı alın.
result = df["movie_name"].head()
# 8- Sadece movie_name ve rating kolonunu içeren ilk 5 kaydı alın.
result = df[["movie_name","rating"]].head()
# 9- Sadece movie_name ve rating kolonunu içeren son 7 kaydı alın.
result = df[["movie_name","rating"]].tail(7)
# 10- Sadece movie_name ve rating kolonunu içeren ikinci 5 kaydı alın.
result = df[5:10][["movie_name","rating"]].head()
# 11- Sadece movie_name ve rating kolonunu içeren ve imdb puanı 8.0 üzerinde olan kayıtlardan ilk 50 tanesini alın.
result = df[(df["rating"] > 8.0)][["movie_name","rating"]].head(50)
# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df["movie_year"] >= 2014) & (df["movie_year"] <= 2015)]["movie_name"]
# 13- Türü Fantastik olan ya da imdb_puanı 8 ile 9 arasındaki filmleri listeleyiniz.
result = df[("Crime" in df["genre"]) | ((df["rating"] > 8) & (df["rating"] < 9))][["movie_name","rating","genre"]]















print(result)