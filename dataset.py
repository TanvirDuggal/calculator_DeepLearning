# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:09:31 2020

@author: Tanvy
"""


import random
import pandas as pd

dt  = []
for i in range(1000000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    c = str(a) + ",+," + str(b) + ","
    dt.append(c + str(a+b))
    
for i in range(1000000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    c = str(a) + ",-," + str(b) + ","
    dt.append(c + str(a-b))
    
for i in range(1000000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    c = str(a) + ",/," + str(b) + ","
    dt.append(c + str(a/b))
    
for i in range(1000000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    c = str(a) + ",*," + str(b) + ","
    dt.append(c + str(a*b))
    
df = pd.DataFrame(dt)
df.to_csv("dataset.csv", header=None, index=None)
