
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('https://juejin.cn/pins/hot')
    element = driver.find_elements(By.CLASS_NAME, 'content-box')
    for item in element :
        print(item.text)
        print("_____________")
    driver.quit()
