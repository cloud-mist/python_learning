# --------------String---------------

# 1.访问字符串中的值
var1 = "hello world"
var2 = 'runoob'
print(var1[0])		# h   
print(var2[1:5])	# unoo

# 2.转义字符
'''
	\a  	响铃
	\b	退格(Backspace)
	\000	空
	\n  	换行
	\v  	纵向制表符
	\t  	横向制表符
	\r  	回车
	\f  	换页
'''

# 3.字符串运算符

# a. +字符串连接    b. *重复输出字符串    c. in   d.not in
# e.  r/R 原始字符串
a = "hello"
if ("e" in a):
	print("e 在变量a中")
else:
	print("e 不在变量a中")

print(r'\n'+ a)


# 3. 字符串格式化		用法：和c中sprintf用法一样
print("my name: %s\nmy age: %d" %('xiaoming', 10))

# 3.5 str.format()
# 基本用法：通过{}和：  来代替以前的%
print("{0} {1}".format("hello","world"))
print("网站名:{name}  地址:{url}".format(name="菜鸟教程", url="runoob.com") )
# 通过字典设置参数
site = {"name":"菜鸟教程", "url":"runoob.com"}
print("网站名:{name}  地址:{url}".format(**site))   # **site不懂！
# 通过list索引
my_list = ['菜鸟','runoob']
print("网站{0[0]}  地址{0[1]}".format(my_list))

#数字格式化
print("{:.2f}".format(3.1415926))
'''
{:.2f} 	 	保留小数点后两位
{:+.2f}         带符号保留小数点后两位
{:.0f} 	 	不带小数

{:0>2d}  	数字补零 (填充左边, 宽度为2)
{:x<4d}  	数字补x  (填充右边, 宽度为4)
{:,} 	 	以逗号分隔的数字格式
{:.2%} 	 	百分比格式
{:.2e} 	 	指数记法
{:>10d}         右对齐   (默认, 宽度为10)
{:<10d} 	左对齐   (宽度为10)
{:^10d} 	中间对齐 (宽度为10) 
'''
#进制
print('{:b}'.format(11)) #二进制输出
print('{:#x}'.format(11))#0xb

# 4.三引号  随便写，就能看到什么
str2 = '''	hello，everyone
	can use \n
	can use \t  yeah!\n    		amazing
'''
print(str2)

# 5. f-string  格式化字符串新方法,无需判断使用 %s 还是%d之类的
w = {'name': 'xiaoming', 'age':10}
print(f'{w["name"]}: {w["age"]}')




