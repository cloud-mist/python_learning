# Q: 寻找两个字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2,
}

print(a.keys() & b.keys())      # {'y', 'x'}    find keys in common
print(a.keys() - b.keys())      # {'z'}         find keys in a that are not in b
print(a.items() & b.items())    # {('y', 2)}    find (key, value) pairs in common

# 修改或过滤字典元素
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)                        # {'x': 1, 'y': 2}


'''
 D: 键视图支持集合操作，不用先将它们转换成set
    items()返回一个包含(键，值)对的元素视图对象,支持集合,可以用来查找两字典相同键值对
    values()不支持集合。因为values不一定唯一. 如果非要操作，可以先转换成set

'''
