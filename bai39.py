# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:29:48 2024

@author: Student
"""

s = 0
n = int(input("Nhap n: "))
while n < 0:
    n = int(input("Nhap lai n: "))
for  i in range(n, n+1):
    s += 1/n 
print(round(s,2))