# 抽象类，读取（文本、JSON）文件
import json

from pyecharts_可视化图表.案例.data_define import Record


class FileReader:
    def reader(self):
        pass


# 读取文本文件
class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def reader(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        # 将取到的数据放到对象中,在放到列表中
        record_list = []
        for data_line in f.readlines():
            data_line = data_line.strip()  # 去除前后空格以及\n
            data_list = data_line.split(",")
            my_record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            # print(my_record)
            record_list.append(my_record)
            # print(my_record)
        f.close()
        return record_list


# JSON文件读取
class JSONFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def reader(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        # 将取到的数据放到对象中,在放到列表中
        json_record_list = []
        for data_line in f.readlines():
            data_dict = json.loads(data_line)
            my_record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            json_record_list.append(my_record)
            # print(my_record)
        f.close()
        return json_record_list


if __name__ == '__main__':
    test_file_reader = TextFileReader("2011年1月销售数据.txt")
    print(test_file_reader.reader())
    # json_file_reader = JSONFileReader("2011年2月销售数据JSON.txt")
    # print(json_file_reader.reader())