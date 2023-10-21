class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("构造方法执行")


if __name__ == '__main__':
    stu_1 = Student("小刘", 31, "男")
    print(type(stu_1))

