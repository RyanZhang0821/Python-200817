# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:38:06 2020

@author: user
"""

Math=int(input("type Math score:"))
English=int(input("type English score:"))
if Math >=90 and English >=90:
    print("U earn a price!")
if Math >=60 or English <=60:
    print("So sad god bless u")
if Math <=60 or English >=60:
    print("So sad god bless u")

if Math <=60 and English<=60:
    print("Punishment!")