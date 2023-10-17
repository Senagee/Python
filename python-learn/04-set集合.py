# 两个集合的差集
my_set1 = {"itheima", "atguigu", "黑马程序员", "Mac", "Mac"}
my_set2 = {"itheima", "黑马程序员", "Mac", "Windows"}

# 差集
my_set3 = my_set1.difference(my_set2)
print(my_set3)
# 差集并且修改
my_set1.difference_update(my_set3)
print(my_set1)
# 合并
my_set4 = my_set1.union(my_set2)
print(my_set4)
print(len(my_set4))
