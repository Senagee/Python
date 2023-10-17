# 数据容器
name_list = ["123", 1, 3, True]
# print(name_list)
# print(type(name_list))

# 倒序输出
#     for x in range(1, 5):
#         print(name_list[-x])

# 常用操作
mylist = ["itcase", "itmeima", "python"]

# 查找元素下标
mylist.index("itcase")

# 插入 （需要填写下标）
mylist.insert(1, "2")

# 追加单个元素（也将数据容器当作它的一个元素）
mylist.append(["atguide1", "powernode1"])

# 追加一组数据
mylist.extend(["atguide1", "powernode1"])
print(mylist)

# 删除元素（根据索引删除）
    # 两种方法 使用del关键字只能删除元素，而pop方法不仅能移除元素，还能获取到移除的元素
mylist.pop(1)
del mylist[1]

# 删除与之匹配的元素（首个）
mylist.remove("itmeima")

# 清空列表
mylist.clear()

# 统计列表中某个元素的个数
mylist.count("itmeima")

