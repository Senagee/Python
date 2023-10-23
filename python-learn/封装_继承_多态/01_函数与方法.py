"""
# 函数：定义在类外部
# 方法：定义在类内部的函数
    区别：方法的形参上需要添加一个关键字 self（java中的this），在调用方法时不需要理会self
    在方法里访问成员变量， 需要使用self
"""


def add(x, y):
    print(x + y)


class Student:
    def add(self, x, y):
        print(x - y)


if __name__ == '__main__':
    add(1, 2)
    stu_1 = Student()
    stu_1.add(1, 2)
