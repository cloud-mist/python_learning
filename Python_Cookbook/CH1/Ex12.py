# Q:找出序列中出现次数最多的元素


# A:collections.Counter类，  most.common()方法

# Ex 在一个单词列表中找出那个单词频率最高
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)  # 出现频率最高的三个单词
print(top_three)                        # [('eyes', 8), ('the', 5), ('look', 4)]


# D: 输入：Counter可接受 hashable元素构成的序列对象。
#    底层实现：一个Counter对象 是一个字典，元素映射出现次数
print(word_counts['look'])              # 4
print(word_counts['eyes'])              # 8

# 方法1：手动增加计数
morewords = ['why','are','you','not','looking','in','my','eyes']
'''
for word in morewords:
    word_counts[word] +=1
print(word_counts['eyes'])              # 9
'''
# 方法2： 使用update()方法
word_counts.update(morewords)
print(word_counts['eyes'])               # 9


# Counter很容易和数学运算结合
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
d = a - b
print(d)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, 
# "don't": 1, "you're": 1, 'under': 1})

'''
适用：需要制表或计数数据的场合
'''