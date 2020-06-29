# Simple Syntax

str='Runoob'
 
print(str)                 # Runoob
print(str[0:-1])           # Runoo
print(str[0])              # R
print(str[2:5])            # noo
print(str[2:])             # noob
print(str * 2)             # RunoobRunoob	重复输出	
print(str + 'hello')       # Runoobhello	连接字符串	
print('------------------------------')
print('hello\nrunoob')     # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')    # 字符串前加一个r(raw)  不会发生转义


# 1.;可以一行多条语句   2.print默认换行，加end=""不会换行
x= "a"; y = "b"; print( y, end=" " ); print( x, end="" )  


'''
1.通常一行写完一条语句，但可以 加 '\' 写多行
2.在 [], {}, 或 () 中的多行语句，不需要使用反斜杠'\'
total = item_one + \
        item_two + \
        item_three
'''

"""		********	RESULT   *******
hello
runoob
hello\nrunoob
ba
"""