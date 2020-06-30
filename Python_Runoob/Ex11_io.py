# python的输入输出功能
'''
----------输出方式----------
a.表达式语句
b.print
c.write方法，标准输出文件用sys.stdout

ps:将值转换成字符串   str()用户易读和repr()解释器易读
'''
# 在 ：后传入一个整数，保证该域至少有这么多宽度，美化表格有用
table = {'google':1, 'runoob':2, 'taobao': 3}
for name, number in table.items():
    print('{0:10}==>{1:10d}'.format(name, number))

# 读取键盘输入  input 从标准输入读入一行文本
str1 = input("please input: ")
print("repeat: ", str1)

'''
# ---------- 读写文件 ---------
open(filename, mode)   参数1：你要访问的文件名称的字符串值
参数2: 决定打开文件模式：只读，写入，追加。非强制默认为只读

模式	    r	r+	w	w+	a	a+
读	        +	+		+		+
写		        +	+	+	+	+
创建		    	+	+	+	+
覆盖		    	+	+		
指针开始    +	+	+	+		
指针结尾					+	+
'''
# 将一句话写入到文件test中
f = open("d:/test.txt", "w") 
f.write("This is a test.\nOnly a test\n")
f.close()

# 文件对象方法

# 1. f.read()   
# 读取文件内容，并作为字符串或字节对象返回，read参数省略为读取所有。
f = open("d:/test.txt", "r") 
str2 = f.read(); print(str2)      
f.close()

# 2. f.readline()
with open("d:/test.txt", "r") as f: 
    str3 = f.readline()
print(str3) 

# 3.f.readlines()
# 返回该文件中包含的所有行。可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f = open("d:/test.txt", "r") 
str3 = f.readlines(); print(str3) 
f.close()

# 4.如果要写入一些不是字符串的东西, 那么将需要先进行转换:
f = open("d:/test.txt", "w") 
value = ('hi', 22)
str4 = str(value)
f.write(str4); f.close()

with open("d:/test.txt", "r") as f: 
    str5 = f.read()
print(str5)       # ('hi', 22)


'''
--------------- pickle模块 -------------
实现了基本的数据序列和反序列化。
序列化:   将程序中运行的对象信息保存到文件中去，永久存储
反序列化：从文件中创建上一次程序保存的对象
'''
import pickle, pprint
data1 = {'a': [1, 2.0],
         'b': ('string', u'unicode string'),
         'c': None}
list1 = [1, 2, 3]
list1.append(list1)
output = open('data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(list1, output, -1)
output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)    # {'a': [1, 2.0], 'b': ('string', 'unicode string'), 'c': None}
data2 = pickle.load(pkl_file)
pprint.pprint(data2)    # [1, 2, 3, <Recursion on list with id=37315520>]
pkl_file.close()


