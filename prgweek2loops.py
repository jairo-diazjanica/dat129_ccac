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
   

    