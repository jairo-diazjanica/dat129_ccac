#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:30:40 2019

@author: Jairo
"""
# This short program read in string and print the first two letter
# and las last two letter of the string

def menu():
    print('********** MENU **********')
    print('1.- Insert String')
    print('2.- Exit')
    print('**************************')
    print()
    
opcionmenu = 0
menu()
while opcionmenu != 2:    
    opcionmenu = int(input("Select option: "))
    if opcionmenu == 1:
        word = str(input("please Enter the String : "))
        a = len(word)
        print('\n')
        print("Length of the String is : ", a)
        if a >= 4:
            print('\n')
            ll = a - 1
            ll2 = ll -1
            print("first two letter are : " + word[0], word[1])
            print("Last two letters are : " + word[ll2], word[ll])
            if word[1] == word[ll]:
                print('\n')
                print("The seconds letters are the SAME") 
            else:
                print('\n')
                print("Fantastic")
        else :
            print ("The Word need to be longer than 4 character ")
menu()        
print('\n')
print("**** Thank you for using the program ****" )          

    
    
