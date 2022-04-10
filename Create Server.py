# pycharm
import socket

server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen()


s, raddr = server.accept()  # 等待对方连接

while True:
	data = s.recv(1024)
	print(data)

	s.send('Got it'.format(data.decode()).encode())

s.close()
server.close()
