import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while True:
    data = input("输入要发送的数据:")
    # 发送数据:
    s.send(data.encode("utf-8"))
    print(s.recv(1024).decode('utf-8'))
    if data == 'exit':
        break
s.send(b'exit')
s.close()