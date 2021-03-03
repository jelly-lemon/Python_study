"""
O(1) 时间复杂度找出栈中最大的数

举例：
假设有入栈：1 3 7 5，如何求出此时最大值？
出栈 5 7：1 3，如何求出此时最大值？

思路 1：
用两个栈，一个栈正常存数据（取名数据栈），另一个栈每次都存最大值（取名最大栈），
这样，最大栈栈顶元素就是当前最大值。
数据栈正常出栈，最大栈也出栈，最大栈栈顶始终是当前最大元素。
空间复杂度 O(n)

画图：

[数据栈]      [最大栈]
______        ______
| 5  |        | 7  | (栈顶元素为最大值)
| 7  |  ----> | 7  |
| 3  |        | 3  |
| 1  |        | 1  |
------        ------
         || (出栈 5 7 后)
        \||/
         \/
[数据栈]      [最大栈]
______        ______
| 3  |  ----> | 3  | (栈顶元素始终为最大值)
| 1  |        | 1  |
------        ------

"""
