#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:38:26 2019

@author: Jairo
"""
# cvs file of Jail Cesus Data - Class Week 3
import csv
file = open('jail.csv',newline='')
reader = csv.DictReader(file)
totblack = 0
totwhite = 0
#censusdate = '2019-06-01'
censusdate = '2018-01-01'
for row in reader:
    if row['date'] == censusdate:
        if row['race']=='B':
            totblack = totblack + 1
        elif row['race']=='W':
            totwhite = totwhite + 1
file.close()

print('total white count on ', censusdate,' are --> ', totwhite)
print('total Black count on ', censusdate, 'are --> ', totblack)

            
            


