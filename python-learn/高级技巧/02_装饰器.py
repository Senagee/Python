# 什么是装饰器？
# 创建一个闭包函数， 在内部函数中调用目标函数， 达到不改变原函数的同时， 添加额外的功能


def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    import time
    import random
    print("睡觉中...")
    time.sleep(random.randint(1, 5))


# 常规写法
f1 = outer(sleep)
f1()

# 装饰器的语法糖（简化）
sleep()
