# 返回多个值
def test_return():
    return 1, "x", 2


x, y, z = test_return()
print(x, y, z)


# 多种传参方式
def test_param1(name, age, sex):
    print(f"名字：{name}, 年龄：{age}, 性别：{sex}")


# 根据位置传参
test_param1("小刘", 18, "男")

# 根据指定参数名传参
test_param1(name="小刘", sex="女", age=17)

# 混合使用
test_param1("小刘", sex="男", age=18)


# 默认值参数
# 注意！！ 设置默认值的参数统一放在后面！
def test_param2(name, age, sex="男"):
    print(f"名字：{name}, 年龄：{age}, 性别：{sex}")


# 不定长参数-- 位置不定长 / 默认转换成元组
def user_info(*args):
    print(args)


user_info("name", "age")
user_info("name", "age", "sex")


# 不定长参数-- 关键字不定长 / 默认转换成字典
def user_info(**args):
    print(args)


user_info(name="xiao", age=19)
user_info(name="xiao", age=19, sex='男')