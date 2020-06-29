# 变量赋值之后会被创建，无需声明

# 单个变量赋值
counter = 100
name = "runoob"
print(counter)
print(name)
# 多个变量赋值
a, b, c=1, 2, "run"



'''
不可变数据：Number（数字）、string（字符串）、Tuple（元组)
可变数据  ：List（列表）  、Dict（字典）    、Set（集合）
'''
# -----------1.Number-----------
# 输出类型&判断
print(type(a))              # <class 'int'> 
print(isinstance(a, int) )  # True

# -----------2.String-----------
# 没有字符类型，一个字符=长度为1的字符串
word = 'python'
print(word[0], word[5])     # p n
print(word[-1], word[-6])   # n p

"""
1、反斜杠用来转义，使用r让反斜杠不转义。
2、字符串用+ 连接，用* 重复。
3、两种索引方式: 从左往右以0开始,从右往左以-1开始。
4、Python中的字符串不能改变
"""

# -----------3.List-----------
# 目的：完成大多数集合类的数据结构实现，元素类型可以不同，支持列表
list = ['abcd', 786, 2.4, 'rubo',]
tinylist = [123, 'runnnn']

print(list)                 # ['abcd', 786, 2.4, 'rubo']
print(list[0])              # abcd
print(list[1:3])            # [786, 2.4]
print(list[2:])             # [2.4, 'rubo']
print(tinylist * 2)         # [123, 'runnnn', 123, 'runnnn']
print(list + tinylist)      # ['abcd', 786, 2.4, 'rubo', 123, 'runnnn']

# 元素可变
q = [1,2,3,4,5]
q[0] = 9
q[2:]=[7,8,9]
q[1] = []
print(q)                    # [9, [], 7, 8, 9]

''' 1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List用+ 拼接。
    4、List中元素是可变的。
'''
#截取 可以接受第三个参数，  作用：指定步长
print(q[1:4:2])             # [[], 8]
print(q[1:4])               # [[], 7, 8]

# **** 翻转字符串 ****
p = "i like runoob"
words = p.split(" ")        # 用空格将字符串分割为列表
words = words[-1::-1]       # 逆向
output = ' '.join(words)    # 组合
print(output)               # runoob like i


# -----------4.Tuple-----------
# ps:与列表类似，但元组元素不可修改，写在小括号里，用逗号隔开。

tuple = ('abcd', 24, 'rub', 70.2)
tinytuple = (123, 'ruuu')
print(tuple)
print(tuple[0])                 # abcd
print(tuple[1:3])               # (24, 'rub')
print(tuple[2:])                # ('rub', 70.2)
print(tinytuple * 2)            # (123, 'ruuu', 123, 'ruuu')
print(tuple + tinytuple)        # ('abcd', 24, 'rub', 70.2, 123, 'ruuu')

# Special
tup1 = ()       # 空元组
tup2 = (12,)    # 一个元素

# Attention
'''
    0. string、list 和 tuple 都属于 sequence（序列）。

    1、与字符串一样，元组的元素不能修改。
    2、可被索引和切片，方法一样。
    3、构造包含 0 或 1 个元素的元组的特殊语法
    4、可以使用 + 拼接。
'''


# -------------5.Set---------------
# 由一个或数个形态各异大小的整体组成，
# 基本功能:1.进行成员关系测试 2.删除重复元素

# example
sites = {'google', 'taobao', 'run', 'zhihu', 'run'}
print(sites) # 重复元素会被去掉 {'zhihu', 'run', 'taobao', 'google'}

#成员测试   run 在集合中
if 'run' in sites:
    print("run 在集合中")
else:
    print("run 不在集合中")

#集合运算
set1 = set('abcde')
set2 = set('ababf')

print(set1)                 # {'d', 'c', 'e', 'a', 'b'}
print(set1 - set2)          # {'c', 'd', 'e'}
print(set1 | set2)          # {'f', 'c', 'e', 'a', 'd', 'b'}
print(set1 & set2)          # {'a', 'b'}
print(set1 ^ set2)          # {'f', 'd', 'c', 'e'}


# ------------6.Dict-------------

#define: 映射类型; 用{}, 无序的key:value 集合，同一字典，key必须唯一
dict3 = {}
dict3['one'] = "1-book"
dict3[2] = "2-tool"
tinydict = {'name':"runo", 'code':1,}

print (dict3['one'])            # 1-book
print (dict3[2])                # 2-tool
print (tinydict)                # {'name': 'runo', 'code': 1}
print (tinydict.keys())         # dict_keys(['name', 'code'])
print (tinydict.values())       # dict_values(['runo', 1])

# 构造函数dict()  直接从键值对序列中构造字典
print(dict(runo=1, google=2, taobao=3))
# {'runo': 1, 'google': 2, 'taobao': 3}