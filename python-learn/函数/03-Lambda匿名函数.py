# Lambda
def test_lambda(computer):
    temp = computer(1, 2)
    print(temp)
    print(type(temp))


# 用法 lambda 参数 : 方法体（一行代码，隐藏return）
test_lambda(lambda x, y: 1 + 2)
