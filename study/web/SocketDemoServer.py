import socket

# Python只支持AF_INET、AF_UNIX、AF_NETLINK和AF_TIPC家族
# AF_INET（又称 PF_INET）是 IPv4 网络协议的套接字类型，
# AF_INET6 则是 IPv6 的；而 AF_UNIX 则是 Unix 系统本地通信。
# 选择 AF_INET 的目的就是使用 IPv4 进行通信。因为 IPv4 使用 32 位地址，相比 IPv6 的 128 位来说，计算更快，便于用于局域网通信。
#
# 而且 AF_INET 相比 AF_UNIX 更具通用性，因为 Windows 上有 AF_INET 而没有 AF_UNIX。

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 20178))
sock.listen(5)

while True:
    conn, address = sock.accept()
    print('connect by ', address)
    data = conn.recv(200)
    print(data.decode('utf-8'))
    conn.send(bytes('hello', 'ascii'))
sock.close()
