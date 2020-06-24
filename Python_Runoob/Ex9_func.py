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

# *参数 会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 2.4.1
def printinfo1( arg1, *vartuple ):
	print("输出： ")
	print(arg1)
	print(vartuple)

printinfo1(70,60,50)	# 调用  result: 70 \n (60, 50)

# 2.4.2
def printinfo2(arg1, *vartuple):
	print("输出： ")
	print(arg1)
	for var in vartuple:
		print(var)
	return
printinfo2(70,60,50)   	 # result: 70(\n)60 (\n)50

# 2.4.3  参数加**    会以字典形式导入
def printinfo3(arg1, **vardict):
	print("输出：")
	print(arg1)
	print(vardict)
printinfo3(1, a=2, b=3)		#1   (\n)  {'a': 2, 'b': 3}

#2.4.4   参数中星号 * 可以单独出现,  *后的参数必须用关键字传入
def f(a,b,*,c):
	return a+b+c
print(f(1,2,c=3))	#c必须用关键字方式


# 3.匿名函数		使用lambda来创建
# lambda函数有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
sum = lambda arg1,arg2: arg1+arg2
print("10+20 =",sum(10,20))

# 4.return语句
def sum1(arg1, arg2):
	total = arg1 + arg2
	return total
t = sum1(10, 20)
print(t)

# 5.   / 用来指明 函数形参必须使用指定位置参数，不能使用关键字参数的形式。
def f1(a,b,/, c, d, *, e, f):
	print(a,b,c,d,e,f)
f1(10,20, 30,d=40, e=50,f=60)   #a,b必须指定位置形参;c,d位置或关键字形参;ef关键字