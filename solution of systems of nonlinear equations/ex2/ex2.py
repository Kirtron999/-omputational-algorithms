import math
import matplotlib.pyplot as plt
import numpy as np


def f1(x1, a):
    return (x1 + 0.5*a)**(1/3.0)


def f2(x1, a):
    return math.cos(2 * x1) - a


def f1_true(x1, x2, a):
    return x1 - (x2**3) + 0.5*a


def f2_true(x1, x2, a):
    return math.cos(2*x1) - x2 - a


def lineplot(x_data, y_data, x_data2, y_data2, x_label="X1", y_label="X2", title="Localization"):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=1, color='#539caf', alpha=1)
    ax.plot(x_data2, y_data2, lw=1, color='#230caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def W(x1, x2):
    jacoby = [[0.0] * 2 for i in range(2)]
    jacoby[0][0] = 1
    jacoby[0][1] = (-3)*(x2**2)
    jacoby[1][0] = (-2) * math.sin(2 * x1)
    jacoby[1][1] = -1
    return jacoby


def F(x1, x2, a):
    matrix = list()
    matrix.append(-f1_true(x1, x2, a))
    matrix.append(-f2_true(x1, x2, a))
    return matrix


def simplified_newton_method(x0, a):
    x_start = x0
    e = 10**(-5)
    k = 0
    while True:
        detX = np.linalg.solve(np.array(W(x0[0], x0[1])), np.array(F(x_start[0], x_start[1], a)))
        x_next = x_start + detX
        if max(math.fabs(x_next[0] - x_start[0]), math.fabs(x_next[1] - x_start[1])) <= e:
            print(x_next)
            print(k + 1)
            break
        else:
            k += 1
            x_start = x_next


a = [0, 1, -0.5]

a00 = [0.38, 0.72]

print("a = 0:")
simplified_newton_method(a00, a[0])


print("a = 1: no roots")

a02 = [0.66, 0.74]


print("a = -0.5")
simplified_newton_method(a02, a[2])
