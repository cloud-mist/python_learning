# Q:在字典上对数据执行各种计算（求最大，最小，排序等）


# A:用zip翻转，变成(值，键)对，值会先进行比较。
price = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HOQ': 37.20,
	'FB': 10.75,
}

min_price = min(zip(price.values(), price.keys()))
max_price = max(zip(price.values(), price.keys()))
print(min_price,max_price)	    # (10.75, 'FB') (612.78, 'AAPL')

prices_sorted = sorted(zip(price.values(), price.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HOQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]


# D:
# 在字典上执行普通的数学运算，仅仅作用与键，而不是值。
print(max(price))                   # IBM
print(min(price))                   # AAPL

# 想通过values方法解决。但只能知道价格，而不知到名字。
print(min(price.values()))          # 10.75
print(max(price.values()))          # 612.78


# 当多个实体拥有相同值，键会决定返回结果。
price1 = {'aaa':23, 'zzz':23}
min_price1 = min(zip(price1.values(), price1.keys()))
max_price1 = max(zip(price1.values(), price1.keys()))
print(min_price1, max_price1)       # (23, 'aaa') (23, 'zzz')










