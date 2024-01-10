import numpy as np
import math
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10], float)

def f(x):
    return x**2
    #return x**3+3*x**2-1

def y(f, x):
    y = np.array([], float)
    for i in x:
        y = np.append(y, f(i))
    return y

y = y(f, x)

#xp = float(input("x: "))

def finite_difference(y, i, k):
    if k == 1:
        return y[i + 1] - y[i]
    else:
        return finite_difference(y, i + 1, k - 1) - finite_difference(y, i, k - 1)

def forward_equidistant_nodes(x_new, x, y):
    n = len(x)
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    h = x[1] - x[0]
    t = (x_new - x[0]) / h
    res = y[0]
    for i in range(1, n):
        tmp = 1
        for j in range(i):
            tmp *= t - j
        tmp *= finite_difference(y, 0, i) / math.factorial(i)
        res += tmp
    return res

#print(forward_equidistant_nodes(xp, x, y ,len(x)))

def graph_lagrange(x, y):
    xplt = np.linspace(x[0], x[-1])
    yplt = np.array([], float)

    for xp in xplt:
        yp = 0

        for xi, yi in zip(x, y):
            yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))
        yplt = np.append(yplt, yp)

    plt.plot(x, y, 'ro', xplt, yplt, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()