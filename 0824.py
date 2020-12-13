#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:53:32 2020

@author: linkuanyu
"""
import tkinter as tk


class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        
    def move(self, canvas):
        self.erase(canvas)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.draw(canvas)
        if (self.x >= canvas.winfo_width()):
            self.dx = -1
        if (self.x <= 0):
            self.dx = 1
        if (self.y >= canvas.winfo_height()):
            self.dy = -1
        if (self.y <= 0):
            self.dy = 1
            
    def erase(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="gray", width = 0)
 
    def draw(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color, width = 0)
            
class Rectangle(Ball):
    def erase(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="gray", width = 0)
 
    def draw(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color, width = 0)

class Triangle(Ball):
    def erase(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill="gray", width = 0)
 
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill=self.color, width = 0)


class Six(Ball):
    def erase(self, canvas):
        canvas.create_polygon(self.x + 10, self.y - 20, self.x - 10, self.y - 20, self.x - 20, self.y, self.x - 10, self.y + 20, self.x + 10, self.y + 20, self.x + 20, self.y, fill="gray", width = 0)
 
    def draw(self, canvas):
        canvas.create_polygon(self.x + 10, self.y - 20, self.x - 10, self.y - 20, self.x - 20, self.y, self.x - 10, self.y + 20, self.x + 10, self.y + 20, self.x + 20, self.y, fill=self.color, width = 0)



balls = [
    Ball(400, 300, 1, 1, "pink"),
    Rectangle(300, 150, -1, 1, "light blue"),
    Triangle(100, 250, 1, -1, "light green"),
    Six(250, 50, -1, -1, "light yellow")
]


def loop():
    for b in balls: 
        b.move(canvas)
    root.after(10,loop)
    
    
root = tk.Tk()
root.geometry("800x600")


canvas = tk.Canvas(root, width = 800, height = 600, bg="gray")
canvas.place(x = 0, y = 0)


root.after(10, loop)

root.mainloop()