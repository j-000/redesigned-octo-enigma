from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:8000')

assert 'Django' in driver.title

