# Q:队列能够以给定的优先级进行排序， 每次pop 会返回最高优先级的那个元素

# A: 利用heapq模块实现简单的优先级队列
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())          # Item('bar')
print(q.pop())          # Item('spam')
print(q.pop())          # Item('foo')
print(q.pop())          # Item('grok')

