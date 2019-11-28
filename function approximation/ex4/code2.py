import math
import numpy
import matplotlib.pyplot as plt


def lineplot(x_data, y_data, x_data2, y_data2, x_label="X", y_label="Y", title="Approximation"):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, 'o', lw=2, color='#539caf', alpha=1)
    ax.plot(x_data2, y_data2, lw=2, color='#230caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


a = 2
b = 3

X = list()
Y = [2.002, 1.7937, 0.39, -0.9052, -1.0023, 0.0001, 1.0025, 0.9054, -0.37, -1.7940, -2.003, -0.5597, 1.6174, 2.9025, 2.2468, 0.001, -2.2365, -2.902, 1.6172, 0.5593, 2.0004]
YArr = list()

for i in range(0, 21):
    X.append(-1 + 0.1 * i)


P = [[0] * 2 for i in range(21)]
for i in range(0, 21):
    P[i][0] = math.sin(a * math.pi * X[i])
    P[i][1] = math.cos(b * math.pi * X[i])


X = numpy.array(X)
Y = numpy.array(Y)
P = numpy.array(P)

PT = P.transpose()

Gram = PT @ P

B = PT @ Y

A = numpy.linalg.solve(Gram, B)
print("C1 = ", A[0], " | C2 = ", A[1])


def countYArr(value):
    return A[0]*math.sin(a * math.pi * value) + A[1]*math.cos(b * math.pi * value)


for item in X:
    YArr.append(countYArr(item))

lineplot(X, Y, X, YArr)


