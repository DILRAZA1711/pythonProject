from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import wait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.vodafone.co.uk/broadband')
driver.implicitly_wait(30)
from selenium.webdriver.common.by import By
a = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
#Selenium always automatically quits after a code is finished running. You can add a time.sleep() to keep it open.
time.sleep(2)
b = driver.find_element(By.XPATH,'//*[@id="postcode"]')
b.send_keys('MK170DB')
time.sleep(3)
c = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[2]/form/div/div[2]/div/button').click()
time.sleep(5)
print('Testcase_01:Check availability execution passed successfully')

