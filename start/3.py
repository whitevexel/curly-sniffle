import time 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/")

url = driver.current_url
print("URL -", url)
assert url == "https://en.wikipedia.org/", "Error in url"

current_title = driver.title
print("Title :", current_title)
assert current_title == "Wikipedia", "Error in Title"


time.sleep(3)
