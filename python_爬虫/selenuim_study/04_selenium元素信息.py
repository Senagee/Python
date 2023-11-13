from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

browser = webdriver.Chrome()

browser.get(url)

ele = browser.find_element(By.ID, "su")
# 获取对应标签的属性值
print(ele.get_attribute("class"))

# 获取标签中的文本
print(ele.text)

# 获取标签名
print(ele.tag_name)