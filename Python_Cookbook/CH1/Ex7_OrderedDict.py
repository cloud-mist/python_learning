# Q:对一个字典进行迭代时，可控制其中元素顺序


# A:OrderedDict 会严格按元素添加顺序进行
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
	print(key, d[key])

'''	******Result******
foo 1
bar 2
spam 3
grok 4
'''

# 构建一个映射 以便稍后对其进行序列化或编码成另一种格式
import json
print(json.dumps(d))	# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}


# D:OrderedDict 内部维护一个双向链表，会根据元素加入顺序排列键的位置。
#   第一个新加入的元素放置在链表末尾。   注意：OrderedDict大小是 普通字典2倍多