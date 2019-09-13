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

# Challenge 1: Another way whit for command
start = 0
end = 100
print ('\n')  
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")

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

# Challenge 4:
a = 1
while a <= 4:
    b = 5
    while b <= 7:
        c = a * b
        print(a," | ", b, " | ", c)
        b = b + 1
    a = a + 1
    


   

    