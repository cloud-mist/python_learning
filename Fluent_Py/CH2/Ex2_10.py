from collections import namedtuple
City = namedtuple('city', 'name country population coordinates')
tokyo = City('tokyo', 'jp', 36.93, (35.68, 139.69))
print(City._fields)         # _fields属性 是一个包含所有字段的元组
# ('name', 'country', 'population', 'coordinates')

Latlong = namedtuple('Latlong', 'lat long')
delhi_data = ('delhi NCR', 'IN', 21.935, Latlong(28.613, 77.20))
delhi = City._make(delhi_data)  # 生成这个类的一个实例
print(delhi._asdict())  # 以collections.OrderedDict的形式返回，元组信息友好呈现
# {'name': 'delhi NCR', 'country': 'IN', 'population': 21.935, 
# 'coordinates': Latlong(lat=28.613, long=77.2)}

for key, value in delhi._asdict().items():
    print(key + ':', value)

'''     ****** Result *****
name: delhi NCR
country: IN
population: 21.935
coordinates: Latlong(lat=28.613, long=77.2)
'''
