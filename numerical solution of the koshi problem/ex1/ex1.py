import math
import matplotlib.pyplot as plt


def lineplot(x_data, y_data, x_data2, y_data2, x_label="T", y_label="Y", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=1, color='#539caf', alpha=1)
    ax.plot(x_data2, y_data2, lw=1, color='#130caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def euler(h, t0, y0, stop, TArr, YArr):
    TArr.append(t0)
    YArr.append(y0)
    t = t0
    y = y0
    while t <= stop:
        y += h * function(t, y)
        t += h
        TArr.append(t)
        YArr.append(y)


def runge_kutta(h, t0, y0, stop, TArr, YArr):
    TArr.append(t0)
    YArr.append(y0)
    t = t0
    y = y0
    while t <= stop:
        k0 = function(t, y)
        k1 = function(t + h/2, y + h*(k0/2))
        k2 = function(t + h/2, y + h*(k1/2))
        k3 = function(t + h, y + h*k2)
        y += (h/6)*(k0 + 2*k1 + 2*k2 + k3)
        t += h
        TArr.append(t)
        YArr.append(y)


def function(t, y):
    return -(y/(2*t)) + t**2  # функция первой производной


def accurate_solution(t):
    return ((2*(t**3))/7) + (5/(7*(t**0.5)))


h = 0.1
t0 = 1
T = 2
y0 = 1
TArr = list()
YArr = list()
YAcc = list()

euler(h, t0, y0, T, TArr, YArr)

i = t0
j = 0
YAcc.append(accurate_solution(TArr[j]))
while i <= T:
    j += 1
    i += h
    YAcc.append(accurate_solution(TArr[j]))

print(" T  -  True  -  Euler")
i = 0
while i < len(TArr):
    print(TArr[i], " - ", YAcc[i], " - ", YArr[i])
    i += 1

lineplot(TArr, YAcc, TArr, YArr)

Max = 0
i = 0
while i < len(TArr):
    if math.fabs(YAcc[i] - YArr[i]) > Max:
        Max = math.fabs(YAcc[i] - YArr[i])
    i += 1
print("Error 1: ", Max)

TErr = list()
YErr = list()
euler(h/2, t0, y0, T, TErr, YErr)

YAcc = list()
i = t0
j = 0
YAcc.append(accurate_solution(TErr[j]))
while i <= T:
    j += 1
    i += h/2
    YAcc.append(accurate_solution(TErr[j]))

Max = 0
i = 0
while i < len(TErr):
    if math.fabs(YAcc[i] - YErr[i]) > Max:
        Max = math.fabs(YAcc[i] - YErr[i])
    i += 1
print("Error 2: ", Max)


TArr = list()
YArr = list()

runge_kutta(h, t0, y0, T, TArr, YArr)

ideal = 0
i = 0
while i < len(TArr):
    if math.fabs(YAcc[2*i] - YArr[i]) > ideal:
        ideal = math.fabs(YAcc[i] - YArr[i])
    i += 1
print("RK error: ", ideal)
error = ideal

while True:
    TArr = list()
    YArr = list()
    YAcc = list()

    euler(h, t0, y0, T, TArr, YArr)

    i = t0
    j = 0
    YAcc.append(accurate_solution(TArr[j]))
    while i <= T:
        j += 1
        i += h
        YAcc.append(accurate_solution(TArr[j]))

    Max = 0
    i = 0
    while i < len(TArr):
        if math.fabs(YAcc[i] - YArr[i]) > Max:
            Max = math.fabs(YAcc[i] - YArr[i])
        i += 1

    if Max <= error:
        print("euler h: ", h)
        break
    else:
        h = h/2
