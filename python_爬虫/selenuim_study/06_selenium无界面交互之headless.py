from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# {  headless的基本配置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# path是你自己Chrome的exe文件位置
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
# }
browser = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com/'

browser.get(url)

# 保存界面快照
# browser.save_screenshot("baidu.png")

browser.find_element(By.ID, "kw") .send_keys("吴雯雯")

browser.save_screenshot("baidu.png")
