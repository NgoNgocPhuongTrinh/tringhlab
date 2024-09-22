# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:46:52 2024

@author: Student
"""

s = 0
n = int(input("nhap n: "))
while n < 0:
    n = int(input("Nhap lai n: "))
for i in range(1, n+1):
    s += 1/(i*(i+1))
print(round(s, 2))