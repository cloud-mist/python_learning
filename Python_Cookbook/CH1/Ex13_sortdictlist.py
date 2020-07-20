# Q: 一个字典列表，根据某个字典字段来排序这个列表


# A: 使用operator模块的itemgetter函数。
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# 1.根据任意字典字段排序
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
'''
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
'''
print(rows_by_uid)
'''
[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
'''

# 2.也支持多个keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
'''
[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},       3和4lname同，又按fname
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]
'''


# D: 也适用min和max函数
print(min(rows, key=itemgetter('uid')))
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}

# 有时也可以用lambda表达式代替，但itemgetter()会快一些
rows_by_fname1 = sorted(rows, key=lambda r: r['fname'])