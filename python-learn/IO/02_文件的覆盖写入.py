"""
    write() :  覆盖写入！
    flush() : 刷新，将写入的数据从缓冲区加载到硬盘中
    close() : 内置了 flush()的功能
"""
f = open("D:/python/python-learn/IO/write_test.text", "w", encoding="UTF-8")
f.write("Hello World!!!")
f.write("Hello !!! World!!!")
f.close()

f = open("D:/python/python-learn/IO/write_test.text", "w", encoding="UTF-8")
f.write("Hello World!!!")


