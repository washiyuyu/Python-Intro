#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:00:54 2020

@author: linkuanyu
"""

import tkinter as tk


def click(event):
    canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill="pink", width = 0)


root = tk.Tk()
root.geometry("600x400")


canvas =  tk.Canvas(root, width = 600, height = 400, bg = "gray")
canvas.place(x = 0, y = 0)


canvas.bind("<Button-1>", click)


root.mainloop()