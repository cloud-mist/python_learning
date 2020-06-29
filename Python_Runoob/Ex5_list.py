'''
 六个序列都可以进行的操作：索引，切片，加，乘，检查成员
'''

# 1.创建&访问
list1 = ['google',123, 23.2] 			# 不需要具有相同的类型
list2 = [1,2,3,4,5,6,7]

print("list1[0]:", list1[0])			# list1[0]: google
print("list2[1:4]:", list2[1:4])		# list2[1:4]: [2, 3, 4]

# 2.更新&删除
print("before:", list1)					# before: ['google', 123, 23.2]
list1[1] = 'test'
print("123 更新为:", list1[1])			# 123 更新为: test
del list1[1]
print("now:",list1)						# now: ['google', 23.2]

# 3.脚本操作符
list3, list4 = ['he','llo'], ['eve','ry','one']

print("len(list3):",len(list3))			# len			len(list3): 2
print(list3+list4)						# 拼接+			['he', 'llo', 'eve', 'ry', 'one']
print(list3*2)							# 重复输出*		['he', 'llo', 'he', 'llo']
print('ry' in list4)			 		# 是否在list中	True
for x in list3:							# 迭代			hello
	print(x, end="")

# 4.嵌套
print("\n")
a, b= ['a', 'b','c'], [1,2,3]
x = [a, b]
print(x)								# [['a', 'b', 'c'], [1, 2, 3]]
print(x[1][1])							# 2

# 5.函数
# len(list)  max(list)  min(list)

# 元组转换为列表:list(seq)  	 seq-- 要转换的列表或者字符串
tuple1 = ('123', 123, 'google')
list6 = list(tuple1)
print(list6)							# ['123', 123, 'google']

str1 = "hao "
list7 = list(str1)
print(list7)							# ['h', 'a', 'o', ' ']


# 6.方法
'''
list.append(obj)	添加到 列表末尾的对象。
list.count(obj)		统计某个元素在列表中 出现的次数
list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值

list.copy() 
list.clear()
'''
# list.sort(key=None, reverse=False)
# reverse=True降序，reverse=False 升序(默认)
list8 = [4,3,6,7,1,0,5]
list8.sort(reverse=True)	# 1.降序
print(list8)				# [7, 6, 5, 4, 3, 1, 0]

list8.reverse()				# 2.反转
print(list8)				# [0, 1, 3, 4, 5, 6, 7]

list9 = [1,2,3,4]
list9.insert(1,'hi')		# 3.insert 参数1:指定位置，参数2:指定内容
print(list9)				# [1, 'hi', 2, 3, 4]

list9.pop()					# 4.pop([index=-1])  
print(list9)				# [1, 'hi', 2, 3]	弹出了4

list9.pop(1)				# 5.index可以指定，默认为-1，即最后一个元素
print(list9)				# [1,2,3]			弹出了hi

list9.remove(1)				# 6.参数为要删除的列表元素值
print(list9)			    # [2,3]

# 7.list.index(x[, start[, end]])	从列表中找出 某个值第一个匹配项的索引位置
print(list8.index(5))		# 4		65行的结果list中5的位置为4