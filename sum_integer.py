#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:43:21 2019

@author: Jairo
"""
# This short program read for an Integer and make a list of the number
# and show the total sum of the numbers

def menu():
    print('********** MENU **********')
    print('1.- Insert the Number')
    print('2.- Exit')
    print('**************************')
    print()
    
opcionmenu = 0
menu()
print('\n')
while opcionmenu != 2:    
    opcionmenu = int(input("Select option: "))
    if opcionmenu == 1:
        num = int(input("please Enter the Number : "))
        s = 0
        k = 0
        while s <= num:
            k = k + s
            print(s, end = " ")
            s = s + 1 
        print('\n')
        print('The sum of the number is : -->  ', k) 
menu()
print('\n')
print("**** Thank you for using the program ****" )        
