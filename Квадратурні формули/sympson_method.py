from sympy import *
import numpy as np
from math import log, log10, exp, e, pow, sqrt

def f(x):
    #return 1/(1+x**2)
    return 3*x**2

def sympson_method(f, a, b, num_of_points, eps):
    S = f(a) + f(b)
    h = (b - a) / (num_of_points)
    for i in range(1, num_of_points):
        k = a + i * h
        if i % 2 == 0:
            S += 2 * f(k)
        else:
            S += 4 * f(k)

    result = S * h/3

    return result

#print(sympson_method(f,0,1,1000))