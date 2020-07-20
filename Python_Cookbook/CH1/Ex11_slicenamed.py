# Q:包含大量无法直视的硬编码切片，想清理一下代码


# A: 假设要从一个记录的某个固定位置提取字段
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)  # 命名切片，使得代码更加清晰可读
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)                         # 51325.0


# D:代码中如果出现大量的硬编码下标会使得代码的可读性和可维护性大大降低。
#　　这样操作会更加清晰的表达代码目的

# Example
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])                   # [2, 3]
print(items[a])                     # [2, 3]

items[a] = [10, 11]                 
print(items)                        # [0, 1, 10, 11, 4, 5, 6]                 
del items[a]                       
print(items)                        # [0, 1, 4, 5, 6]

# 如果你有切片对象a，可调用a.start, a.stop, a.step属性获取更多信息
b = slice(5, 50, 2)
print(b.start, b.stop)              # 5 50
print(b.step)                       # 2

# 切片 indices(size)方法 映射一个已知大小序列， 
# 返回一个(start,stop,step),所有值缩小到适合这个已知序列的边界为止。
s = 'helloworld '
print(b.indices(len(s)))            # (5, 11, 2)
for i in range(*b.indices(len(s))):
    print(s[i])
                                    # w
                                    # r
                                    # d