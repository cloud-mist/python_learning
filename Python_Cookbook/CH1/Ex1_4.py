# Q: 从一个集合中找到最大 或者最小的N个元素

# A: heapq模块的 nlargest() nsmallest()
import heapq

nums = [1, 5, 7,2,6, 22,8,-3,22]
print(heapq.nlargest(3, nums))          # [22, 22, 8]
print(heapq.nsmallest(2, nums))         # [-3, 1]


portfolio = [
    {'name':'a', 'share':'100', 'price': 91},
    {'name':'b', 'share':'50', 'price': 543},
    {'name':'c', 'share':'200', 'price': 21},
    {'name':'d', 'share':'35', 'price': 31},
    {'name':'e', 'share':'45', 'price': 16},
    {'name':'f', 'share':'75', 'price': 115},
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(cheap)
# [{'name': 'e', 'share': '45', 'price': 16}, {'name': 'c', 'share': '200', 'price': 21}]
print(expensive)
# [{'name': 'b', 'share': '50', 'price': 543}, {'name': 'f', 'share': '75', 'price': 115}]


# D: N小于集合元素数量，有更好的性能。在底层，会先将集合数据进行堆排序后放入一个列表中
heap = list(nums)
heapq.heapify(heap)
print(heap)                 # [-3, 1, 7, 2, 6, 22, 8, 5, 22]

# heap[0]永远是最小元素，弹出最小元素，o（logn）
print(heapq.heappop(heap))  # -3
heapq.heappop(heap)
print(heap)                 # [2, 5, 7, 22, 6, 22, 8]

# S: 1.要查元素个数少：nlargest();     
#    2.N=1: max() ;
#    3.大小相近：sorted(items)[-N:]   先排序后切片