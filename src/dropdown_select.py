import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By #by is class

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("http://demo.guru99.com/test/newtours/register.php")

drpCountry = Select(driver.find_element(By.NAME, "country"))
time.sleep(1)
drpCountry.select_by_visible_text("ANTARCTICA")

time.sleep(1)
drpCountry.select_by_index(3)
time.sleep(2)

# Selecting Items in a multiple select elements

driver.get("http://jsbin.com/osebed/2")

fruits = Select(driver.find_element(By.ID, "fruits"))

assert fruits.is_multiple
assert frui

fruits.select_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Apple")
time.sleep(2)
fruits.select_by_index(1)

driver.quit()

