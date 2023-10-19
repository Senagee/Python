def str_reverse(s):
    """
    反转字符串
    :param s:被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]
def substr(s, x, y):
    """
    对字符串切片（子字符串）
    :param s: 原字符串
    :param x: 初始索引
    :param y: 结束索引
    :return: s[x,y) 字符串
    """
    return s[x: y]
if __name__ == '__main__':
    print(type(str_reverse("abc")))
    print(str_reverse("abc"))
    print(substr("abcd", 0, 4))