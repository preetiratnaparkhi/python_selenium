
import time
from selenium.webdriver.common.by import By #by is class

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
browser="chrome"
if browser.lower()=="chrome":


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)



driver.quit()

driver.get("https://www.icicibanks.com/")

time.sleep(5)

try:
    driver.find_element_by_id("push-modal-close").click()
except Exception:
    pass

time.sleep(5)

driver.quit()
