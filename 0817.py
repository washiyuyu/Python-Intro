#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:02:15 2020

@author: linkuanyu


#1
a=1
print(a)

#2
a=1
b=2
print(a+b)

#3
for i in [1,2,3,4,5]:
    print(i)

#4
for i in [1,2,3,4,5]:
    print(i)
    print("Hello")

#5
for i in [1,2,3,4,5]:
    print(i)
print("Hello")

#6
for i in range(1,100+1):
    print(i)

#7
for i in "Hello":
    print(i)

#8
total = 0
a = 1
while total <= 50 :
    total = total + a
    a = a + 1
print(total)

#9 !!!
for i in range(5):
    print(i+1)

i = 1
while i <= 5 :
    print(i)
    i = i + 1

#10
for i in range(10):
    if i < 5:
        print("小的")
    else:
        print("大的")

#11
for i in range(1,10+1):
    print(i)
    if i % 2 == 0:
        print("○")
    if i % 3 == 0:
        print("□")
    if (i % 2 == 0) and (i % 3 == 0):
        print("△")

#12
for i in range(1,12+1):
    print(i)
    if i % 12 == 0:
        print("○")
    elif i % 4 == 0:
        print("△")
    elif i % 2 == 0:
        print("x")
    else:
        print("☆")
"""
#九九乘法表
a = 1
b = 1
for a in range(1,1+9):
    for b in range(1,1+9):
        print(str(a)+"X"+str(b)+"="+str(a*b))
        b = b + 1