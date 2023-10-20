"""
try:
    可能发生异常的代码
except[异常类 as e（别名）]:
    发生异常后，执行的代码
[else:]
    未发生异常，执行的代码
[finally:]
    不管发不发生异常，都会执行的代码

"""
try:
    f = open("D:/python/python-learn/IO/except_test.text", "r", encoding="UTF-8")
except ZeroDivisionError as e:
    print(f"出现{e}错误")
except FileNotFoundError as e:
    print(f"出现{e}错误")

    1 / 0