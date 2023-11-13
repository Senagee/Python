from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

browser = webdriver.Chrome()

browser.get(url)

# 根据id进行定位
# button = browser.find_element(By.ID, "su")
# print(button)

# 根据name定位
# button = browser.find_element(By.NAME, "wd")
# print(button)

# 根据标签名进行定位
# button = browser.find_element(By.TAG_NAME, "input")
# print(button)

# 根据xpath语法进行定位
# button = browser.find_element(By.XPATH, "//input[@id='su']")
# print(button)

# # 根据bs4语法进行定位
# button = browser.find_element(By.CSS_SELECTOR, "#su")
# print(button)

# 根据文本链接进行定位
button = browser.find_element(By.LINK_TEXT, "新闻")
print(button)
