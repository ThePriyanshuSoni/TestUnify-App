
import time
from selenium import webdriver


driver = webdriver.Firefox(executable_path="/home/priyansu/Downloads/geckodriver")
driver.get("http://www.google.com")

time.sleep(5)
driver.close()
