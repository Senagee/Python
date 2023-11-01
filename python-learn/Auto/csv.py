# DDT(Data Driver Test)：数据驱动测试

"""
csv文件读取基本操作
"""

# 导包
import _csv

# 打开csv文件
f = open("data.csv", 'r')

# 获取数据句柄（数据的入口）
rows = _csv.reader(f)

# 循环读取测试数据
for row in rows:
    print(row[0])