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