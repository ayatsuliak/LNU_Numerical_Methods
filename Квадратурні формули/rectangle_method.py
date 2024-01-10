import numpy as np
from sympy import *
import numpy as np
from math import log, log10, exp, e, pow, sqrt

def f(x):
    #return 1/(1+x**2)
    return 3*x**2

def method_of_rectangles(f, a, b, num_of_points, eps):
    points = np.linspace(a, b, num_of_points)
    h = (b - a) / (num_of_points)
    S = np.sum([f(points[i]) for i in range(num_of_points)]) * h

    num_of_points *= 2
    points = np.linspace(a, b, num_of_points)
    h = (b - a) / (num_of_points)
    S2 = np.sum([f(points[i]) for i in range(num_of_points)]) * h

    while abs(S2-S) > eps:
        S = S2
        points = np.linspace(a, b, num_of_points)
        h = (b - a) / (num_of_points)
        S2 = np.sum([f(points[i]) for i in range(num_of_points)]) * h

    return S2

#print(method_of_rectangles(f,0,1,1000, 0.01))