# Creating, saving, and loading a large array of floats
from array import array
from random import random
floats  = array('d', (random() for i in range (10**7)))
print(floats[-1])   # inspect the last number in the array
                           # 0.09262539465289843
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])          # 0.09262539465289843
print(floats2 == floats)    # True

'''
array.tofile array.fromfile， 用起来很简单，
存读二进制文件要比文本文件快很多
'''