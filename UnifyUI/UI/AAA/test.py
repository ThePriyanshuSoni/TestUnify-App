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
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(3)



element = driver.find_element(By.XPATH, "//div[contains(text(),'Please check the form carefully for errors!')]")

# Check if the element contains the text "Welcome"
search_text = "Please check the form carefully for errors!"
if search_text in element.text:
    print(f"The element contains the {search_text}.")
else:
    print(f"The element does not contain the search text: {search_text}.")

time.sleep(5)
driver.close()


