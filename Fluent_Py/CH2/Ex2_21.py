'''
memoryivew 不复制内容，操作同一数组的不同切片
memoryview 通过改变数组中的一个字节来更新数组里某个元素的值

'''

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))                # 5
print(memv[0])                  # -2
memv_oct = memv.cast('B')   
print(memv_oct.tolist())        # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers)                  # array('h', [-2, -1, 1024, 1, 2])
