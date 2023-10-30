from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.binary_location = "/root/chromedriver-linux64/chromedriver"


driver = webdriver.Chrome(executable_path="/root/chromedriver-linux64/chromedriver")
driver.get('https://www.example.com')

print("hello python")

driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

chrome_driver_path = "/root/chromedriver-linux64/chromedriver"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.google.com')

print("Hello There, Now its working...:)")
driver.quit()
_______________________________________________________________________

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/usr/bin/google-chrome"  # Path to your Chrome binary

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="/root/chromedriver-linux64/chromedriver",chrome_options=chrome_options)



driver.quit()
