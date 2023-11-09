"""
自动化测试脚本：上传多媒体文件

# 访问地址：url_login = 'https://svr-6-9010.share.51env.net/accounts/login'
# 上传地址：url_up = 'https://svr-6-9010.share.51env.net/upload'
"""

# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login() -> None:
    # 输入url
    url_login = 'https://svr-6-9010.share.51env.net/accounts/login/'

    # 打开被测程序
    _driver = webdriver.Chrome()
    _driver = webdriver.Chrome()
    _driver.get(url_login)

    # 导入测试数据（登录）
    _driver.find_element(By.ID, "id_login").send_keys("51testing")
    _driver.find_element(By.ID, "id_password").send_keys("atstudybwf")
    _driver.find_element(By.ID, "id_captcha_1").send_keys("passed")
    _driver.find_element(By.CLASS_NAME, "primaryAction").click()

    # 执行操作（上传）
    url_upload = 'https://svr-6-9010.share.51env.net/upload'
    _driver.get(url_upload)
    _driver.find_element(By.NAME, 'qqfile').send_keys("D:\\python\\python-learn\\selenuim_test\\csvATM.py")

    time.sleep(10000)


login()
