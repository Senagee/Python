# 定义函数
# def say_hi():
#     print("hi")
#
#
# say_hi()

#
# def add(x, y):
#     return x + y
#
#
# print(f"{add(1, 2)}")


num = 200
def test_1():
    global num
    num = 100
    print(num)
test_1()
print(num)
