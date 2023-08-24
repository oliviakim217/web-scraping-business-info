from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/Users/olivia/Documents/IT/chromedriver")
driver = webdriver.Chrome(service=service)

for page in range(11, 12):
    driver.get("https://kyocharocalgary.com/yellowpage?page=" + str(page))
    print("page" + str(page))
    
    for i in range(1, 51):
        # Click on business name
        xpath = '//*[@id="fboardlist"]/div/table/tbody/tr[' + str(i) + ']/td[2]/a'
        business_name = driver.find_element(By.XPATH, xpath)
        business_name.click()
        time.sleep(1)
        
        # Print content
        content = driver.find_element(By.ID, "bo_v_con").text
        print(content)
        print(str(i) + "------------")
        time.sleep(1)

        # Return to previous page
        driver.back()
        time.sleep(1)


# driver.close()
