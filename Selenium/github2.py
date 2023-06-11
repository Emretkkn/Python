from githubUserInfo import password,username
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.repos = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        username_input = self.browser.find_element(By.XPATH,'//*[@id="login_field"]')
        password_input = self.browser.find_element(By.XPATH,'//*[@id="password"]')
        username_input.send_keys(f"{self.username}")
        password_input.send_keys(f"{self.password}",Keys.ENTER)
        time.sleep(3)
    def goRepos(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(4)
        items = self.browser.find_elements(By.CSS_SELECTOR,".col-12.d-flex")
        for i in items:
            self.repos.append(i.find_element(By.TAG_NAME,"a").text)        
        print(self.repos)
object = Github(username,password)
object.signIn()
object.goRepos()