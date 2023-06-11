import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=50)
# print(list)
count = 0
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").string
    year = tr.find("td",{"class":"titleColumn"}).find("span",{"class":"secondaryInfo"}).string.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").string
    count += 1
    print(f"{count} - {title.ljust(50)} Year: {year} Rating: {rating}")