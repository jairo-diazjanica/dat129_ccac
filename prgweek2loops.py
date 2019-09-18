# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:46:27 2019

@author: jairo_000
"""

# Challenge 1:
start = 0
while start <= 100:
    print(start, end=" ")
    start = start + 2
#

# Challenge 1: Another way with for command
start = 0
end = 100
print ('\n')  
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")
#
        
# Challenge 2:
print ('\n')
w = "KABOOM"
for r in w:
    s = r*3
    print(s, end="")
#
# Another way Challenge 2: with out loops
print ("\n")
w = "KABOOM"
k,a,b,o,m = ("K"*3,"A"*3, "B"*3,"O"*6,"M"*3)
print(k,a,b,o,m)

#
# Challenge 3:
print ("\n")
a = "askaliceithinkshe'llknow"
b = -1
for i in a:
    b = b + 1
    if b % 2 == 0:
        print(a[b], end = " ")
        
#
# Challenge 4:
print ('\n') 
a = 1
while a <= 4:
    b = 5
    while b <= 7:
        c = a * b
        print(a," | ", b, " | ", c)
        b = b + 1
    a = a + 1
    
# Challenge 5:
print ('\n') 
listoflists = [['mn','pa','ut'],['b','p','c'],['echo','charlie','tango']]
labels = {"state":"US State Abbr: ", "element":"Chemical Element: ", "alpha":"Phonetic Call: "}
x = 0
y = 0
while y <=2:
    print(labels['state'], listoflists[x][y])
    y = y + 1
x = x + 1
y = 0
while y <=2:
    print(labels['element'], listoflists[x][y])
    y = y + 1
x = x + 1
y = 0  
while y <=2:
    print(labels['alpha'], listoflists[x][y])
    y = y + 1
   
# Challenge 6:
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:14:16 2019

@author: Jairo
"""

# This program stores information about Schools.
# For each School, we store the program of School,
# The Director name, and phone_number.
schools = dict()

schools ={'public': {'program': 'IT','director_name': 'jairo', 'phone_number': '(123)456-7421'},
        'private': {'program': 'med', 'director_name': 'tyler', 'phone_number': '(726)853-9234'},
        'semi':{'program': 'law', 'director_name': 'valerie', 'phone_number': '(514)777-5125'}} 
numElem = len(schools)
print('\n')
print("Number of element in the Dictionary--->",numElem)


# Show all the information for each school.
for school_name, school_information in schools.items():
    print('\n')
    print("Here is what I know about %s school:" % school_name.title())
    print("program: " + school_information['program'])
    print("director_name: " + school_information['director_name'])
    print("phone_number: " + str(school_information['phone_number']))

# Show the type that are currently in the dictionary.
print('\n')
print("The following School have been defined:")
print('\n')
for type in schools:
    print("- %s" % type)
print('\n')  

request = ''
while request != 'quit':
    # Allow the user to choose a type of School he/she want info.
    request = input("\nWhat School would you like to get info ? (or 'quit') ")
    if request in schools.keys():
#       print("\n  %s: %s" % (request, schools[request]))
        
        print("Program: " + schools[request]['program'])
        print("Director Name: " + schools[request]['director_name'])
        print("Phone Number: " + schools[request]['phone_number'])
    else:
        # Handle misspellings, and words not yet stored.
        print("\n  Sorry, I don't know that school.")
# 
# Add another type of School
add_school = ''
add_program = ''
add_director = ''
add_phone = ''

while add_school != 'quit':
    # Allow the user to ADD a type of School 
    add_school = input("\nWhat School would you like to ADD? (or 'quit') ")
    if add_school =='quit':
        break
    add_program = input("\nADD new Program: ")
    add_director = input("\nADD Director Name: ")
    add_phone = input("\nADD Phone Number ")
    schools[add_school]= {'add_program','add_director', 'add_phone'}
print('\n')

# I want to make copy of the Directory, and delete one key
# from the copy . and we keep the original too
schoolscopy = schools.copy()


    
#    print(schools)  
  
    