from selenium import webdriver

# path = '../chromedriver.exe'

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=option)

url = 'https://www.baidu.com/'
browser.get(url)

content = browser.page_source

print(content)