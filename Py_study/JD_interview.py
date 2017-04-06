#coding=utf-8
#1. string list with word:  ab3 he 12HM  D3  》》》 output D3 12HM he ab3 ?
#Need (N), think about exception,think about 100W ,how to do?

tList = "ab3 he 12HM  D3"
#print(tList.split(" "))

def reverse_list(tList):
    stack = []
    for i in range(len(tList.split(" "))):
        stack.append(tList.split(" ")[i])
    while stack:
        print(stack.pop())

reverse_list(tList)
