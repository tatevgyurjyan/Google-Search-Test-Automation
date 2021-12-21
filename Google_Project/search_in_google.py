from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
import time
import re


logging.basicConfig(filename="google_log.txt",
                    format="%(asctime)s: - %(levelname)s:%(message)s",
                    level=logging.INFO)

driver = webdriver.Chrome(
    executable_path="/home/tatevik/Desktop/QA_Automation/Drivers/chromedriver")

driver.maximize_window()
driver.get("https://google.com")

# Saying ok to cookies
agree_btn = driver.find_element(By.XPATH, "//div[text()='Ich stimme zu']")
agree_btn.click()
time.sleep(2)

search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("qwallity")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    data = driver.find_elements(By.TAG_NAME, "a")

time.sleep(2)
logging.info(f"The overall number of finden links is {len(data)}")

try:
    results = []
    for link in data:
        href = link.get_attribute("href")
        if re.findall(r"\bqwallity\b", str(href), re.MULTILINE):
            results.append(href)

except Exception as e:
    logging.error(e)

logging.info(f"Links containing word 'qwallity' are {len(results)}")

with open("qwallity_links.txt", "w") as file:
    for href in results:
        file.write(href + "\n")

driver.close()
