import math

XArr = [-2, -1.6, - 1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2, 1.6, 2]
YArr = [8.16617, 5.92986, 4.30596, 3.12677, 2.27050, 1.64872, 2.27050, 3.12677, 4.30596, 5.92986, 8.16617]


def countX(x):
    return math.fabs(x)


def countY(y):
    return math.log(y)


n = len(XArr)

SumX = 0
for item in XArr:
    SumX += countX(item)

SumY = 0
for item in YArr:
    SumY += countY(item)

SumXY = 0
for i in range(0, len(XArr)):
    SumXY += countX(XArr[i]) * countY(YArr[i])

SumX2 = 0
for item in XArr:
    SumX2 += math.pow(countX(item), 2)

b = (n * SumXY - SumX * SumY)/(n * SumX2 - math.pow(SumX, 2))
a = (SumY - b * SumX)/n

print("s = ", b, " * t + ", a)
