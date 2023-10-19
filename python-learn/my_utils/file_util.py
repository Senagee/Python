def print_file_info(file_name):
    """
    打印文件内容，
    如果不存在，捕获异常，finally关闭文件
    :param file_name:文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        print(f.read())
    except:
        print("文件不存在")
    finally:
        if f:  # 如果f == None ==> f == False
            f.close()


def append_to_file(file_name, data):
    """
    追加数据到文件中
    :param file_name:文件路径
    :param data: 追加的数据
    :return: None
    """
    f = open(file_name, "a", encoding="utf-8")
    f.write(data)
    f.close()


if __name__ == '__main__':
    print_file_info("D:/python/python-learn/IO/write_tet.text")
