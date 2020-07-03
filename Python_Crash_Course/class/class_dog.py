#	---------类---------
#1.创建Dog类
class Dog():
	'''一次模拟小狗的简单尝试'''

	def __init__(self, name, age):	
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll(self):
		print(self.name.title() + " rolled over!")

 #创建类的实例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
 #调用方法
my_dog.roll()

 #创建多个实例
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
