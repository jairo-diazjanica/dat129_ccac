#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:18:01 2019

@author: Jairo
"""
# This program download text file
print('\n')

k = open('exe2w3.txt','r')
m = k.read()
print("***** txt file link- Week 3 exercise 2 *****")
print(m)
print("*************************")
print('\n')
print("***** OUTPUT *****")


with open('exe2w3.txt','r') as f:
    for i in f.readlines():
        temp = i.split()
        name, lname = temp[0], temp[1]
#        print(name, lname)
        print("Good evening Dr.", lname + "  Would you mind if I call you ", name + "?")
   # m = f.read().split("\n")
