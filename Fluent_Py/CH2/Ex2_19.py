# 由于排序耗时,得到一个有序序列，最好能保持它的有序， bisect.insort
# insort(seq, item) 将item插入序列seq中， 保持seq的升序
import bisect
import random
SIZE = 7
random.seed(1729)
# my idea: seed指定后，它相当于一个固定随机生成序列，所以才跟书上的结果一样、
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    # randrange() 返回指定递增基数集合中的一个随机数，基数默认值为1。
    bisect.insort(my_list, new_item)
    print('%2d->'%new_item, my_list)

'''     *****RESULT*****
10-> [10]
 0-> [0, 10]
 6-> [0, 6, 10]
 8-> [0, 6, 8, 10]
 7-> [0, 6, 7, 8, 10]
 2-> [0, 2, 6, 7, 8, 10]
10-> [0, 2, 6, 7, 8, 10, 10]
'''