# 列表对象.sort(key = 指定按照列表中元素排序的依据（需要传递一个函数）, reverse = 排序结果的顺序)

my_list = [["小刘", 10], ["小王", 20], ["小吴", 30]]
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)