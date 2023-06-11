from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://www.github.com"
driver.get(url)

searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
time.sleep(2)
searchInput.send_keys("Python",Keys.ENTER)
time.sleep(2)
result = driver.find_elements(By.CSS_SELECTOR, ".f4.text-normal a")
for i in result:
    print(i.text)  

