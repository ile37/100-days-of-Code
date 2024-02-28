from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True

service = Service(executable_path='/snap/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

input("press any key to continue")
print("bot will run for 5 minutes")

def upgrade(store):
    items = store.find_elements(By.TAG_NAME, "div")
    for item in reversed(items):
        if item.get_attribute("class") == "product unlocked enabled":
            item.click()
            break

def cookie_bot():

    cookie = driver.find_element(By.ID, "bigCookie")
    store = driver.find_element(By.ID, "store")

    start_time = time.time()
    runtime = time.time() + 60 * 5
    store_buy_time = time.time() + 5

    while start_time < runtime:
        cookie.click()

        if time.time() >= store_buy_time:
            upgrade(store)
            store_buy_time = time.time() + 5


cookie_bot()


driver.quit()