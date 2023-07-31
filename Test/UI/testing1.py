from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://unifyng.inventum.co/login")
driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Settings']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Site Settings']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Billing Frequency']").click()

time.sleep(2)