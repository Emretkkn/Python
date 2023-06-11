from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup
import pyautogui
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.actionChains = ActionChains(self.browser)
        self.usernameList = []
    def login(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(2)
        self.browser.maximize_window()
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(f"{self.username}")
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(f"{self.password}",Keys.ENTER)
        time.sleep(5)

    def getFollowers(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        self.browser.find_element(By.XPATH,f"//a[@href='/{username}/followers/']").click()

        time.sleep(1)
        css_text = " xl565be x1m39q7l x1uw6ca5 x2pgyrj".replace(" ",".")
        list = self.browser.find_elements(By.CSS_SELECTOR,f"{css_text}")
        for i in list:
            if 'takipçi' in i.text:
                a = i.text.split()
                followerNumber = a[0]
        count = int(int(followerNumber)/10) 
        for i in range(count):
            usernames = self.browser.find_elements(By.XPATH,"//div[@role='button']/div/div/div/div[2]/div/div/span/span/div/div/div/a/span/div")
            pyautogui.moveTo(960,540,0.5)
            pyautogui.scroll(-1000)
            time.sleep(1)
            print(len(usernames))
        for i in usernames:
            self.usernameList.append(i.text) 
        with open(f"C:\\Users\\emret\\OneDrive - Dokuz Eylül Üniversitesi\\Masaüstü\\{username}.txt","w",encoding="UTF-8") as file:
            for i in self.usernameList:
                file.write(i+"\n")


            

instaobject = Instagram(username,password)

while True:
    choosen = int(input("1- Kullanıcı girişi yap\n2- Takipçi Listesi Oluştur\n3- Exit\nLütfen seçim yapınız: "))
    if choosen == 1:
        name = input("Kullanıcı adınızı yazınız: ").strip()
        password = input("Şifrenizi yazınız: ").strip()
        instaobject.login(username=name,password=password)
    elif choosen == 2:
        secilmis = input("Lütfen listesini almak istediğiniz kullanıcı adını yazınız: ").strip()
        instaobject.login()
        instaobject.getFollowers(username=secilmis)        
    elif choosen == 3:
        break
    else:
        break

