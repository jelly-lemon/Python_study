import numpy as np

# # 创建 npy
# data = np.array([1,2,3,4])
# np.save("./data.npy", data)
#
# # 读取 npy
# data = np.load("./data.npy", allow_pickle=True)
# print(data)

# 创建 npz
data1 = np.array([1,2,3,4])
data2 = np.array([5,6,7,8])
# 【注意】形参名即保存的数组名（也是 zip 中的文件名）
np.savez("./data.npz", data1=data1, data2=data2)

# 读取 npz
data = np.load("./data.npz", allow_pickle=True)
with np.load("./data.npz", allow_pickle=True) as f:
    data1 = f["data1"]
    print(data1)
