from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/user/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1366,768)

driver.find_element(By.NAME, "username").click()
driver.find_element(By.NAME, "password").click()
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "otp-code").click()
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.ID, "cards-overview-index").click()
element = driver.find_element(By.CSS_SELECTOR, "#card-details-ownbank-10068 .card-set-pin > .link-title")
driver.find_element(By.CSS_SELECTOR, "#card-details-ownbank-10068 .card-set-pin > .link-title").click()
driver.find_element(By.ID, "pin").click()
driver.find_element(By.ID, "pin").send_keys("5555")
driver.find_element(By.ID, "set-pin").click()
driver.find_element(By.ID, "deposits-index").click()
driver.find_element(By.ID, "loans-index").click()
driver.find_element(By.ID, "accounts").click()
driver.find_element(By.ID, "overview").click()
driver.find_element(By.ID, "externaltraderoom-index").click()
driver.find_element(By.XPATH, "//*[@id='logout-button']/span").click()
