# --------元组拆包(tuple unpacking) 出现形式-----------

# 1.平行赋值（parallel assignment）
x = (33.94, -118.408)
a, b = x
print(a, b)                 # 33.94 -118.408

# 2. *运算符把一个可迭代对象拆开作为函数参数
print(divmod(20, 8))        # (2, 4)
t = (20, 8)         
print(divmod(*t))           # (2, 4)
c, d = divmod(*t)
print(c, d)                 # 2 4

# 3.让一个函数能用元组返回多个值，然后调用函数的代码能接受这些返回值
import os                   # 返回以路径和文件名的组成的元组(path,last_part)
_, filename = os.path.split('d:/test.txt')
print(filename)             # test.txt

# 4.用* 平行赋值
e, f, *rest = range(5)
print(e,f, rest)            # 0 1 [2, 3, 4]

g, *body, h,f =range(5)     # can appear in any position
print(g,body,h,f)           # 0 [1, 2] 3 4

