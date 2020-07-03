#1.for循环初探	for x in b：			x是自己定义的变量。b是列表的名字
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see you next trick, "+ magician.title()+"\n")
print("Thank you, everyone.That was a great magic show!")

#2.函数range()	
for value in range(1,5):
	print(value)
#打印的是1~4！

#3.用range()	 创建数字列表
numbers = list(range(1,6))
print(numbers)

#4.指定步长	
 #打印1~10内的偶数
even_numbers = list(range(2,11,2))
print(even_numbers)

 #.打印1~10的平方	**为乘方
squares = []
for value in range(1,11): 
	squares.append(value**2)
print(squares)

#5.简单计算函数	min max sum
print(min(squares))
print(max(squares))
print(sum(squares))

#6.列表解析！！	用一行代码来综合生成列表的方式
sq = [value**2 for value in range(1,11)]	#这里for没有	“：”
print(sq)

#7.使用列表的一部分

 #切片	指定要使用的第一个元素:最后结束元素位置（但不包含此元素）
players = ['charles','martina','michael', 'florence', 'eli']
print(players[0:3])	#0 1 2 位置元素

 #用负数索引
print(players[-3:])	#返回离列表末尾相应距离的元素
#['michael', 'florence', 'eli']

 #遍历切片
for player in players[:3]:
	print(player.title())
 #复制列表	
friend_players = players[:]		
#如果只是简单地friend_players = players 代表这两个东西都指向同一个列表而非复制
print(friend_players)

 #元组	不变的列表 const。不能单个的对元组里的内容进行修改但是可以整体修改
 

	
