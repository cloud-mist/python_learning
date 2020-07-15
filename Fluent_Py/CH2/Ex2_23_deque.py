''' *****取代列表的另一种：队列*****
把列表模拟 栈或者队列，用append&pop  ，但删除或添加非常耗时.
所以 collections.deque(双向队列)
'''
# 使用双向队列
from collections import deque

# 1.建队
dq = deque(range(10), maxlen=10)    # maxlen可选，可容纳元素数量，一旦设定，不可改
print(dq)           # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# 2.旋转
dq.rotate(3)        # n>0 最右边n个元素移到队列左边
print(dq)           # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

dq.rotate(-4)       # n<0 最左边n个元素移动到右边
print(dq)           # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

# 3.添加元素
dq.appendleft(-1)   # 对一个满队头部添加元素时， 尾部元素会被删除
print(dq)           # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.extend([11, 22, 33]) # 尾部添加3个元素，挤掉了-1,1,2
print(dq)           # deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40]) 
#　extendleft(iter) 会把迭代器内元素逐个添加到队列左边，因此迭代器元素会逆序出现在队列
print(dq)           # deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)