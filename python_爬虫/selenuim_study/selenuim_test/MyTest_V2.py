# 导包
import _csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login() -> None:
    # 输入url
    url_login = 'https://svr-6-9010.share.51env.net/accounts/login/'

    # 打开被测程序
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
    # 循环读取.csv文件中的测试数据，并执行上传操作
    # 打开csv文件
    f = open("data.csv", 'r')

    # 获取数据句柄（数据的入口）
    rows = _csv.reader(f)

    # 循环读取测试数据
    for row in rows:
        # print(row[0])
        f_name = str(row[0])
        # 没有对应文件，报错
        _driver.find_element(By.NAME, 'qqfile').send_keys("D:\\python\\python-learn\\" + f_name)

    time.sleep(10000)


login()
