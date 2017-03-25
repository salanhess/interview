#coding=utf-8

#refer to https://python.freelycode.com/train/pyallknow/detail/4

#classmethod:  used for such as class count,can be used in instance/class
#staticmethod: used just for organize structure
#use cls as parameters while define classmethod, then call int in __init__ method to count class instanced times.
#假如我们想仅实现类之间交互而不是通过实例？我们可以在类之外建立一个简单的函数来实现这个功能，但是将会使代码扩散到类之外，这个可能对未来代码维护带来问题。

#staticmethod can be used for class/instance as well,通常，有很多情况下一些函数与类相关，但不需要任何类或实例变量就可以实现一些功能.
#比如设置环境变量，修改另一个类的属性等等.这种情况下，我们也可以使用一个函数，一样会将代码扩散到类之外（难以维护）

class cat():
    class_count = 0

    def __init__(self,name):
        self.name = name
        self.cat_born()

    def hello(self):
        print(self.name + "miao~~")

    @classmethod
    def cat_born(cls):
        cls.class_count +=1

    @staticmethod
    def new_hello(name):
        print("this is new: " + name)

Lily = cat("lily")
Lily.hello()
Lily.new_hello("xxx")

print(cat.class_count)

xiaoming = cat("hleilei")
xiaoming.hello()
print(xiaoming.class_count)
cat.new_hello("Boss")