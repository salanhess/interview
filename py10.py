#coding=utf-8
#@description: Charpter 9

#xrange
a = range(1,10)
print(type(a))
print(a[6])

#modify tuple (1,2,3) with list method,then output new tuple with(1,2,4)
tuple_a = (1,2,3)


#From id adress we can see tuple even content are same, but adress is still diff;but list will share a same adress
la = list(tuple_a)
print("Tuple tuple_a is: %s, address is %d" % (tuple_a,id(tuple_a)))
la[2]=4
print(tuple(la))
print("List la is: %s, address is %d" % (la,id(la)))
la = list(tuple_a)
la[2]=3
tuple_b = tuple(la)
print(tuple_b)
print("Tuple tuple_b is: %s, address is %d" % (tuple_b,id(tuple_b)))
lb = [1,2,4]
print("List lb is: %s, address is %d" % (lb,id(lb)))
lc = lb
print("List lc is: %s, address is %d" % (lc,id(lc)))
tuple_c = tuple_a
print("Tuple tuple_c is: %s, address is %d" % (tuple_c,id(tuple_c)))


#python列表推导式
#list generate with x for x in range format
#['1 love python', '2 love python', ... '10 love python'] ,
print([str(x) + ' love python' for x in range(1,11)])

#Tuple generate with double x for x in range format
#[(0, 0), (0, 2), (2, 0), (2, 2)]
print([(x,y) for x in range(0,3,2) for y in range(0,3,2)])

#Dictionary generate with double x for x in range format
#[{'name': 'Cary', 'age': 30}, {'name': 'Cary', 'age': 31}, {'name': 'Susan', 'age': 30}, {'name': 'Susan', 'age': 31}]
print([{"name":x,"age":y} for x in ["Cary","Susan"] for y in range(30,32)])

#clean up list, and copy operation?
lb = [1,2,4]
lx = lb.copy()
#lx = lb[:]
del lb
print(lx)
lx.clear()
print(lx)
