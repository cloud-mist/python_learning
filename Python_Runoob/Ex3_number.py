# --------------Number---------------

'''
三种类型：
	1.int			没限制大小，可当做long用
	2.float		
	3.complex		形如a + bj 或 complex(a,b)  实部虚部均是浮点型

类型转换：
	1.int(x) 		将x转换为一个整数。
	2.float(x) 		将x转换到一个浮点数。
	3.complex(x) 	将x转换到一个复数，实数x，虚数0
	4.complex(x, y) 将 x 和 y 转换到一个复数，实数x虚数y。x和y是数字表达式。
'''

import math
import random

# Special
print(17/3)   		 # 5.666666667	结果总是浮点
print(17//3)  		 # 5	 		结果是向下取整，
print(17.0//3) 		 # 5.0 			但不一定是整数，跟分母分子类型有关

# Math Func
a, b = 5.1, 4
print(math.ceil(a)) 	# 向上取整		6						
print(math.floor(a))	# 向下取整		5						
print(math.exp(b))		# e的b次方		54.598150033144236	
print(math.log(100, 10))# lg100			2.0
print(math.modf(a))		# 整数小数部分  (0.09999999999999964, 5.0)
print(math.pow(2,3))	# x**y			8.0
print(math.sqrt(b))		# 平方根		2.0
print(round(17/3, 5))	# 5.66667		四舍五入值，5:舍入到小数点后的几位


# Random Func
c = random.choice(range(10))
print(c)

d = random.randrange(96, 100, 2)	# 选取 96-100 的偶数,不包含100
print(d)				

e = random.random() 				# 随机生成一个[0,1)的实数
print(e)				

list = [1, 3, 6, 8]		
random.shuffle(list)				# 将序列的所有元素 随机排序
print("random list:", list)			# random list:[6, 8, 3, 1]

f = random.uniform(5,10) 			# 随机生成一个实数，在[x,y]范围
print(f)							# 8.03743952515141