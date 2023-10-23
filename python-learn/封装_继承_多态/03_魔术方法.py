# 魔术方法（Python内置方法）
"""
    __init__():  构造方法
    __str__():   toString方法
    __lt__():    两个对象无法进行 <、>  的比较，但实现了这个方法就可以
    __le__():    两个对象无法进行 <=、>=  的比较，但实现了这个方法就可以
    __eq__():    两个对象是否相等（默认比较内存地址），可以设置这两个对象相等的条件
"""
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Studnet[name: {self.name}, age: {self.age}, sex: {self.sex}]"

    def __eq__(self, other):
        # return self == other
        return self.age == other.age
if __name__ == '__main__' :
    stu_1 = Student("小刘", 18, "男")
    stu_2 = Student("小刘", 18, "男")
    print(stu_1 == stu_2)


