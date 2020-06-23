# ************FUNCTION***********

# 1.定义
#example1
def hello():
	print("hello world")
hello()

#example2
def area(width, height):
	return width * height

def print_wel(name):
	print("welcome", name)

print_wel("runoob")
w, h = 4, 5
print("width=", w, "height=", h, "area=", area(w, h))

# 2.参数
# 2.1 必需参数     须以正确的顺序传入函数。调用时的数量必须和声明时的一样
# 2.2 关键字参数	   使用关键字参数来确定传入的参数值，允许函数调用时参数的顺序与声明时不一致
def printinfo(name, age=35):
	print('name:', name)
	print('age:', age)
	return 
printinfo(age=50, name='runoob')

# 2.3 默认参数	如果没有传递参数，则会使用默认参数
printinfo( name='runoob')

# 2.4 不定长参数
# 可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，

# 加了 * 参数 会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo1( arg1, *vartuple ):
	print("输入： ")
	print(arg1)
	print(vartuple)

# 调用
printinfo1(70,60,50)	# 70 \n	(60, 50)
