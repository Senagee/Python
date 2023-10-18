# Map（key, value）
my_dict = {"王力宏": 99, "周杰龙": 88, "林俊杰": 77}
print(type(my_dict))
print(my_dict)

# 新增元素
my_dict["长相又"] = 66
print(my_dict)

# 修改元素
my_dict["王力宏"] = 100
print(my_dict)

# 删除元素 pop(Key)
my_dict.pop("王力宏")
print(my_dict)

# 获取所有Key Keys()
my_keys = my_dict.keys()
print(my_keys)

my_dict = {
    "张三": {
        "薪资": 1000,
        "级别": 1
    },
    "李四": {
            "薪资": 2000,
            "级别": 2
        },
    "王五": {
            "薪资": 3000,
            "级别": 1
        },
    "赵六": {
            "薪资": 4000,
            "级别": 1
        },
    "六七": {
            "薪资": 1000,
            "级别": 3
        }
}
print(my_dict)

# 级别 1 的升职加薪
for emp in my_dict:
    if my_dict[emp]["级别"] == 1:
        my_dict[emp]["级别"] += 1
        my_dict[emp]["薪资"] += 1000
print(my_dict)