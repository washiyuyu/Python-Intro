#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:01:33 2020

@author: linkuanyu
"""

import random
import tkinter as tk
import tkinter.messagebox as tmsg 


def ButtonClick1():
    b = editbox1.get()

    flag = False
    if len(b) != 4:
        tmsg.showerror("wrong!", "type-in 4 nums")
    else:
        nums = True
        for i in range(4):
            if (b[i] <"0") or (b[i] > "9"):
                tmsg.showerror("wrong!", "it should be num")
                nums = False
                break
        if nums:
            flag = True
    if flag:
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

    if hit == 4:
        tmsg.showinfo("correct!", "You win!")
        root.destroy()
    else:
        recordbox.insert(tk.END, b + " /H:" + str(hit) + " B:" + str(blow) + "\n")


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),]


def ButtonClick2():
    tmsg.showinfo("test2", "哈哈哈哈哈")


root = tk.Tk()
root.geometry("600x400")
root.title("Number Guessing Game")


recordbox = tk.Text(root, font=("Courier", 14))
recordbox.place(x=400, y=0, width=200, height= 400)


label1 = tk.Label(root, text="Type-in Num", font=("Courier", 14))
label1.place(x = 20, y = 20)


editbox1 = tk.Entry(width = 4, font=("Courier", 28))
editbox1.place(x = 120, y = 60)


button1 = tk.Button(root, text="send", font=("Courier", 14), command=ButtonClick1)
button1.place(x = 220, y = 60)


button2 = tk.Button(root, text="hahaha", font=("Courier", 14), command=ButtonClick2)
button2.place(x = 280, y = 60)


root.mainloop()