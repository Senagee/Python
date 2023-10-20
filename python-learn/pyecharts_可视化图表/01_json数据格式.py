# json :  一种特殊格式的字符串， 方便不同语言数据之间的转换

# 引入json模块
import json
s = [{"name": "小刘", "age": 18}, {"name": "小黄", "age": 17}]
print(type(s))
# json.dumps()： 将python数据转换成json类型的字符串
j_s = json.dumps(s)
print(type(j_s))
# json.loads()： 将json类型的字符串转换成对应的python数据类型
s_s = json.loads(j_s)
print(type(s_s))