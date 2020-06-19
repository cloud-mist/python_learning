# Simple Syntax

str='Runoob'
 
print(str)               
print(str[0:-1])           # 输出 第一个~倒数第二个 的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + 'hello')       # 连接字符串
print('------------------------------')
print('hello\nrunoob')     # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')    # 字符串前加一个r(raw)  不会发生转义

# ;可以一行多条语句    print默认换行，加end="" 不会换行
x= "a";y = "b";print( y, end="" ); print( x, end="" )  

'''
1.通常一行写完一条语句，但可以 加 '\' 写多行
2.在 [], {}, 或 () 中的多行语句，不需要使用反斜杠'\'
total = item_one + \
        item_two + \
        item_three
'''

"""
********RESULT*******
Runoob
Runoo
R
noo
noob
RunoobRunoob
Runoobhello
------------------------------
hello
runoob
hello\nrunoob
ba
"""