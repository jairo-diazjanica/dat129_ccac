#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:24:52 2019

@author: Jairo
"""

# This program stores information about Schools.
# For each School, we store the program of School,
# The Director name, and phone_number.
def menu():
    print('********** MENU **********')
    print('1.- Insert Directory Name')
    print('2.- Insert Data')
    print('3.- Search in the Directory')
    print('4.- Edit Data')
    print('5.- Show Data')
    print('6.- Exit')
    print()

def menu2():
    print('a.- Search by Director Name')
    print('b.- Search by Phone Number')

def menu3():
    print("Edit Data")
    print('1.- Delete Data')
    print('2.- Change Data')

directory = []
phone_number = {}
program = {}
director_name = {}

opcionmenu = 0
menu()
x=0
while opcionmenu != 6:
    opcionmenu = int(input("Select option: "))
    if opcionmenu == 1:
        print('Insert Directory Name :')
        nombre_de_lista=input()
        menu()


    elif opcionmenu == 2:
        print("Insert Program Name, Director Name and Phone Number ")
        progr = input("Program: ")
        name = input("Director Name : ")
        phone = input("Phone : ")


        phone_number[name] = phone
        director_name[phone] = name
        program[progr] = name
        directory.append([progr, name, phone])
        menu()

    elif opcionmenu == 3:
        print("Search")
        menu2()
        opcionmenu2 = input("Insert a letter as option: ")
        if opcionmenu2 == "a":
            progr = input("Director Name: ")
            if progr in phone_number:
                print("The Phone number is ", phone_number[progr])
            else:
                print(progr, "not found it")

        if opcionmenu2 == "b":
            phone = input("Director Phone: ")
            if phone in director_name:
                print("The Name is ", director_name[phone])
            else:
                print(phone, "not found it")

        menu()
    elif opcionmenu == 4:
        menu3()
        opcionmenu3 = input("Insert a number to option: ")
        if opcionmenu3 == "1":
            progr = input("Program: ")
            index = None
            for i in range(len(directory)):
                if directory[i][0] == progr:
                    index = i
                    break
            if index != None:
                del directory[index]
                print('deleted')
            else:
                print(progr, "not found it")
        elif opcionmenu3 == "2":
            progr = input("Program: ")
            # Editar - primero hay buscar el registro
            index = None
            for i in range(len(directory)):
                if directory[i][0] == progr:
                    index = i
                    break
            if index != None:
                print('Omite aquellos campos que no quieras editar para conservar los datos')
                progr = input('Program:')
                phone = input('Phone: ')
                name = input('Director Name')

                directory[index] = [
                    progr if len(progr) > 0 else directory[index][0],
                    name if len(name) > 0 else directory[index][1],
                    phone if len(phone) > 0 else directory[index][2],    
                ]
                print('Edit was excellent!')
            else:
                print('The user is not in the Directory')

    elif opcionmenu == 5:

        print("\nDirectory Name : ",nombre_de_lista)
        for e in directory:
            print("\nThe Data is : ",directory)
        menu()


    elif opcionmenu != 6:
        menu()





