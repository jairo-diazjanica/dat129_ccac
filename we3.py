#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:29:07 2019

@author: Jairo
"""
n = int(input("Enter the number of row: "))
for row in range (n,0,-1):
    for col in range (1, row+1):
        print(col, end = " ")
    print()
 

