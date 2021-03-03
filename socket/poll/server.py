"""
poll 使用

windows 环境并未实现 poll 和 epoll
"""

import select
import socket
import queue
from time import sleep

poller = select.poll()