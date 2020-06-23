'''
6个序列都可以进行的操作：包括索引，切片，加，乘，检查成员

'''
# 1.创建&访问
list1 = ['google',123, 23.2] 	# 不需要具有相同的类型
list2 = [1,2,3,4,5,6,7]

print("list1[0]: ", list1[0])
print("list2[1:4]: ", list2[1:4])


# 2.更新&删除
list1[1] = 'test'
print("把123更新成了：", list1[1])

print("原来：", list1)
del list1[1]
print("now: ",list1)


# 3.脚本操作符
list3, list4 = ['he','llo'], ['eve','ry','one']

print("len(list3):",len(list3))		# len
print(list3+list4)					# 拼接+
print(list3*2)						# 重复输出*
print('ry' in list4)			 	# 是否在list中
for x in list3:						# 迭代
	print(x, end="")

# 4.嵌套
print()
a, b= ['a', 'b','c'], [1,2,3]
x = [a, b]
print(x)
print(x[1][1])		# 2

# 5.函数

# len(list)  max(list)  min(list)

# 元组转换为列表  list(seq)   seq-- 要转换的列表或者字符串
tuple1 = ('123', 123, 'google')
list6 = list(tuple1)
print(list6)

str1 = "hello "
list7 = list(str1)
print(list7)		# ['H', 'e', 'l', 'l', 'o', ' ']


# 6.方法
'''
list.append(obj)	添加到列表末尾的对象。
list.count(obj)		统计某个元素在列表中出现的次数
list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值

list.copy() 
list.clear()
'''
# list.sort( key=None, reverse=False)
# reverse = True 降序， reverse = False 升序（默认）
list8 = [4,3,6,7,1,0,5]
list8.sort(reverse=True)	# 1.降序
print(list8)

list8.reverse()				# 2.反转
print(list8)

list9 = [1,2,3,4]
list9.insert(1,'hi')		# 3.insert 参数1指定位置， 参数2指定内容
print(list9)

list9.pop()					# 4.pop([index=-1])  
print(list9)
list9.pop(1)				# 5.index可以指定，默认为-1，即最后一个元素
print(list9)				# [1,2,3]

list9.remove(1)				# 6.参数为要删除的列表元素值
print(list9)			    # [2,3]

# 7.list.index(x[, start[, end]])	从列表中找出某个值第一个匹配项的索引位置
print(list8.index(7))