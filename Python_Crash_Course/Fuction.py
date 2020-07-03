#**********函数**********

#1.定义函数(无参)
def greet_user():
	print("hello world")
greet_user()
#a.定义def name():  b.语句   c.调用name()

#2.有参
def greet_user2(username):
	print("Hello," + username.title() +"!")
greet_user2('zx')

#3.位置实参与关键字实参
#位置实参就是，传递值时，要看清函数定义内的形参顺序，按序传递
#关键字实参是， 传递的是 形参名=要传递的值， 键值对，无需考虑形参内部顺序,不易出错。 但代码长
def describe_pet(type, name):
	print("I have a " + type + ".")
	print("My " + type + "'s name is " + name.title() + '.')
describe_pet(name = 'qwer', type = 'dog')
describe_pet('dog', 'qwer')
#还可以给形参设置默认值，调用方式可以混用

#4.返回简单值
def get_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()
musician = get_name('jimi', 'hendrix')
print(musician)

#5.返回字典
def build_person(first_name, last_name):
	person = {'first':first_name, 'last': last_name}
	return person
bianliang = build_person('jimi', 'hendrix')
print(bianliang)

#6.函数与while的结合
def get_name2(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print('please tell me your name:')
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	name2 = get_name2(f_name, l_name) 
	print('\nHello, ' + name2 + '!')

#7.传递列表	
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#8.在函数中修改列表
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(sorted(completed_models))

#9.传递任意数量的实参
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

#10.任意数量的关键字实参
def build_profile(first, last, **user_info):
''' 
	** 让Python创建一个 名为user_info的空字典，
	并将收到的所有名称—值对都封装到这个字典中。
	在这个函数中，可以像访问其他字典那样 访问user_info中的名称—值对。
'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert','einstein',
							 location = 'princeton',
							 field = 'physics')
print(user_profile)

#11.模块

