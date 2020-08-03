# Q:有一字典或实例序列， 根据特定字段 分组迭代访问


# A: itertools.groupby() 数据分组操作
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 需要按date分组迭代-->  指定字段排序，调用itertools.groupby()
from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))   # 按date排序
for date, items in groupby(rows, key=itemgetter('date')): #按date分组迭代
    print(date)
    for i in items:
        print(' ', i)
''' **************result**************
07/01/2012
  {'address': '5412 N CLARK', 'date': '07/01/2012'}
  {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
07/02/2012
  {'address': '5800 E 58TH', 'date': '07/02/2012'}
  {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
  {'address': '1060 W ADDISON', 'date': '07/02/2012'}
07/03/2012
  {'address': '2122 N CLARK', 'date': '07/03/2012'}
07/04/2012
  {'address': '5148 N CLARK', 'date': '07/04/2012'}
  {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
'''


# D:groupby() 扫描整个序列查找连续相同值。每次迭代，返回一个值和一个迭代对象。
这个迭代对象返回 生成全部等于上面值的组中所有对象。









