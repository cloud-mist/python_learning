class Car():
	""" car """
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0	#指定初始值，就无需包含形参

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("this car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an adometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles		

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(122)
print("\n")

#继承，创建子类
class Battery():
	'''模拟电动车电瓶'''

	def __init__(self, battery_size=70):
		'''初始化电瓶属性'''
		self.battery_size = battery_size

	def describe_battery(self):
		print("this car has a " + str(self.battery_size) + " -kwh battery.")

	def get_range(self):
		'''描述电瓶的续航里程'''
		range = self.battery_size * 3;
		message = "this car can go approximately " + str(range)
		message += ' miles on a full charge.'
		print(message) 

	def upgrade_battery(self):
		'''升级电瓶'''
		if self.battery_size != 85:
			self.battery_size = 85		


class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make,model,year)	
		#调用super函数，将父与子联系。调用init方法，让Elec包含父类所有方法与属性
		self.battery = Battery() #特有属性	自动创建的Battery类实例
	
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()