# python中对文件的操作 ： 打开、读写、关闭
# open("文件的路径", "限制操作", 编码.....)
#       r = 只读
#       w = 写（覆盖写）
#       a = 追加写入

"""
    read(num)：
            num : 读取的长度（不写直接读取所有）
    readLine()：读取一行
    readLines()：读取所有数据，将每一行数据都作为列表的每一个元素
    for line in 文件对象:     每一行数据
    执行完读操作，需要关闭文件！ close()
    以下方法自动执行close()方法，否则文件会一直被占用
    with open("文件路径", "r") as f
        f.
"""
f = open("/data-source/06_容器的通用操作.py", "r", encoding="UTF-8")
print(f.read(10))
print(f.read())
print(type(f.readlines()))
print(f.readlines())
for my_f in f.readlines():
    print(type(my_f))
# 在执行完读操作之后，文本中的指针都会移动