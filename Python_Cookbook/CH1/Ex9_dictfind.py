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


# D: 
