#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:53:26 2021

@author: linkuanyu
"""

"""
vowel -> l

dog -> dlg
cat -> clt
"""

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "L"
            else:
                translation = translation + "l"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))

# variable_name.isupper() to check if there is any upper letter in the variable_name
# variable_name.lower() to make all the letter become lower letter