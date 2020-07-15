# 对numpy.ndarray的行和列进行基本操作

import numpy

a = numpy.arange(12)    # 新建一个0-11的整数numpy.ndarray
print(a)                # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(type(a))          # <class 'numpy.ndarray'>

print(a.shape)          # (12,)  看数组维度，它是一维，有12个元素的数组
a.shape = 3, 4          # 变成二维，打印
print(a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
''' 

print(a[2])             # [ 8  9 10 11]     打印第二行
print(a[2, 1])          # 9                 打印第二行第一列
print(a[:, 1])          # [1 5 9]           打印第一列

print(a.transpose())    # 行和列交换
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
