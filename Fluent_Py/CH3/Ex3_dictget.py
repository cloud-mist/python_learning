# use dict.get to fetch and update a list of word occurrences from the index
# a better soluton is in Ex4
'''build an index mapping word -> list of occurrences'''

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            occurrences = index.get(word, [])   # 提取word出现的次数
            occurrences.append(location)        # 把单词新出现的位置添加到列表后面
            index[word] = occurrences           #　把新的列表放回字典

for word in sorted(index, key=str.upper):
    print(word, index[word])
