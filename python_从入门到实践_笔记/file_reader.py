filename = 'pi_digits.txt'
with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip()) #rstrip()删除多余的空行
	lines = file_object.readlines()
#with 在不需要访问文件后将其关闭.python智能关闭
#open(文件名) 返回一个表示此文件的对象