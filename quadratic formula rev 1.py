# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:41:11 2020

@author: Jaz
"""
#quadratic eqn solver
print("Quadratic equation solver for real solutions")
print(" ax^2 + bx + c ")
#while True handles exceptions for string inputs
while True:
    try:
        a = float(input('what is the a value = '))
        b = float(input('what is the b value = '))
        c = float(input('what is the c value = '))
        break
    except ValueError:
        print("Please input a real number")
#float function converts the inputs from strings to floating point numbers (decimals)
d = (b**2) - (4*a*c)
#d is the discriminant
#elif is used as d conditions are mutually exclusive to each other
if d < 0 :
    print("This equation has no real roots")
elif d==0:
    x = (-b / (2*a))
    print("The equation has one root, x =" , x)
else:
    x1 = ((-b + (d**(0.5))) / (2*a))
    x2 = ((-b - (d**(0.5))) / (2*a))
    print("The equation has two roots, x =" , x1 ,"or x =", x2)