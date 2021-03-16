"""
套接字分类：
- 接受套接字 accept
- 连接套接字 connection

问：select 等到多少个事件才返回呢？只要有一个就返回？
答：select 遍历传递进来的所有套接字，并返回所有出现的可读、可写或异常事件。
如果没有事件，重新遍历。如果始终没有，超时返回。

问：可写是如何判断的呢？
答：建立连接即可写

问：socket 异常有哪些呢？
答：没响应？

该程序整体逻辑：
只要待读列表中有 socket，就一直循环下去。
按 “读 -> 写” 顺序执行。当接收到了客户端消息后才回复，否则不管。
读到了数据就把该 socket 放入待写列表中。
监听待读列中的所有 socket 有没有异常。
"""
import select
import socket
import queue
from time import sleep

# 创建一个 socket 实例
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 设置为非阻塞模式

# 绑定监听端口
server_address = ('localhost', 8090)
print('starting up on %s port %s' % server_address)
server.bind(server_address)

# 设置最大监听连接数
server.listen(5)

# 待读 socket 集合
inputs = [server]

# 待写 socket 集合
outputs = []

# 套接字消息队列
conn_dict = {}

# 只要有待读 socket，就循环
while inputs:
    print("-----------------------------")

    # 开始 select 监听
    # 第三个参数用来监听套接字是否出现异常（也就是有没有断开）
    # readable,writable,exceptional 都是后面三个参数的子集
    readable, writable, exceptional = select.select(inputs, outputs, inputs)  # 阻塞，超时返回

    # 循环判断是否有客户端连接进来, 当有客户端连接进来时 select 将触发
    for s in readable:
        print("readable")

        # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时，说明有新客户端连接进来了
        if s is server:
            # 有新的客户端连接，一次只能建立一个连接
            conn_socket, client_address = s.accept()
            print('connectison from', client_address)
            conn_socket.setblocking(0)  # 设置为非阻塞 socket？
            inputs.append(conn_socket)

            # 为连接的客户端单独创建一个消息队列，用来保存客户端发来的消息
            conn_dict[conn_socket] = queue.Queue()
        else:
            # 有老用户发消息
            # readable 列表中肯定是可读的：要么断开了，要么有数据来了。
            # 客户端主动正常断开连接：recv 返回空串
            # 客户端强制关闭连接：recv 报错
            try:
                data = s.recv(1024)

                if data != b'':
                    print('received "%s" from %s' % (data, s.getpeername()))

                    # 将收到的消息放入到相对应的 socket 客户端的消息队列中
                    conn_dict[s].put(data)

                    # 将该 socket 放入待写 socket 列表中（既然收到了消息，就要给出回复）
                    if s not in outputs:
                        outputs.append(s)
                else:
                    # 在读取数据发现客户端已经断开了连接, 将客户端的监听从 input 列表中移除
                    print(s.getpeername(), "closed")

                    # 将该连接 socket 移除待写和待读队列
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)

                    # 移除对应socket客户端对象的消息队列
                    del conn_dict[s]

                    # 关闭该连接
                    s.close()
            except ConnectionResetError as e:
                # 将该连接 socket 移除待写和待读队列
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)

                # 移除对应socket客户端对象的消息队列
                del conn_dict[s]

                # 关闭该连接
                s.close()

                # 正要读取数据，结果对方强制断开连接
                print(e)

    for s in writable:
        print("writable", s.getpeername())

        # 发来什么数据就回复什么数据
        message_queue = conn_dict.get(s)
        send_data = message_queue.get_nowait()
        try:
            s.send(send_data)
        except Exception as e:
            print(e)
        outputs.remove(s)

        print(send_data)

    for s in exceptional:
        # TODO 套接字会出现哪些错误呢？
        print('exception', s.getpeername())

        # 从待读列表中移除
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()  # 关闭 socket

        # 删除相应的消息队列
        del conn_dict[s]

    # 挂起 1s，模拟服务器忙碌
    sleep(1)
