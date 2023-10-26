# 什么是闭包？（其实就是定义private的变量）
    # 定义双层嵌套函数， 内层函数可以访问外层函数的变量
    # 将内层函数作为外层函数的返回值， 此内层函数就是闭包函数

# 好处
    # 不需要定义全局变量， 也可以让函数持续的访问和修改外部变量
    # 闭包函数引用的外部变量是外层函数的变量， 作用域只能被闭包函数访问和修改
# nonlocal关键字
    # 当闭包函数需要修改外层函数的变量时，需要在闭包函数体中使用nonlocal关键字修饰外层变量
    # 访问时不需要

def outer(out_var):

    def inner(in_var):
        nonlocal out_var
        out_var += 1
        print(f"out_var: {out_var}, in_var: {in_var}")
    return inner


f1 = outer(10)
f1(20)
f1(20)
