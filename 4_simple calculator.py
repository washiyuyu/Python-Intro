#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:36:12 2021

@author: linkuanyu
"""

num1 = float(input("Enter first number: "))
#value we get from input is always converted into a string
#use float() to convert value into number

op = input("Enter operator: ")
num2 = float(input("Enter Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")