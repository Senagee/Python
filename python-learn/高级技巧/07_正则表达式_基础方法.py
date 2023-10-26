# re的三个方法 match、 search、 findall

import re

s = "1python itmeima python python"
# match 方法
    # 从头开始检索，返回第一次命中的结果
    # ！ 只要头检索失败，后面的命不命中都无所谓
my_re1 = re.match("python", s)
print(my_re1)

# search 全局检索
my_re2 = re.search("python", s)
print(my_re2)

# findall
my_re3 = re.findall("python", s)
print(my_re3)
