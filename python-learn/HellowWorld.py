# 占位符拼接字符串 %s字符串型占位符（其他类型使用%s将转换成str后输出）  %d整型  %f浮点型
    #number = 17
    #name = "刘昇"
    #message = "第%s期 , %s" % (number , name)
    #print(message)

#
    #print("1 * 1 = %.2f" % (19.90 * 1.2 ** 7.0))
"""
    name = input("请告诉我你是谁？")
    print("我是： " + name)
"""
import random

# if elif else
"""
str1 = "123"
str2 = "123" 
print(str1 == str2)
age = input("输入年龄: ")
age = int(age)
if age >= 18:
    print("你已成年，补票")
print("祝你旅途愉快")

num = 10
if int(input("请输入一个数： ")) == num:
    print("猜对了")
elif int(input("再猜一次：  ")) == num:
    print("猜对了")
else:
    print("你没有机会了")
"""

# while
# 1~100相加
"""i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)"""

# 判断
"""num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess = int(input("请输入要猜测的数字： "))
    count += 1
    if guess == num:
        print("猜对啦")
        flag = False
    else:
        if guess < num:
            print("猜小了")
        else:
            print("猜大了")
print(f"你一共猜了{count}次")"""

# 双循坏打印99乘法表
"""
i = 1

while i < 10:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}  " , end = '')
        j += 1
    print()
    i += 1
"""
# for in

"""
name = 'this a test , form itmeima'
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"this a test , form itmeima中有{count}个a")
"""

# range() 生成序列
balance = 10000

for x in range(1,21):
    if balance <= 0:
        print("工作发完了，下个月再发吧")
        break
    performance = random.randint(1,11)
    if performance < 5:
        print(f"第{x}个员工的绩效考核为：{performance}， 太低了，不发")
        continue
    balance -= 1000
    print(f"第{x}个员工的绩效考核为：{performance}， 已发1000，账户余额为：{balance}")





