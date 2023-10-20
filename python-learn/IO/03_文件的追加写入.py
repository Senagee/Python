
f = open("D:/python/python-learn/IO/write_test.text", "a", encoding="UTF-8")
f.write("追加写入！")
f.close()
f = open("D:/python/python-learn/IO/write_test.text", "a", encoding="UTF-8")
f.write("我再写追加写入！")
f.close()

