"""
    多继承:
        当继承的多个父类中有相同的属性或方法时，谁优先级高呢？？
        答案是 先继承的优先级高
        ！！！当继承的多个父类中有相同的属性或方法时优先使用优先级高的父类的属性或方法）


    复写（覆盖）：
        复写父类的属性或方法
            必须与父类的属性或方法重名并且方法的参数列表一致
        调用父类的属性或方法：
            super().属性
            super().方法(self,参数列表)
            父类名.属性
            父类名.方法(参数列表)
    pass关键字：

"""
from random import random


class Phone:

    def __init__(self, ID, preducer):
        self.ID = ID
        self.preducer = preducer

    def call_by_4G(self):
        print("4G通话")


class Phone2022(Phone):
    face_id = True

    def __init__(self):
        super().__init__(1, "ITCAST")
    def call_by_5G(self):
        print("5G通话")


my_phone = Phone2022()

my_phone.call_by_4G()
my_phone.call_by_5G()
