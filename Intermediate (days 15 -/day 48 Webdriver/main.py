from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.headless = True

service = Service(executable_path='/snap/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.amazon.com")


driver.quit()