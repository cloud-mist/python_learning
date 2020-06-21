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
可变数据  ：List（列表）、Dictionary（字典）、Set（集合）
'''

# 1.Number
# 输出类型和判断
print(type(a), type(b), type(c))
isinstance(a, int)

# 2.String
# 没有字符类型，一个字符就是 长度为1的字符串
word = 'python'
print(word[0], word[5])
print(word[-1], word[-6])

"""
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变
"""

# 3.List
# 目的：完成大多数集合类的数据结构实现，元素类型可以不同，支持列表
list = ['abcd', 786, 2.4, 'rubo',]
tinylist = [123, 'runnnn']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

#元素可变
q = [1,2,3,4,5]
q[0] = 9
q[2:]=[7,8,9]
q[1] = []
print(q)

''' 1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。
'''
#截取 可以接受第三个参数，  作用：指定步长
print(q[1:4:2])
print(q[1:4])

#***翻转字符串***
p = "i like runoob"
words = p.split(" ")        #用空格将字符串分割为列表
words = words[-1::-1]       #逆向
output = ' '.join(words)    #组合
print(output)               #输出



# -----------3.Tuple-----------
# ps:与列表类似，但元组元素不可修改，写在小括号里，用逗号隔开。

tuple = ('abcd', 24, 'rub', 70.2)
tinytuple = (123, 'ruuu')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

# special
tup1 = ()       #空元组
tup2 = (12,)    #一个元素

# Attention
'''
    0. string、list 和 tuple 都属于 sequence（序列）。

    1、与字符串一样，元组的元素不能修改。
    2、可被索引和切片，方法一样。
    3、构造包含 0 或 1 个元素的元组的特殊语法
    4、可以使用 + 进行拼接。
'''



# -------------4.Set---------------
# basic： 由一个或数个形态各异大小的整体组成，基本功能进行成员关系测试和删除重复元素

# example
sites = {'google', 'taobao', 'run', 'facebook', 'zhihu', 'run'}
print(sites) #重复元素会被去掉

#成员测试
if 'run' in sites:
    print("run 在集合中")
else:
    print("run 不在集合中")

#集合运算
set1 = set('abracadabra')
set2 = set('alacazam')

print(set1)
print(set1 - set2)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)



# ------------5.Dict-------------

#define: 映射类型;用{} , 无序的key：value 集合，同一字典，key必须唯一
dict3 = {}
dict3['one'] = "1- book"
dict3[2] = "2-tool"
tinydict = {'name':"runo", 'code':1, 'site': 'www.runo.com'}

print (dict3['one'])
print (dict3[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

# 构造函数dict()  直接从键值对序列中构造字典
print(dict(runo=1, google=2, taobao=3))









