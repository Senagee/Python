money = 10000
name = "刘昇"



def main():
    while True:
        if input("请输入用户名：") != name:
            print("用户名错误, 请重新输入！")
        else:
            exit1 = True
            while exit1:

                print("[1] 查询账户余额")
                print("[2] 取款")
                print("[3] 存款")
                print("[4] 退出")
                num = int(input("请输入需要的操作："))
                if 1 == num:
                    search()
                elif 2 == num:
                    amount2 = int(input("请输入取款金额："))
                    if amount2 <= money:
                        withdraw(amount2)
                        search()
                    else:
                        print("余额不足！")
                elif 3 == num:
                    amount3 = int(input("请输入存款金额："))
                    deposit(amount3)
                    search()
                elif 4 == num:
                    exit1 = Exit()
            break;


def search():
    """
    查询余额
    :return: None
    """
    print(f"当前账户余额为：{money}")


def withdraw(amount2):
    """
    取款操作
    :return: None
    """
    global money
    money -= amount2


def deposit(amount3):
    """
    存款
    :return: None
    """
    global money
    money += amount3


def Exit():
    """
    退出
    :return: False
    """
    return False
main()