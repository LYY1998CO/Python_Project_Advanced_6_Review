import socket  # 导入模块

# web服务器通过http协议和浏览器(客户端)进行通信,http协议基于tcp协议

# ①创建服务端套接字
# 参数1:IPv4地址
# 参数2:基于tcp协议的套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# ②绑定服务端ip地址和端口号
# 接收的是一个元组 参数1:字符串类型的ip地址 参数2:服务器的端口号
tcp_server_socket.bind(('', 8080))
# ③设置监听
tcp_server_socket.listen(128)
# ④等待接收客户端(浏览器)的连接  一直阻塞等待
# 返回一个元组类型 参数1:浏览器和服务器通信的套接字 参数2:浏览器端ip地址和端口号
client_server_socket, client_ip_port = tcp_server_socket.accept()
print(f'链接的客户端的IP地址和端口号为:{client_ip_port}')
# ⑤接收数据(浏览器发送的请求报文)
recv_data = client_server_socket.recv(1024)
# 解码:将二进制类型的数据转换成字符串类型
recv_data = recv_data.decode('gbk')
print(f'客户端发来的数据为{recv_data}')
# ⑥发送数据 重点:web服务器发送的数据要以响应报文格式发送 响应行+响应头+空行+响应体(网页中展示的内容)
# 响应行
response_line = 'HTTP/1.1 200 OK\r\n'
# 响应头
response_header = 'Server:python\r\n'
# 空行
# 响应体
response_body = '<h1>我是一个一级标签</h1>'
# 将四部分拼接成响应报文的格式
response_data = response_line + response_header + '\r\n' + response_body
response_data = response_data.encode('gbk')
# 发送响应报文数据
client_server_socket.send(response_data)
# ⑦关闭连接
client_server_socket.close()
tcp_server_socket.close()
