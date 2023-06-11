import requests
from bs4 import BeautifulSoup
class Scraping:
    def __init__(self):
        self.url = "https://www.pttavm.com/arama/cep-telefonu"
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html,"html.parser")
        self.titleList = []
        self.priceList = []
    def getTitle(self):
        findTitle = self.soup.find_all("span",{"class":"product-list-box-container-info-name"})
        for i in findTitle:
            title = i.text.strip()
            self.titleList.append(title)
        self.length = len(self.titleList)
    def getPrice(self):
        findPrice = self.soup.find_all("div",{"class":"price-box-price"})
        for i in findPrice:
            price = i.text.strip()
            self.priceList.append(price)
    def printTitleandPrice(self):
        for i in range(self.length):
            print(f"Product Name: {self.titleList[i]} Price: {self.priceList[i]}")
            
scrapeObject = Scraping()
scrapeObject.getPrice()
scrapeObject.getTitle()
scrapeObject.printTitleandPrice()