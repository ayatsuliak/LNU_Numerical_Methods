from math import log, log10, exp, e, pow, sqrt
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import rectangle_method as rec
import trapeze_method as trap
import sympson_method as sym

print("Hello, please select an option:\n "
      "\t1 - rectangle method\n"
      "\t2 - trapeze method\n"
      "\t3 - sympson method")
option = input()

x = Symbol('x')
f = eval(input("Enter function: "))
f = lambdify(x, f)

a, b = input("Enter limits: ").split(' ')
a = float(a)
b = float(b)

num_of_points = int(input('Enter number of points: '))

eps = float(input('Enter eps: '))

if option == '1':
    result = rec.method_of_rectangles(f, a, b, num_of_points, eps)
    print(f'Rectangles method: {result}')
elif option == '2':
    result = trap.trapeze_method(f, a, b, num_of_points, eps)
    print(f'Trapeze method: {result}')
elif option == '3':
    result = sym.sympson_method(f, a, b, num_of_points, eps)
    print(f'Sympson method: {result}')