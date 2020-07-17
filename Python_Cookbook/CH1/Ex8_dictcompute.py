# Q:在字典上对数据执行各种计算（求最大，最小，排序等）


# A:
price = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HOQ': 37.20,
	'FB': 10.75,
}

min_price = min(zip(price.values(), price.keys()))
max_price = max(zip(price.values(), price.keys()))
print(min_price,max_price)		# (10.75, 'FB') (612.78, 'AAPL')

prices_sorted = sorted(zip(price.values(), price.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HOQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

