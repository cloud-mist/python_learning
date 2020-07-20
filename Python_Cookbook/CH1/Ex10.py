# Q:在一个序列上 保持元素顺序&消除重复元素


# A: 1.若序列上的值为 hashable ，利用set 或 生成器。
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))          # [1, 5, 2, 9, 10] 元素位置有序

#    2.若为 不可哈希的(如dict)
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe2(b, key=lambda d: (d['x'],d['y']))) )
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


# D:仅仅消除重复元素， 简单构造集合即可
print(set(a))                    # {1, 2, 5, 9, 10} 元素位置被打乱