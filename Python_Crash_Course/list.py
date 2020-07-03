#列表的使用
#1.在列表 末尾 添加元素	append
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

#2.在列表 某个位置 插入元素	insert() 指定索引与值,它后面的元素向后移一个位置
motorcycles.insert(0, 'ducati2')
print(motorcycles)

#3.删除元素	del	需知道其索引
del motorcycles[0]
print(motorcycles)

#4.删除元素 pop()		 删除列表 末尾的元素 并且能够接着使用它
popped_moto = motorcycles.pop()
print(motorcycles)	#证明已经删除尾部元素
print(popped_moto)	#证明还可以访问它

#目前列表的值	['honda', 'yamaha', 'suzuki']
#5.根据值删除元素	remove()	
motorcycles.remove('honda')
print(motorcycles)

#6.永久排序从小到大sort()		从大到小sort(reverse = True)
cars = ['bmw','aodi','baoma','qirui']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

#7.临时排序 sorted()
cars_2 = ['bmw','aodi','baoma','iqrui']
print("\nhere is the sorted list:")
print(sorted(cars_2) )	#从小到大
print("\nhere is the original list again:")	
print(cars_2)	#验证还是原始排列
#遇到问题：	cars_2.sorted(reverse = True)
#print(cars_2)	#从大到小

#8.反转列表永久修改	想回去再执行reverse()
cars_2.reverse()
print(cars_2)
cars_2.reverse()	#再回来

#9.列表长度	len()
print(len(cars_2))
