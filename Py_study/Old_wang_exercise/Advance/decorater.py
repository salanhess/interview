#coding=utf-8
import time

def print_call(fn):
    def wrap_(*args,**kwargs):
        start = time.clock()
        retval = fn(*args,**kwargs)
        print("cost time: %s" % (time.clock()-start))
        return retval
    return wrap_

@print_call
def test(str1):
    time.sleep(2)
    print(str1)
    return "111"

print(test("abc"))

#闭包就是一个捕捉了（或者关闭）非本地变量（自由变量）的代码块（比如一个函数）。
## 如果你不清楚我在说什么，你可能需要进修一下 CS 的相关课程，但是不要担心 —— 我会给你演示例子。
# 闭包的概念很简单：一个可以引用在函数闭合范围内变量的函数。

