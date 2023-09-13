import time
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://unifyng.inventum.co/login")
driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='AAA Configuration']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Policy Manager']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Add New']").click()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Policy1dd2")
driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Description test")
driver.find_element(By.XPATH, "//input[@id='min_upload_speed']").send_keys("12")
driver.find_element(By.XPATH, "//input[@id='min_download_speed']").send_keys("18")
driver.find_element(By.XPATH, "//input[@id='brst_upload_speed']").send_keys("50")
driver.find_element(By.XPATH, "//input[@id='brst_download_speed']").send_keys("60")
driver.find_element(By.XPATH, "//div[@id='min_upload_speed_dtype']").click()
driver.find_element(By.XPATH, "//li[normalize-space()='MBPS']").click()
driver.find_element(By.XPATH, "//div[@id='brst_upload_speed_dtype']").click()
driver.find_element(By.XPATH, "//li[normalize-space()='MBPS']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()



time.sleep(5)
driver.close()