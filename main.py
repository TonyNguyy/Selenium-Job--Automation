from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

ACCOUNT_EMAIL = "tonynguyy@gmail.com"
ACCOUNT_PASSWORD ="#"


chrome_webdriver = "/Users/tonynguyen/Desktop/ChromeDriver/chromedriver"
driver = webdriver.Chrome(chrome_webdriver)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3623654673&f_E=1%2C2&f_TPR=r604800&geoId=100025096&keywords=developer&location=Toronto%2C%20Ontario%2C%20Canada&refresh=true&start=50")



sign_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_button.click()

time.sleep(5)

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

time.sleep(20)


driver.close()
