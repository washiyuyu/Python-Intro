#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:01:33 2020

@author: linkuanyu
"""

import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("Number Guessing Game")


label1 = tk.Label(root, text="Type-in Num", font=("Courier", 14))
label1.place(x = 20, y = 20)


editbox1 = tk.Entry(width = 4, font=("Courier", 28))
editbox1.place(x = 120, y = 60)


root.mainloop()