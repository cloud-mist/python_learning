# -------------- 面向对象 ------------

'''
1.类对象
两种操作:属性引用，实例化
属性引用:obj.name  
'''

class MyClass:
    i = 123
    def f(self):
        return "hello world"

x = MyClass()
print("myclass类的属性i:", x.i)
print('myclass类的方法f:', x.f())

#  __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart   # self代表类的实例，而非类
        self.i = imagpart
y = Complex(3.0, -4.5)
print(y.r, y.i)


# 类的方法
class people:
    # 基本属性
    name = ''
    age = 0
    
    __weight = 0     # 私有属性，类外部无法直接访问
    # 构造方法
    def __init__(self, n, a, w):
        self.name = n 
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁。" %(self.name, self.age))

p = people('runoob', 10, 30)    # 实例化
p.speak()

# 单继承
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)      # 调用父类构造函数
        self.grade = g
    def speak(self):                        # 重写父类方法
        print("%s says:i am %d years old.Grade %d. " \
               %(self.name, self.age, self.grade))

s = student('ken', 10, 60, 3)
s.speak()


# 多继承准备
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print('my name is %s, i am a speaker, my topic is %s'%\
            (self.name, self.topic))

# 多重继承
class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample('tim', 25, 80, 4, 'python')
test.speak()        # 方法名同，默认调用括号中排在前面的父类方法
                    # my name is tim, i am a speaker, my topic is python


# 方法重写
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Child()
c.myMethod()
super(Child, c).myMethod()  # 重要！！ 用子类对象调用父类已被覆盖的方法



'''
-----类属性和方法-------
1.私有属性  __private_attrs 两个下划线开头，声明为私有，外部无法直接访问  
2.类的方法  def关键字； 必须包含参数self且为第一个,self代表类的实例。
3.私有方法  __private_method
'''

class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
counter = JustCounter()
counter.count()                 # 1
counter.count()                 # 2
print(counter.publicCount)      # 2
# print(counter.__secretCount)    报错 ，无法访问到私有变量。

'''
__init__ : 构造函数，在生成对象时调用      __setitem__ : 按照索引赋值
__del__  : 析构函数，释放对象时使用        __getitem__ : 按照索引获取值
__repr__ : 打印，转换                      __call__   : 函数调用 

__len__: 获得长度               __add__: 加运算
__cmp__: 比较                   __mul__: 乘运算
__pow__: 乘方                   __sub__: 减运算
__mod__: 求余                   __truediv__: 除
'''


# 运算符重载，对类的专有方法进行重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' %(self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5, -2)
print(v1+v2)        # Vector (7, 8)