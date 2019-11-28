import numpy
import math
import matplotlib.pyplot as plt


def count(i1, i2, i3, xArr, yArr):
    return 3*(yArr[i3] - yArr[i1])/(xArr[i2] - xArr[i1])


def interpolate(x_i1, x_i2, x, f_i1, f_i2, m_i1, m_i2):
    h = x_i2 - x_i1
    result1 = (((x_i2 - x)**2) * (2*(x - x_i1) + h)*f_i1)/(h**3) + (((x - x_i1)**2) * (2*(x_i2 - x) + h)*f_i2)/(h**3)
    result2 = (((x_i2 - x)**2) * (x - x_i1) * m_i1)/(h**2) + (((x - x_i1)**2) * (x - x_i2) * m_i2)/(h**2)
    return result1 + result2


def interpolate2(x):
    if (0 < x) & (x < 4):
        return interpolate(0, 4, x, 5*math.sin(0), 5*math.sin(16), 0, 38.4)
    else:
        return 5*math.sin(x**2)


def interpolate3(x):
    if (0 < x) & (x < 2):
        return interpolate(0, 2, x, 5*math.sin(0), 5*math.sin(4), 0, V2[0])
    elif (2 < x) & (x < 4):
        return interpolate(2, 4, x, 5*math.sin(4), 5*math.sin(16), V2[0], 38.4)
    else:
        return 5*math.sin(x**2)


def interpolate4(x):
    if (0 < x) & (x < 1):
        return interpolate(0, 1, x, 5*math.sin(0), 5*math.sin(1), 0, V3[0])
    elif (1 < x) & (x < 3):
        return interpolate(1, 3, x, 5*math.sin(1), 5*math.sin(9), V3[0], V3[1])
    elif (3 < x) & (x < 4):
        return interpolate(3, 4, x, 5*math.sin(9), 5*math.sin(16), V3[1], 38.4)
    else:
        return 5*math.sin(x**2)


def interpolate5(x):
    if (0 < x) & (x < 1):
        return interpolate(0, 1, x, 5*math.sin(0), 5*math.sin(1), 0, V4[0])
    elif (1 < x) & (x < 2):
        return interpolate(1, 2, x, 5*math.sin(1), 5*math.sin(4), V4[0], V4[1])
    elif (2 < x) & (x < 3):
        return interpolate(2, 3, x, 5*math.sin(4), 5*math.sin(9), V4[1], V4[2])
    elif (3 < x) & (x < 4):
        return interpolate(3, 4, x, 5*math.sin(9), 5*math.sin(16), V4[2], 38.4)
    else:
        return 5*math.sin(x**2)


def interpolateOther(x):
    if (0 < x) & (x < 0.5):
        return interpolate(0, 0.5, x, 5*math.sin(0), 5*math.sin(0.5**2), 0, V7[0])
    elif (0.5 < x) & (x < 1):
        return interpolate(0.5, 1, x, 5*math.sin(0.5**2), 5*math.sin(4), V7[0], V7[1])
    elif (1 < x) & (x < 1.5):
        return interpolate(1, 1.5, x, 5*math.sin(1), 5*math.sin(1.5**2), V7[1], V7[2])
    elif (1.5 < x) & (x < 2):
        return interpolate(1.5, 2, x, 5*math.sin(1.5**2), 5*math.sin(4), V7[2], V7[3])
    elif (2 < x) & (x < 2.5):
        return interpolate(2, 2.5, x, 5*math.sin(4), 5*math.sin(2.5**2), V7[3], V7[4])
    elif (2.5 < x) & (x < 3):
        return interpolate(2.5, 3, x, 5*math.sin(2.5**2), 5*math.sin(9), V7[4], V7[5])
    elif (3 < x) & (x < 3.5):
        return interpolate(3, 3.5, x, 5*math.sin(9), 5*math.sin(3.5**2), V7[5], V7[6])
    elif (3.5 < x) & (x < 4):
        return interpolate(3.5, 4, x, 5*math.sin(3.5**2), 5*math.sin(16), V7[6], 38.4)
    else:
        return 5*math.sin(x**2)


def choice(nodes):
    if nodes == 2:
        i = 0
        while i <= 4:
            XPlot.append(i)
            YPlot.append(interpolate2(i))
            i += 0.05
    elif nodes == 3:
        i = 0
        while i <= 4:
            XPlot.append(i)
            YPlot.append(interpolate3(i))
            i += 0.05
    elif nodes == 4:
        i = 0
        while i <= 4:
            XPlot.append(i)
            YPlot.append(interpolate4(i))
            i += 0.05
    elif nodes == 5:
        i = 0
        while i <= 4:
            XPlot.append(i)
            YPlot.append(interpolate5(i))
            i += 0.05
    else:
        i = 0
        while i <= 4:
            XPlot.append(i)
            YPlot.append(interpolateOther(i))
            i += 0.05


def lineplot(x_data, y_data, x_data2, y_data2, x_label="X", y_label="Y", title="Interpolation"):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)
    ax.plot(x_data2, y_data2, lw=2, color='#230caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


XArr = []
M7 = numpy.array([[4, 1, 0, 0, 0, 0, 0],
                  [1, 4, 1, 0, 0, 0, 0],
                  [0, 1, 4, 1, 0, 0, 0],
                  [0, 0, 1, 4, 1, 0, 0],
                  [0, 0, 0, 1, 4, 1, 0],
                  [0, 0, 0, 0, 1, 4, 1],
                  [0, 0, 0, 0, 0, 1, 4]])

M4 = numpy.array([[4., 1., 0.],
                  [1., 4., 1.],
                  [0., 1., 4.]])

M3 = numpy.array([[4., 1.],
                  [1., 4.]])

M2 = numpy.array([4.])
V7 = []
V4 = []
V3 = []
V2 = []
Arr = []
XPlot = []
YPlot = []
i = 0
while i <= 4:
    XArr.append(i)
    Arr.append(5*math.sin(i**2))
    #print(i, " - ", 5*math.sin(i**2), "\n")
    i += 0.05
YArr = numpy.array(Arr)
XArr = numpy.array(XArr)

V7.append(count(0, 1, 2, XArr, YArr))
V7.append(count(1, 2, 3, XArr, YArr))
V7.append(count(2, 3, 4, XArr, YArr))
V7.append(count(3, 4, 5, XArr, YArr))
V7.append(count(4, 5, 6, XArr, YArr))
V7.append(count(5, 6, 7, XArr, YArr))
V7.append(count(6, 7, 8, XArr, YArr))
V7 = numpy.array(V7)

V4.append(count(0, 1, 2, XArr, YArr))
V4.append(count(1, 2, 3, XArr, YArr))
V4.append(count(2, 3, 4, XArr, YArr))
V4 = numpy.array(V4)

V3.append(count(0, 1, 3, XArr, YArr))
V3.append(count(1, 3, 4, XArr, YArr))
V3 = numpy.array(V3)

V2.append(count(0, 2, 4, XArr, YArr))
V2 = numpy.array(V2)

S7 = numpy.linalg.solve(M7, V7)
S4 = numpy.linalg.solve(M4, V4)
S3 = numpy.linalg.solve(M3, V3)
S2 = V2[0]/4

select = int(input("What about nodes? - "))
choice(select)

lineplot(XArr, YArr, XPlot, YPlot)
