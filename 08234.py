#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:09:02 2020

@author: linkuanyu
"""


import tkinter as tk

balls = [
    {"x" : 400, "y" : 300, "dx" : 1, "dy" : 1, "color" : "pink"},
    {"x" : 200, "y" : 150, "dx" : -1, "dy" : 1, "color" : "light green"},
    {"x" : 100, "y" : 250, "dx" : 1, "dy" : -1, "color" : "light blue"}
]


def move():
    global balls
    for b in balls:
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill="gray", width = 0)
        b["x"] = b["x"] + b["dx"]
        b["y"] = b["y"] + b["dy"]
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill=b["color"], width = 0)
        if b["x"] >= canvas.winfo_width():
            b["dx"] = -1
        if b["x"] <= 0:
            b["dx"] = +1
        if b["y"] >= canvas.winfo_height():
            b["dy"] = -1
        if b["y"] <= 0:
            b["dy"] = +1
    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")


canvas =  tk.Canvas(root, width = 600, height = 400, bg = "gray")
canvas.place(x = 0, y = 0)


root.after(10, move)


root.mainloop()
