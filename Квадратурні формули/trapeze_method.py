from sympy import *
import numpy as np
from math import log, log10, exp, e, pow, sqrt

def f(x):
    #return 1/(1+x**2)
    return 3*x**2

def trapeze_method(f, a, b, num_of_points, eps):
    h = (b - a) / (num_of_points)
    S = (np.sum([f(a + i*h) for i in range(num_of_points)]) + (f(a)+f(b))/2) * h

    num_of_points *= 2
    h = (b - a) / (num_of_points)
    S2 = (np.sum([f(a + i * h) for i in range(num_of_points)]) + (f(a) + f(b)) / 2) * h

    while abs(S2-S) > eps:
        S = S2
        num_of_points *= 2
        h = (b - a) / (num_of_points)
        S2 = (np.sum([f(a + i * h) for i in range(num_of_points)]) + (f(a) + f(b)) / 2) * h
    return S

#print(trapeze_method(f,0,1,1000, 0.01))