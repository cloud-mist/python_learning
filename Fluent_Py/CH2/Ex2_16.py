# sorted  和 list.sort 的区别

'''
1.list.sort method sorts a list in place. returns None.chang the target object,
  and does not creat a new list
2.sorted creat a new list and returns it.

reverse: True降序。默认为False
'''

fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))               # ['apple', 'banana', 'grape', 'raspberry']
print(fruits)   # unchanged           ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits, reverse=True)) # ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len))      # ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, key=len, reverse=True))#['raspberry', 'banana', 'grape', 'apple']
print(fruits)                       # ['grape', 'raspberry', 'apple', 'banana']
fruits.sort()
print(fruits)                       # ['apple', 'banana', 'grape', 'raspberry']

