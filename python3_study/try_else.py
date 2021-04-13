"""
try else 结构：没有任何异常就执行 else
"""

try:
    print("hello")
except Exception:
    print("exception")
else:
    print("world")