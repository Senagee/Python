#
import socket

# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
    # 元组做参数
socket_server.bind(("localhost", 8888))
# 监听端口
    # 接收多少个链接
socket_server.listen(1)
# 等待客户端链接
    # 普通写法
# result: tuple = socket_server.accept()
# conn = result[0]        # 链接对象
# address = result[1]     # 客户端地址信息
    # 进阶写法
conn, address = socket_server.accept()
    # accept方法是阻塞方法（等待客户端的链接）

print(f"链接对象的ip地址： {address}")
while True:
    # 使用conn对象接收客户端信息
    client_data: str = conn.recv(1024).decode("utf-8")
    if (client_data == "exit") | (client_data == "断开链接"):
        break
        # recv方法也是阻塞式的方法
        # recv方法的参数是缓存区的大小， 返回的是一个byte数组，所以要进行解码
    print(f"客户端发送过来的消息：{client_data}")
    # 发送消息
        # 别忘记编码
    msg = input("请输入向客户端发送的消息：")
    if msg == "拒绝":
        break
    conn.send(msg.encode("utf-8"))

conn.close()
socket_server.close()