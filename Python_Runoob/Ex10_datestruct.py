# 1.列表推导式
'''
Introduction

1.目的：从序列创建列表的简单途径
2.形式：
'''
#ex1	将列表 每个数*3
vec = [2, 4,6]
a = [3*x for x in vec]
print(a)

#ex2
b = [[x, x**2] for x in vec]
print(b)

#ex3
fruit = ['banana', 'peach', 'apple']
c = [weapon.strip() for weapon in fruit]
print(c)

#ex4
d = [3*x for x in vec if x > 3]
print(d)


# 2.嵌套列表解析
matrix = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]
#将3*4矩阵 转换 4*3列表
e = [[row[i] for row in matrix] for i in range(4)]
print(e)

# 3.遍历技巧
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k,v in knights.items():
	print(k,v)