# threading.Thread(target = 执行的函数名 , args= 以元组的格式传函数的参数, kwargs= 以字典的形式传参)
import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=sing, args=("我要唱歌了",))
    thread_2 = threading.Thread(target=sing, kwargs={"msg": "我要跳舞了"})

    thread_2.start()
    thread_1.start()
