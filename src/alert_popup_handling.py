#Changed to show git commit and push
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By #by is class

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))



driver.maximize_window()

driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME, "cusid").send_keys("53920")

driver.find_element(By.NAME, "submit").submit()

alert = driver.switch_to.alert

alert_message = alert.text

print("ALERT TEXT = ", alert_message)

alert.accept()

driver.quit()