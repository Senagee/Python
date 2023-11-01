import socket

# 创建socket对象
socket_client = socket.socket()
# 请求链接的服务端的ip地址和端口
    # 元组做参数
socket_client.connect(("localhost", 8888))

while True:
    # 发送消息
    msg = input("请输入你要发送给服务端的消息： ")
    if msg == "exit" or msg == "断开链接":
        break
    socket_client.send(msg.encode("utf-8"))
    # 接收消息
    server_data = socket_client.recv(1024).decode("utf-8")
    if server_data == "拒绝":
        print(f"服务端发送过来的消息：{server_data}")
        break
    print(f"服务端发送过来的消息：{server_data}")

socket_client.close()

