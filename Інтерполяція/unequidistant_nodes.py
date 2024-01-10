import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 3, 4, 6, 10], float)

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

def divided_differences(x, y):
    n = len(x)
    if n == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    else:
        return (divided_differences(x[1:], y[1:]) - divided_differences(x[:n - 1], y[:n - 1])) / (x[-1] - x[0])

def forward_unequidistant_nodes(x_new, x, y):
    n = len(x)
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    result = y[0]
    for i in range(1, n):
        tmp = 1
        for j in range(i):
            tmp *= x_new - x[j]
        tmp *= divided_differences(x[:i + 1], y[:i + 1])
        result += tmp
    return result
#print(forward_unequidistant_nodes(xp, x, y, len(x)))

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




























# def coef(x, y):
#     x.astype(float)
#     y.astype(float)
#     n = len(x)
#     a = []
#     for i in range(n):
#         a.append(y[i])
#
#     for j in range(1, n):
#         for i in range(n-1, j-1, -1):
#             a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
#
#     return np.array(a) # return an array of coefficient
#
# def Eval(a, x, r):
#     x.astype(float)
#     n = len( a ) - 1
#     temp = a[n] + (r - x[n])
#     for i in range( n - 1, -1, -1 ):
#         temp = temp * ( r - x[i] ) + a[i]
#     return temp