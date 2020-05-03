#*******用户输入和while循环********

#1.小例子之input 
message = input("tell me something, and i will repeat it back to you: ")
print(message)
#input接受一个参数，把用户输入解读为字符串

#2.用int()来获取数值
age = input("how old are u? ")
print(age)
#返回是 '21'		也就是说他是一个字符串
age =int(age)	#这样既可转换为数字,与数字比较了
print(age >= 18)

#综合例子
height = input("how tall are you , in inches? ")
height = int(height)
if height >= 36:
	print("\nyou're tall enough to ride!")
else:
	print("\nno!")

#3.求模运算 		例子：判断奇偶
number = input("enter a number, and i'll tell you if "+
	"it's even or add: ")
number = int(number)
if number % 2 == 0:
	print(str(number) + " is even.")
else:
	print(str(number) + " is odd.")

#4.小例子让用户选择什么时候退出，并设置个标志来判断
prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'q' to end the program."
active = True
while active:
	message = input(prompt)
	if message == 'q':
		active = False
	else:
		print(message)

#5.在列表之间移动元素
unconfirmed_users = ['alice','brain', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("verifying user: ", current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#6..删除特定值		删除所有的猫
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#7.将回答存储到字典里
responses = {}
polling_active = True
while polling_active:
	name = input("enter name: ")
	response = input("what like?")
	responses[name] = response

	repeat = input("another person?(yes or no)")
	if repeat == 'no':
		polling_active = False
print('\n--- Poll Results ---')
for name,response in responses.items():
	print(name + " like " + response + ".")
