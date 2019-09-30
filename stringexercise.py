#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:30:40 2019

@author: Jairo
"""
# This short program read in string and print the first two letter
# and las last two letter of the string
word = str(input("please Enter the String : "))
a = len(word)
print(a)
if a >= 4:
    ll = a - 1
    ll2 = ll -1
    print("primera two letter are : " + word[0], word[1])
    print("Last two letters are : " + word[ll2], word[ll]) 
 
else :
    print ("The Word need to be longer than 4 character ")
    
    
    
    
    
    
