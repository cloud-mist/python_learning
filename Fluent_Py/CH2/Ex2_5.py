'''
列表推导：生成列表。 而生成器表达式是为了生成其他类型的序列类型。
生成器表达式的语法和列表推导差不多，只是把方括号换成了圆括号
'''
# initializing a tuple and an array from a generator expression
symbols = "#$%^j"
a = tuple(ord(symbol) for symbol in  symbols)
print(a) # (35, 36, 37, 94, 106)

import array
b = array.array('i', (ord(symbol) for symbol in symbols))
print(b)
# array('i', [35, 36, 37, 94, 106])


