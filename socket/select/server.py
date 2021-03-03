"""
套接字分类：
- 接受套接字 accept
- 连接套接字 connection

问：select 等到多少个事件才返回呢？只要有一个就返回？
答：select 遍历传递进来的所有套接字，并返回所有出现的可读、可写或异常事件。
如果没有事件，重新遍历。如果始终没有，超时返回。

问：可写是如何判断的呢？
答：建立连接即可写


"""
import select
import socket
import queue
from time import sleep

# Create a TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个 socket 实例
server.setblocking(False)  # 设置为非阻塞模式

# Bind the socket to the port
server_address = ('localhost', 8090)
print('starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Sockets to which we expect to write
# 处理要发送的消息
outputs = []

# Outgoing message queues (socket: Queue)
conn_dict = {}

while inputs:
    print("-----------------------------")
    # 开始 select 监听
    # 第三个参数用来监听套接字是否出现异常（也就是有没有断开）
    readable, writable, exceptional = select.select(inputs, outputs, inputs)    # 阻塞
    # Handle inputs
    # 循环判断是否有客户端连接进来, 当有客户端连接进来时 select 将触发
    for s in readable:
        print("readable", s)
        # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时，说明有新客户端连接进来了
        if s is server:
            # 有新的客户端连接
            connection, client_address = s.accept()
            print('connectison from', client_address)
            connection.setblocking(0)
            inputs.append(connection)

            # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
            conn_dict[connection] = queue.Queue()
        else:
            # 有老用户发消息
            data = s.recv(1024)

            if data != '':
                print('received "%s" from %s' % (data, s.getpeername()))
                # 将收到的消息放入到相对应的socket客户端的消息队列中
                conn_dict[s].put(data)
                # Add output channel for response
                # 将需要进行回复操作socket放到output 列表中, 让select监听
                if s not in outputs:
                    outputs.append(s)
            else:
                # 在读取的过程中客户端断开了连接, 将客户端的监听从input列表中移除
                print('closing', client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # 移除对应socket客户端对象的消息队列
                del conn_dict[s]

    for s in writable:
        print("writable", s)
        try:
            # 如果消息队列中有消息,从消息队列中获取要发送的消息
            message_queue = conn_dict.get(s)
            send_data = ''
            if message_queue is not None:
                # get_nowait 要区别 get 来学习
                # get_nowait 发现没有值立即返回，get 会等待直到有值可取
                send_data = message_queue.get_nowait()
            else:
                # 客户端连接断开了
                print("has closed ")
        except queue.Empty:
            # 客户端连接断开了
            print("%s" % (s.getpeername()))
            outputs.remove(s)
        else:
            # print "sending %s to %s " % (send_data, s.getpeername)
            # print "send something"
            if message_queue is not None:
                s.send(send_data)
            else:
                print("has closed ")
            # del message_queues[s]
            # writable.remove(s)
            # print "Client %s disconnected" % (client_address)


    for s in exceptional:
        print("exceptional", s)
        print('exception condition on', s.getpeername())

        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del conn_dict[s]

    # TODO 挂起 1s 为哪般？
    sleep(1)
