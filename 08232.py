#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:30:37 2020

@author: linkuanyu
"""

import tkinter as tk


x = 400
y = 300

def move():
    global x, y
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="gray", width = 0)
    x = x + 2
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="pink", width = 0)
    root.after(10, move)
    

root = tk.Tk()
root.geometry("600x400")


canvas =  tk.Canvas(root, width = 600, height = 400, bg = "gray")
canvas.place(x = 0, y = 0)


root.after(10, move)


root.mainloop()