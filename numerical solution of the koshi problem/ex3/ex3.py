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


def adams(h, t0, y0, stop, TArr, YArr):
    t = t0
    y = y0
    TArr.append(t)
    YArr.append(y)
    prev1 = y

    y += h * function(t, y)
    t += h
    TArr.append(t)
    YArr.append(y)
    prev2 = y

    y += h * function(t, y)
    t += h
    TArr.append(t)
    YArr.append(y)
    prev3 = y

    while t <= stop:
        y += (h/12)*(23*prev3 - 16*prev2 + 5*prev1)
        t += h
        prev1 = prev2
        prev2 = prev3
        prev3 = y
        TArr.append(t)
        YArr.append(y)


def function(t, y):
    return y + 2*t*(y**2)  # функция первой производной


h = 0.05
t0 = 0
T = 0.8
y0 = 0.5

Tadam1 = list()
Tadam2 = list()

Yadam1 = list()
Yadam2 = list()

Trk1 = list()
Trk2 = list()

Yrk1 = list()
Yrk2 = list()

Y_rk_corrected = list()
Y_adams_corrected = list()

runge_kutta(h, t0, y0, T, Trk1, Yrk1)
runge_kutta(h/2, t0, y0, T, Trk2, Yrk2)

adams(h, t0, y0, T, Tadam1, Yadam1)
adams(h/2, t0, y0, T, Tadam2, Yadam2)

Y_rk_corrected = Yrk1
Y_adams_corrected = Yadam1

Max = 0
i = 0
while i < len(Trk1):
    if math.fabs(Yrk1[i] - Yrk2[2*i])/15 > Max:
        Max = math.fabs(Yrk1[i] - Yrk2[i])/15
    Y_rk_corrected[i] = Yrk2[2*i] + math.fabs(Yrk1[i] - Yrk2[2*i])/15
    i += 1
print("Error RK: ", Max)

Max = 0
i = 0
while i < len(Tadam1):
    if math.fabs(Yadam1[i] - Yadam2[2*i])/7 > Max:
        Max = math.fabs(Yadam1[i] - Yadam2[i])/7
    Y_adams_corrected[i] = Yadam2[2*i] + math.fabs(Yadam1[i] - Yadam2[2*i])/7
    i += 1
print("Error Adams: ", Max)


lineplot(Trk1, Y_rk_corrected, Trk2, Yrk2, title="RK")
lineplot(Tadam1, Y_adams_corrected, Tadam2, Yadam2, title="Adams")
