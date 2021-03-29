#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:19:58 2021

@author: linkuanyu
"""
from Question import Question

question_prompts = [
        "What color is a banana?\n(A)red\n(B)yellow\n(C)blue\n\n",
        "What color is a carrot?\n(A)orange\n(B)purple\n(C)Green\n\n",
        "What color is an elephant?\n(A)black\n(B)white\n(C)Gray\n\n"
        # \n :next line
    ]

questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "C"),
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)