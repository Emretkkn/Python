from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Twitter:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self,username,password):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input[autocomplete=username]").send_keys(f"{username}",Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,"input[name=password]").send_keys(f"{password}",Keys.ENTER)
        time.sleep(3)
    
    def searchPerson(self,kullanici_adi):
        self.browser.get("https://twitter.com/home")
        time.sleep(3)
        self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input').send_keys(f"{kullanici_adi}")
        time.sleep(2)
        check = self.browser.find_elements(By.CSS_SELECTOR,"div[role=button] span")
        for btn in check:
            if btn.text == f"@{kullanici_adi} adlı kullanıcıya git":
                btn.click()
                time.sleep(5)
            else:
                continue
    
    def getUserTweets(self):
        username = "Rumistow"
        self.browser.get(f"https://twitter.com/{username}")
        time.sleep(2)
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        loopcount = 0
        tweetList = []
        while True:
            if loopcount > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            tweetLists = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
            for i in tweetLists:
                tweetList.append(i.text)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopcount += 1 

    def getFollowers(self):
        username = input("Lütfen Takipçilerini dosyalamak istediğiniz kullanıcı adını yazınız: ")
        self.browser.get(f"https://twitter.com/{username}/followers")
        time.sleep(2)
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        nameList = []
        while True:
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            Liste = self.browser.find_elements(By.XPATH,"//div[@data-testid='UserCell']/div/div[2]/div/div/div/div/a/div/div")
            for i in Liste:
                nameList.append(i.text)
            if last_height == new_height:
                break
            last_height = new_height
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in nameList:
                file.write(item+"\n")
twiter = Twitter()
twiter.login(username,password)
twiter.getFollowers()