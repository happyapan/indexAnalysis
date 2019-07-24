import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 与服务端相同
sock.connect(('127.0.0.1', 20178))
message ='send you a message'
sock.send(message.encode('utf-8'))
data = sock.recv(200)
print('recieved ', data.decode('utf-8'))
sock.close()
