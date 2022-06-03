import socket

# tcp服务端程序开发流程

# ①创建服务端套接字
# 有了服务端的套接字,可以实现接收客户端的请求了
# 参数1:socket.AF_INET ip地址:IPv4地址
# 参数2:socket.SOCK_STREAM 套接字类型:流套接字 tcp协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用
# 为什么设置端口号复用:程序结束运行后,不会立即释放的端口资源,还想连接到此服务器的端口,需要①修改服务器的端口 或者②设置端口号复用
# 参数1:socket.SOL_SOCKET 当前的套接字
# 参数2:socket.SO_REUSEADDR 设置套接字复用选项
# 参数3:True 复用选项的值 默认是False
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# ②绑定服务端的ip地址和端口号
# bind方法中输入的是一个元组类型
# 元组中的第一个参数:服务端的ip地址,字符串类型, 空字符串表示本机中的任何地址
# 元组中的第二个参数:端口号 整数类型,可以自行修改
tcp_server_socket.bind(('', 8080))
# ③设置监听
# 设置服务端最大连接数量(客户端的数量)
# 参数:128 数量值, 可以自行修改
tcp_server_socket.listen(128)
# ④等待接收客户端程序连接
# 执行此行代码时,如果没有客户端和服务端连接,一直在此行代码等待(程序不会结束运行), 客户端阻塞
# 返回值1:客户端和服务端进行数据传输的套接字
# 返回值2:连接的客户端的ip地址和端口号
print('等待客户端的链接...')
client_server_socket, client_ip_port = tcp_server_socket.accept()
print(f'客户端的IP地址和端口号是:{client_ip_port}')
# ⑤接收数据(服务端接收客户端发来的数据)
# 1024:接收的数据大小 1024个字节 可以自行修改
recv_data = client_server_socket.recv(1024)
# 将接收到的数据进行解码,转换成字符串类型,人能看懂
print(f'客户端发送的数据为:{recv_data.decode("utf-8")}')
# ⑥发送数据(服务端将客户端需要的数据返回给客户端)
send_data = 'hello world'
# 需要给发送的数据进行编码,转换成二进制类型,计算机能看懂
client_server_socket.send(send_data.encode('utf-8'))
# ⑦关闭连接
# 关闭服务端和客户端通信的套接字
client_server_socket.close()
# 关闭服务端套接字
tcp_server_socket.close()
