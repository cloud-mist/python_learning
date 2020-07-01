# ex1
# 把一个字符串变成unicode码位列表
symbols = '$%#@&@'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)
# [36, 37, 35, 64, 38, 64]

# ex2
str2 = 'djdfskd#$%'
codes2=[ord(strr) for strr in str2 ]
print(codes2)
#  [100, 106, 100, 102, 115, 107, 100, 35, 36, 37]
