import math
import numpy as np


def f1(x1, x2):
    return math.tan(x1 * x2) - x1**2


def f2(x1, x2):
    return 0.7*x1**2 + 2*x2**2 - 1


def W(x1, x2):
    jacoby = [[0]*2 for i in range(2)]
    jacoby[0][0] = x2/((math.cos(x1 * x2))**2) - 2*x1
    jacoby[0][1] = x1/((math.cos(x1 * x2))**2)
    jacoby[1][0] = 1.4*x1
    jacoby[1][1] = 4*x2
    return jacoby


def F(x1, x2):
    matrix = list()
    matrix.append(-f1(x1, x2))
    matrix.append(-f2(x1, x2))
    return matrix


def newton_method(x0):
    x_start = x0
    e = 10**(-6)
    k = 0
    while True:
        detX = np.linalg.solve(np.array(W(x_start[0], x_start[1])), np.array(F(x_start[0], x_start[1])))
        x_next = x_start + detX
        if max(math.fabs(x_next[0] - x_start[0]), math.fabs(x_next[1] - x_start[1])) <= e:
            print(x_next)
            print(k + 1)
            break
        else:
            k += 1
            x_start = x_next
            print(x_next)


x01 = [0.65, 0.6]
x02 = [-0.65, -0.6]

newton_method(x01)
newton_method(x02)


