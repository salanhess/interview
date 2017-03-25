#coding=utf-8

#refer to https://python.freelycode.com/train/pyallknow/detail/1
#define a class using with format then use it
#  use format __init__  to receive parameters
#  __enter__  return class self for it related function use
# __exit__ for exception handle not want to return True


class Usefile():
    def __init__(self,filename,opentype):
        print(filename,opentype)

    def __enter__(self):
        return self

    def write(self,str):
        print(str)
        int('abc')

    def __exit__(self, a, b, c):
        print(a)
        print(b)
        print(c)
        #return True

try:
    with Usefile('twit.txt','r') as f:
        f.write("abc")
except ValueError:
    print("Catch error!")