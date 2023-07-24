import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('http://unifyng.inventum.co/login')
driver.find_element(By.XPATH,"//input[@id='tenant']").send_keys("priyanshu")
driver.find_element(By.XPATH,"//input[@id='tenant']").send_keys(Keys.BACKSPACE)
driver.minimize_window()

time.sleep(5)

