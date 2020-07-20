# Q: 排序类型相同的对象，但是它们不支持原生比较操作。


''' 
sorted有一个关键字参数key， 可以传入一个callable对象给他. 
这个对象对每个传入对象返回一个值，sorted用来排序。
'''
# ex User实例序列，通过user_id排序， 可以提供一个User实例作为输入并输出对应user_id值的callable对象
from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)
    

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
sort_notcompare()