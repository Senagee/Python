# 序列（有序的数据容器：列表、元组、字符串）

# 切片操作 格式： 序列[起始位: 结束位: 步长]
my_list = [1, 2, 3, 5, 4]
my_list1 = my_list[1: 3]
print(my_list1)

#     反转序列
my_list2 = my_list[::-1]
print(my_list2)

my_str = "学Python，来黑马程序员，月薪过万"
my_strs = my_str.split("，")
my_str1 = my_strs[1]
my_str2 = my_str1.replace("来", "")
print(my_str2)