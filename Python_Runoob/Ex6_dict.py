
# d = {key1 : value1, key2 : value2 }
# KEY必须唯一且不可变， VALUE可取任意类型。

# 1.创建&访问
dict1 = {'name':'runoob', 'age':7, 'class':'first'}
print("dict1['name']:", dict1['name'])		# dict1['name']: runoob

# 2.modify/add
dict1['age'] = 10			 	# update value of age
dict1['school'] = 'cai niao' 	# add school message
print(dict1)				 	# {'name': 'runoob', 'age': 10, 'class': 'first', 'school': 'cai niao'}

# 3.del
del dict1['name']				# delete name
print(dict1)					# {'age': 10, 'class': 'first', 'school': 'cai niao'}
dict1.clear()					# 清空dict
print(dict1)					# {}
#del dict    					删除字典

# 4.func
dict2 = {'name':'runoob', 'age':7, 'class':'first'}
print(len(dict2))		# 4.1 key的总数					3
print(str(dict2))		# 4.2 输出字典，加双引号
print(type(dict2))		# 4.3 返回变量类型				<class 'dict'>

# 5.method
'''
5.1 dict.clear()	删除字典内所有元素
5.2 dict.copy()		返回一个字典的浅复制
'''

dict3 = dict.fromkeys(dict2, "test")	# 复制所有键值,后面参数指定value
print(dict3)							# {'name': 'test', 'age': 'test', 'class': 'test'}

# 5.3 dict.get(key, default=None) 返回指定键的值， 
# key:要查找的， default:指定键值不存在，返回该默认值。
print(dict2.get('age'))
print(dict2.get('sex','不存在'))

# 5.4 key in dict  	判断键是否存在于字典中
if 'sex' in dict2:
	print("存在dict2中")
else:
	print("no exist")


# 5.5 dict.items()	返回可遍历的(键, 值) 元组数组。
for i,j in dict2.items():
	print(i,":",j)
# 5.6 dict.keys()	返回一个可迭代对象，可用list()转换为列表。
print(list(dict2.keys() ) )
# 5.9 dict.values()		返回迭代器，用list()转换成列表
print(list(dict2.values()))	

# 5.7 dict.setdefault(key, default=None) 和5.3类似，**但不存在时会添加那个**
dict2.setdefault('sex',None)
print(dict2)

# 5.8 dict.update(dict2)     把dict2 的键值对添加到 dict中
dict4 = {'zz':26}
dict4.update(dict2)
print(dict4)

# 5.10 pop(key[,default])   
# key: 要删除的键值 ,default: 如果没有key,返回default值
pop1 = dict2.pop('sex')
print(pop1)

# 5.11 popitem() 按FIFO返回 并删除字典中的最后一对键和值
pop2 = dict2.popitem()
print(pop2)
print(dict2)


 
