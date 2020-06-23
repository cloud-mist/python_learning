# -----------迭代器和生成器-----------
#
import sys

list1 = [1,2,3,4]
list2 = list1.copy()
it = iter(list1)
print(next(it))
for x in it:
	print(x,end=" ")


# 使用了 yield 的函数被称为生成器（generator）
# 	生成器是一个返回迭代器的函数，只能用于迭代操作，
#	生成器就是一个迭代器

def fibonacci(n):
	#生成器函数-fibonacci
	a, b, counter = 0, 1, 0
	while True:
		if (counter > n):
			return
		yield a
		a, b = b, a+b
		counter += 1
f = fibonacci(10)

while True:
	try:
		print(next(f), end=" ")
	except StopIteration:
		sys.exit()