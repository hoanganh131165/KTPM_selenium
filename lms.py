import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://lms.ou.edu.vn/')
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,'main-btn').click()
driver.find_element(By.CLASS_NAME,'login100-form-btn').click()
userType = Select(driver.find_element(By.NAME,'form-usertype'))
userType.select_by_index(0)

with open('taikhoan.csv','r', newline = '') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

driver.find_element(By.CSS_SELECTOR,'m-loginbox-submit-btn').click()
course = driver.find_element(By.CSS_SELECTOR,'dashboard-card-deck.dashboard-card')
for c in course:
    print(c.text)
driver.close()
