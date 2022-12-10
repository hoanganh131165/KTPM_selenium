from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://www.facebook.com/')


driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"firstname").send_keys("anh")
driver.find_element(By.NAME ,"lastname").send_keys("Hoang")
driver.find_element(By.NAME ,"reg_email__").send_keys("HoangAnh2002@gmail.com")
Day=Select(driver.find_element(By.ID,"day"))
Day.select_by_visible_text("10")
month=Select(driver.find_element(By.ID,"month"))
month.select_by_visible_text("Dec")
year=Select(driver.find_element(By.ID,"year"))
year.select_by_visible_text("2000")

driver.find_element(By.XPATH,"//lable[text()='Femal]").click()
driver.find_element(By.NAME,"websubmit").click()
driver.close()