# --------------Number---------------

'''
三种类型：
	1.int			没限制大小，可以当做long用
	2.float		
	3.complex		形如a + bj  或者 complex(a,b)  实部虚部均是浮点型

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
print(17//3)  		 # 5	 		结果是向下取整，但不一定是整数，跟分母分子类型有关
print(17.0//3) 		 # 5.0

# Math Func
a, b = 5.1, 4
print(math.ceil(a)) 	# 向上取整
print(math.floor(a))	# 向下取整
print(math.exp(b))		# e的b次方
print(math.log(100, 10))# lg100
print(math.modf(a))		# 返回x的整数与小数部分,整数部分以浮点型表示。
print(math.pow(2,3))	# x**y
print(math.sqrt(b))		# 平方根
print(round(17/3, 5))	# 返回x的四舍五入值， 5 代表摄入到小数点后的几位


# Random Func
c = random.choice(range(10))
print(c)

d = random.randrange(96, 100, 2)
print(d)				# 选取一个96-100 的偶数,不包含100

e = random.random() 	# 随机生成一个[0,1)的实数
print(e)				

list = [1, 3, 6, 8]		
random.shuffle(list)	# 将序列的所有元素 随机排序
print("随机排列：", list)

f = random.uniform(5,10)# 随机生成一个实数，在[x,y]范围
print(f)				