from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from settings import kullanici_adi, sifre, driver

# Enters the browser.
tarayici = webdriver.Firefox(executable_path=driver)
tarayici.maximize_window()
tarayici.get("https://twitter.com/i/flow/login")

bekle = WebDriverWait(tarayici, 30)

# Logs in
bekle.until(ec.visibility_of_element_located(
    (By.NAME, "text")
)).send_keys(kullanici_adi)
tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='İleri']").click()
bekle.until(ec.visibility_of_element_located(
    (By.NAME, "password")
)).send_keys(sifre)
tarayici.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']").click()
sleep(3)

# Enters the trends part.
tarayici.find_element(By.XPATH, "//a[@href='/i/trends']").click()
sleep(2)

# Prints trending topics.
"""Trends = tarayici.find_elements(By.XPATH, "//span[@class='css-901oao']")

for trend in Trends:
    print(f"Trendler: {Trends}")

sleep(3)
"""

# Takes a screenshot
tarayici.save_screenshot('C:\\Users\\GRAFIKLAB-18\\Pictures\\PicturesTrends.png')
sleep(2)

# Takes a screenshot of the Trends section 
#tarayici.find_element(By.XPATH, "//div[@class='css-1dbjc4n'").screenshot()

