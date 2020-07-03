#dictionary
#字典是一系列 键-值对。与键相关联的值：数字、字符串、列表、字典都可。

#1.形式：键值对在一组花括号里； 键值用冒号隔开
alien_0 = {'color':'green','points': 5}
new_points = alien_0['points']
print("you just earned " + str(new_points) + " points!")
#用字典名[键]	来访问

#2.添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#！！键值对的排列顺序与添加顺序不同

#3.删除键值对 	del 字典名[键]
del alien_0['color']	#删除color键值对
print(alien_0)

#由类似对象组成字典
favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite languages is " +
	favorite_languages['sarah'].title() +
	".")


#******字典遍历******
#1.遍历所有	for循环
#Ⅰ.key,value 一组变量； Ⅱ.items()它返回一个键值对列表
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print('\nKey: ' + key)
	print("Value: " + value)
#上一个例子遍历
for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is "+
		language.title() + '.')
#遍历字典中的键，没有值 用keys()
for name in favorite_languages.keys():
	print(name.title())
#使用当前键来访问与之关联的值
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	if name in friends:
		print(" hi " + name.title() +
			", i see your favorite language is " +
			favorite_languages[name].title() + '.')

#**顺序遍历 所有键**
#for循环 用sorted返回的键进行排序
for name in sorted(favorite_languages.keys()):
	print(name.title() + ',thank u for taking the poll.')

#遍历值，用values()  和用keys 是一样的道理。但他不会提剔除重复的值
#**剔除重复用set**
for language in set(favorite_languages.values()):
	print(language.title())

#****嵌套****
#需要将字典存储进列表 或 将列表作为值存储在字典中
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

#将列表存储在字典中
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
print("you ordered a " + pizza['crust'] + "-crust pizza "+
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

#每当需要在字典中将一个键关联到多个值，都可以把值设为一个列表
favo_lgg = {
	'jen': ['python', 'ruby'],
	'sarah':['c'],
	'edward': ['ruby', 'go'],
	'phil':['python','haskell'],
}
for name,lgg in favo_lgg.items():
	print('\n' + name.title() + "'s favorite languages are:")
	for language in lgg:
		print('\t' + language.title() )

#字典中存储字典 及访问
users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title() )
	print("\tLocation: " + location.title() )
	
