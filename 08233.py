#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:46:54 2020

@author: linkuanyu
"""


import tkinter as tk


x = 400
y = 300
dx = 1


def move():
    global x, y, dx
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="gray", width = 0)
    x = x + dx
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="pink", width = 0)
    if x >= canvas.winfo_width():
        dx = -1
    if x <= 0:
        dx = +1
    root.after(10, move)
    

root = tk.Tk()
root.geometry("600x400")


canvas =  tk.Canvas(root, width = 600, height = 400, bg = "gray")
canvas.place(x = 0, y = 0)


root.after(10, move)


root.mainloop()