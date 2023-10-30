from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver: WebDriver = webdriver.Chrome()

driver.implicitly_wait(9)
driver.maximize_window()

driver.get("http://unifyng.inventum.co/login")
driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='NgCreator']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Add New']").click()
time.sleep(3)
driver.find_element(By.ID, "formTitle").send_keys("hello")
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Text']").click()

#driver.find_element(By.XPATH, "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]").send_keys("something new")
driver.find_element(By.XPATH, "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]").send_keys("there")
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(5)
