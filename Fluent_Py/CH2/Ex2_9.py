# Defining and using a named tuple.
# This ex shows how we could define a named tuple
# to hold information about a city.
from collections import namedtuple
City = namedtuple('city', 'name country population coordinates')
# Two parameters.a class name and a list of field names.
tokyo = City('tokyo', 'jp', 36.93, (35.68, 139.69))
# 对应字段数据要以一串参数的形式传入到构造函数中
print(tokyo)
# city(name='tokyo', country='jp', population=36.93, coordinates=(35.68, 139.69))

# access the fields(字段信息) by name or position.
print(tokyo.name)                   # tokyo
print(tokyo.coordinates)            # (35.68, 139.69)
print(tokyo[2])                     # 36.93

