from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://vnexpress.net/')
article = driver.find_elements(By.CSS_SELECTOR,'article.item-news')
for ar in article:
    try :
        title  = ar.find_element(By.TAG_NAME, 'h3').text
        link = ar.find_element(By.CSS_SELECTOR , 'h3.title-news > a ').get_attribute('href')
        description = ar.find_element(By.TAG_NAME , 'p').text
        print(title)
        print(link)
        print(description)

    except:
        print('loi')
print('======')
driver.close()

