# Q:可迭代对象中分解出N个元素，可迭代对象的长度超过N

# A: *表达式解决
user_record = ('dave', 'dave@example.com', '773-555', '847-555')
name, email, *phone_num = user_record
print(phone_num)                # ['773-555', '847-555']


# D: 解压不确定个数或任意个数元素的可迭代对象而设计。

# E1:迭代一个边长的元组序列
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)            # foo 1 2
    elif tag == 'bar':           # bar hello
        do_bar(*args)            # foo 3 4

# E2:字符串的拆分
line = 'nobody:*:-2:-2:unprivileged user:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)                     # nobody
print(homedir)                   # /var/empty
print(sh)                        # /usr/bin/false

# E3:想解压丢弃元素。不能只单独指定一个 *。可以*_
record = ('acme', 50, 123.45, (12,18,2012))
name, *_, (*_, year) = record
print(name)                      # acme
print(year)                      # 2012

# E4:实现递归算法
items = [1,2,3,4,5]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
 
print(sum(items))                # 15 
