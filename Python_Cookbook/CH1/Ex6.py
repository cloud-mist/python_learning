# Q:一键多值字典 multidict

# A:想映射多个值，需将多个值保存到另一个容器，列表或者集合。
# 列表可以保留元素插入顺序，列表可以消除重复元素

from collections import defaultdict		# defaultdict会自动初始化第一个元素

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])							# [1, 2]

# D: