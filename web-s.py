#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:46:58 2019

@author: Jairo
"""

# My First scraping

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.python.org/")
res = BeautifulSoup(html.read(),"html5lib");

print('********************')
print(res.title)
print('********************')





