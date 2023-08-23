from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/Users/olivia/Documents/IT/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com")