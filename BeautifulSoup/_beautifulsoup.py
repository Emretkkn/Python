html_content = r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project</title>
</head>
<body>
    <div class="group1" id="header">
        <h1>List</h1>
    </div>
    <div class="group2" id="list">
        <ul>
            <li>Once</li>
            <li>Second</li>
            <li>Third</li>
        </ul>
    </div>
    <img src="C:\Users\emret\Pictures\Screenshots\image.png" alt="">
    <a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example2.com/lacie" class="sister" id="link2">Lacie</a>
    <a href="http://example3.com/tillie" class="sister" id="link3">Tillie</a>
</body>
</html>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content,"html.parser")
result = soup.prettify() # Html dökümanını düzenleme işlemi yapar.
a = soup.title
b = soup.head
c = soup.body
# print(a)

result = soup.title.name # Etiket ismini getirir.
result2 = soup.title.string # İçindeki stringi getirir.
result = soup.h1.string
liste = soup.find_all('li')
result = soup.find_all("div")[1].ul.find_all("li")
result = soup.find_all("div")[1].findChildren()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
result = soup.find_all("a")
# for i in result:
#     print(i)
for link in result:
    print(link.get("href")) # etiket içindeki attributelara ulaşmak için kullanılır.

# print(result)
