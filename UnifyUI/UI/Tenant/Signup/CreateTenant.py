import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


serv_obj = Service('/home/priyanshusoni/PycharmProjects/pythonProject2/chromedriver')
driver = selenium.webdriver.Chrome(service=serv_obj)

driver.get("http://unifyng.inventum.co/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[normalize-space()='login']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='SignUp?']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Purchase']").click()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("priyanshudd.soni@test.net")
driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Priyanshudd")
driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("Sonidd")
driver.find_element(By.XPATH,"//input[@id='mobile_no']").send_keys("9956400901")
driver.find_element(By.XPATH,"//input[@id='organisation_name']").send_keys("Inventumdd")
driver.find_element(By.XPATH,"//input[@id='city']").send_keys("Noida")
driver.find_element(By.XPATH,"//input[@id='state']").send_keys("UP")
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("India")
driver.find_element(By.XPATH,"//input[@id='pincode']").send_keys("201301")
driver.find_element(By.XPATH,"//input[@id='shipping_address']").send_keys("4 Privet Drive")
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("Surrey 56")
driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()

test1 = driver.find_element(By.XPATH, '//iframe[@class="razorpay-checkout-frame"]')

driver.switch_to.frame(test1)
driver.find_element(By.XPATH,'//div[text()="UPI / QR"]').click()
driver.find_element(By.ID,"new-vpa-field-upi").click()
a = driver.find_element(By.ID,"vpa-upi")
a.send_keys("test@icici")
time.sleep(5)
a.send_keys(Keys.ENTER)

#driver.find_element(By.XPATH,"//button[@id='redesign-v15-cta']").click()
time.sleep(10)
driver.switch_to.default_content()
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='tenant_name']").send_keys("jawaaa")
driver.find_element(By.XPATH,"//button[normalize-space()='verify']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
print("Unify Test Pass")
time.sleep(10)