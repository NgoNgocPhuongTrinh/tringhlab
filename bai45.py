# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:52:40 2024

@author: Student
"""

s = 0
n = int(input("nhap n: "))
while n < 0:
    n = int(input("Nhap lai n: "))
x = float(input("Nhap x: "))
for i in range(1, n+1):
    s += (x**i) / i
print(round(s, 2))