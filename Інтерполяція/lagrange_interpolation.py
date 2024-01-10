from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt


def interpolation_lagrange_polynomials(x, y, x_new, n):
    if n > len(x):
        raise ValueError("")
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    p = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                p[i] *= (x_new - x[j]) / (x[i] - x[j])
    return np.dot(y, p)


def divided_differences(x, y):
    n = len(x)
    if n == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    else:
        return (divided_differences(x[1:], y[1:]) - divided_differences(x[:n - 1], y[:n - 1])) / (x[-1] - x[0])


def finite_difference(y, i, k):
    if k == 1:
        return y[i + 1] - y[i]
    else:
        return finite_difference(y, i + 1, k - 1) - finite_difference(y, i, k - 1)


def forward_newton_interpolating_unequidistant_nodes(x, y, x_new, n):
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    if n > len(x):
        raise ValueError('')
    res = y[0]
    for i in range(1, n):
        tmp = 1
        for j in range(i):
            tmp *= x_new - x[j]
        tmp *= divided_differences(x[:i + 1], y[:i + 1])
        res += tmp
    return res


def backward_newton_interpolating_unequidistant_nodes(x, y, x_new, n):
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    if n > len(x):
        raise ValueError('')
    res = y[-1]
    for i in range(n - 2, -1, -1):
        tmp = 1
        for j in range(n - 1, i, -1):
            tmp *= x_new - x[j]
        tmp *= divided_differences(x[i:], y[i:])
        res += tmp
    return res


def forward_newton_interpolating_equidistant_nodes(x, y, x_new, n):
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


def backward_newton_interpolating_equidistant_nodes(x, y, x_new, n):
    x = np.asarray(x[:n])
    y = np.asarray(y[:n])
    h = x[1] - x[0]
    t = (x_new - x[-1]) / h
    res = y[-1]
    for i in range(n - 2, -1, -1):
        tmp = 1
        for j in range(n - 1, i, -1):
            tmp *= t + (n - j - 1)
        tmp *= finite_difference(y, i, n - i - 1) / math.factorial(n - i - 1)
        res += tmp
    return res

x = Symbol('x')
f = eval(input('Enter function: '))
f = lambdify(x, f)
a = float(input("a = "))
b = float(input("b = "))
print("1 Lagrange polynomials")
print("2 Forward Newton interpolating for unequidistant nodes")
print("3 Forward Newton interpolating for equidistant nodes")
arr_x = np.linspace(a, b, 2000)
arr_y = f(arr_x)
plt.figure()
plt.plot(arr_x, arr_y, label='f(x)')
way = int(input())
if way not in range(1, 6):
    raise ValueError("Wrong input")
if way in range(1, 3):
    x = list(map(float, input('x = ').split()))
    y = [f(i) for i in x]
    if len(x) != len(y):
        raise ValueError("x and y must be the same length")
    x_new = float(input("x_new = "))
    n = 2
    if way == 1:
        for i in range(n, len(x) + 1):
            res = interpolation_lagrange_polynomials(x, y, x_new, i)
            print(f'n = {i}, f({x_new}) = {res}')
            arr_x = x[:i]
            arr_y = y[:i]
            arr_x.append(x_new)
            arr_y.append(res)
            tmp = {arr_x[i]: arr_y[i] for i in range(len(arr_x))}
            tmp = dict(sorted(tmp.items(), key=lambda i: i[0]))
            arr_x = tmp.keys()
            arr_y = tmp.values()
            plt.plot(arr_x, arr_y, label = f'n = {i}')
    elif way == 2:
        for i in range(n, len(x) + 1):
            res = forward_newton_interpolating_unequidistant_nodes(x, y, x_new, i)
            print(f'n = {i}, f({x_new}) = {res}')
            arr_x = x[:i]
            arr_y = y[:i]
            arr_x.append(x_new)
            arr_y.append(res)
            tmp = {arr_x[i]: arr_y[i] for i in range(len(arr_x))}
            tmp = dict(sorted(tmp.items(), key=lambda i: i[0]))
            arr_x = tmp.keys()
            arr_y = tmp.values()
            plt.plot(arr_x, arr_y, label = f'n = {i}')
else:
    num_of_pts = int(input('Number of points = '))
    x = list(np.linspace(a, b, num_of_pts))
    y = [f(i) for i in x]
    if num_of_pts != len(y):
        raise ValueError("x and y must be the same length")
    x_new = float(input("x_new = "))
    n = 2
    if way == 3:
        for i in range(n, len(x) + 1):
            res = forward_newton_interpolating_equidistant_nodes(x, y, x_new, i)
            print(f'n = {i}, f({x_new}) = {res}')
            arr_x = x[:i]
            arr_y = y[:i]
            arr_x.append(x_new)
            arr_y.append(res)
            tmp = {arr_x[i]: arr_y[i] for i in range(len(arr_x))}
            tmp = dict(sorted(tmp.items(), key=lambda i: i[0]))
            arr_x = tmp.keys()
            arr_y = tmp.values()
            plt.plot(arr_x, arr_y, label = f'n = {i}')
    plt.xlabel('x')
    plt.ylabel('f(x)')

plt.legend()
plt.show()





















# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([0, 1, 3, 4, 6, 10], float)
#
# def f(x):
#     #return x**2
#     return x**3+3*x**2-1
#
# def y(f, x):
#     y = np.array([], float)
#     for i in x:
#         y = np.append(y, f(i))
#     return y
#
# y = y(f, x)
#
# #xp = float(input("x: "))
#
# # def lagrange_interpolation(xp, x, y):
# #     yp = 0
# #     for xi, yi in zip(x, y):
# #         yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))
# #
# #     return yp
#
# def lagrange_interpolation(x, y, x_new):
#     n = len(x)
#     if n > len(x):
#         raise ValueError("")
#     x = np.asarray(x[:n])
#     y = np.asarray(y[:n])
#     p = np.ones(n)
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 p[i] *= (x_new - x[j]) / (x[i] - x[j])
#     return np.dot(y, p)
#
# #print(lagrange_interpolation(xp, x, y))
#
# def graph_lagrange(x, y):
#     xplt = np.linspace(x[0], x[-1])
#     yplt = np.array([], float)
#
#     for xp in xplt:
#         yp = 0
#
#         for xi, yi in zip(x, y):
#             yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))
#         yplt = np.append(yplt, yp)
#
#     plt.plot(x, y, 'ro', xplt, yplt, 'b-')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.show()

#graph_lagrange(x, y)


# def plot_graphics(f, a, b, x, y):
#     xarr = np.linspace(a, b, 1000)
#     yy = f(xarr)
#     plt.plot(x, y, 'ro', xarr, yy)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.grid(True)
#     plt.show()

#plot_graphics(f, -1, 10, x, y)