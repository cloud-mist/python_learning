# Q: 一个包含N个元素的元组或序列 ---> 分解为N个单独变量

# A: 可迭代对象通过一个 简单赋值 来分解。 要求：变量总数要与序列 吻合
p = (1, 2)
x, y = p
print(x, y)                 # 1 2

data = ['acme', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)                 # acme
print(date)                 # (2012, 12, 21)
year, mon, day = date
print(mon)                  # 12

# D: 不仅仅是元组、列表，只要是可迭代对象。 包括字符串，文件，迭代器，生成器
s = 'Hello'
a, b, c, d, e = s
print(b)                    # e
# 想丢弃一些用不到的值，用一个用不到的变量名来作为丢弃值的名称
_, sh, pr, _ = data
print(sh)                   # 50
