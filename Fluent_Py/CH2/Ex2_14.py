# 一个谜题
t = (1, 2, [30, 40])
t[2] += [50, 60]    
# TypeError: 'tuple' object does not support item assignment
# 但是t确实被修改为了(1, 2, [30, 40, 50, 60])

'''
教训：
    1.不要把可变对象放在元组里
    2.增量赋值不是一个原子操作，虽抛出异常，但是完成了操作。
    3.查看python字节码并不难，它对我们了解代码背后的运行机制很有帮助
'''