#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:10:48 2020

@author: linkuanyu
"""

# coding:utf-8

import random

a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),]
#print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True:
    flag = False
    while flag == False:
        b = input("type-in nums>")
        if len(b) != 4:
            print("please type-in 4 nums")
        else:
            nums = True
            for i in range(4):
                if (b[i] <"0") or (b[i] > "9"):
                    print("it should be num")
                    nums = False
                    break
            if nums:
                flag = True
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit = hit +1

    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                blow = blow +1
                break
    print("hit"+str(hit))
    print("blow"+str(blow))

    if hit == 4:
        print("You win!")
        break
    

