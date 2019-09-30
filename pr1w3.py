#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:00:44 2019

@author: Jairo
"""

# This program design Dictionary whose keys describe what values
# you'd like to learn about your peer in this class.
def menu():
    print('********** MENU **********')
    print('1.- Insert Student List Name')
    print('2.- Insert Sport List')
    print('3.- Insert Data dict')
    print('4.- Show Data')
    print('5.- Exit')
    print()

def menu2():
    print('a.- Search by Name')
    print('b.- Search by Sport')

def menu3():
    print("Edit Data")
    print('1.- Delete Data')
    print('2.- Change Data')

dict = {}
student_name = {}
sport_list = {}

# dict = {dicname: sportmach}
# student_name = {cs: name}
# sport_list = {csp: snma}
 
opcionmenu = 0
menu()
x=0


while opcionmenu != 5:
    opcionmenu = int(input("Select option: "))

    if opcionmenu == 1:
        student_number = int(input("How many Students : "))
        cs=1        
        while cs <= student_number :
            name = input("Insert Student Name :")
            student_name[cs] = name
            cs = cs + 1
        menu()

    elif opcionmenu == 2:
        sport_number = int(input("How many Sports : "))
        csp=1        
        while csp <= sport_number :
            sname = input("Insert Sport Name :")
            sport_list[csp] = sname
            csp = csp + 1
        menu()       
   
    elif opcionmenu == 3:
        print(student_name)
        print(sport_list)
        cs = 1
        print('\n')
        while cs <= student_number :
            print(student_name[cs])
            dicname = student_name[cs]
            sportmach = input("Insert what Sport He/She like it :")
            print('\n')
            dict[dicname] = sportmach
            cs = cs + 1
        print('\n')
        print("*************************************************")
        print("***** DICTIONARY *********")
        print(dict)
        print("*************************************************")
        menu()
       
    elif opcionmenu == 4:       
        for diname, disport in dict.items():
            print('\n')
            print("NAME : " + diname + "  - LIKE --> : " + dict[diname])         
        print('\n')
        menu()
        
#          
            
    
       
            
        