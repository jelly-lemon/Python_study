"""
pip install h5py（不是 hdf5）

对于一个 DataSet
+-- Dataset
|   +-- (Raw) Data Values (eg: a 4 x 5 x 6 matrix)
|   +-- Metadata
|   |   +-- Dataspace (eg: Rank = 3, Dimensions = {4, 5, 6})
|   |   +-- Datatype (eg: Integer)
|   |   +-- Properties (eg: Chuncked, Compressed)
|   |   +-- Attributes (eg: attr1 = 32.4, attr2 = "hello", ...)

"""
import h5py
import numpy as np


def test_0():
    """
    创建 hdf5 文件

    --/
      |--bar1
         |--dset1
      |--dset
    """
    f = h5py.File("h5py_example.hdf5", "w")

    # 在根目录 "/" 下创建子目录
    g1 = f.create_group("bar1")

    # 在根目录 "/" 下创建数据集
    d = f.create_dataset(name="dset", data=np.arange(16).reshape([4, 4]))
    d.attrs["myAttr1"] = [100, 200]
    d.attrs["myAttr2"] = "Hello, world!"

    # 在子目录 "/bar1" 下创建数据集
    d1 = g1.create_dataset("dset1", data=np.arange(10))
    f.close()

def test_1():
    """
    读取 h5 文件
    """
    f = h5py.File("h5py_example.hdf5", "r")

    # 打印根目录下的文件夹和文件名
    print(f.name)
    print([key for key in f.keys()])

    # 读取根目录下文件
    d = f["dset"]
    print(d.name)
    print(d[:])

    # 打印文件的属性
    for key in d.attrs.keys():
        print(key, ":", d.attrs[key])

    # 读取子目录
    g = f["bar1"]

    # 打印数据集的三种方法
    print(f["/bar1/dset1"][:])        # 1. absolute path
    print(f["bar1"]["dset1"][:])    # 2. relative path: file[][]
    print(g['dset1'][:])

    # 删除数据集
    # 【注意】需要删除时读取模式应该为 'a'
    # del g["dset1"]

    f.close()

if __name__ == '__main__':
    test_1()
