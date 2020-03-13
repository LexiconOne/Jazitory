# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:04:41 2020

@author: user
"""
print("Surface area and volume of a sphere calculator")
pi = 3.1415926535898
#refer to quadratic formula rev 1 for further clarifications
while True:
    try:
        r = float(input('Please input the radius of the sphere = '))
        break
    except ValueError:
        print("Please input a real number (Do not include the units, just the value)")
s = 4 * pi * (r**2)
v = (4/3) * pi * (r**3)
print("The surface area of the sphere is" , s , "units", "while the volume is" , v , "units")