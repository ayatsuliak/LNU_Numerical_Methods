from math import log, log10, exp, e, pow, sqrt
import numpy as np
from sympy import *
import lagrange_interpolation as lag
import unequidistant_nodes as uneq
import equidistant_nodes as eq

print("Hello, please select an option:\n "
      "\t1 - lagrange interpolation\n"
      "\t2 - unequidistant nodes\n"
      "\t3 - equidistant nodes")
option = input()

x = Symbol('x')
f = eval(input('Enter function: '))
f = lambdify(x, f)

n = int(input('Enter degree of the polynomial: '))
x = np.array([], float)
for i in range(1, n+1):
    xi = float(input(f'Enter x{i}: '))
    x = np.append(x, xi)

def y(f, x):
    y = np.array([], float)
    for i in x:
        y = np.append(y, f(i))
    return y

y = y(f, x)

xp = float(input('Enter wanted x: '))

if option == '1':
    result = lag.lagrange_interpolation(xp, x, y)
    print(f'Lagrange interpolation: {result}' )
    ask = str(input('Draw a graph? '))
    if ask == 'yes':
        lag.graph_lagrange(x, y)
elif option == '2':
    result = uneq.forward_unequidistant_nodes(xp, x, y)
    print(f'Newton unequidistant nodes: {result}')
    ask = str(input('Draw a graph? '))
    if ask == 'yes':
        uneq.graph_lagrange(x, y)
elif option == '3':
    result = eq.forward_equidistant_nodes(xp, x, y)
    print(f'Newton equidistant nodes: {result}')
    ask = str(input('Draw a graph? '))
    if ask == 'yes':
        eq.graph_lagrange(x, y)