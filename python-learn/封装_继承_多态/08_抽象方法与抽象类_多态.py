# 抽象类做顶层设计，实现类做具体实现

# 抽象类（含有抽象方法）
class Ami:
    # 抽象方法 没有方法体
    def song(self):
        pass


class Dog(Ami):
    def song(self):
        print("狗叫")


def func(ami: Ami):
    ami.song()


func(Dog())
