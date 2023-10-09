import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0, 12, 121)
y = np.linspace(0, 12, 121)

X, Y = np.meshgrid(x, y)

points = [[5., 1.],
          [7., 2.],
          [8.7, 1.],

          [0., 1.4],
          [1.2, 2.],
          [2.3, 3.],
          [4., 4.5],
          [6., 5.5],
          [8.2, 3.],
          [10.1, 2.],
          [11., 0.8],

          [0., 3.5],
          [2., 5.],
          [3., 6.],
          [4.5, 7.],
          [6., 7.4],
          [8., 6.5],
          [9.5, 4.5],
          [10.8, 3],
          [12., 1.5],

          [0.0, 5.1],
          [1., 5.8],
          [2.5, 7.],
          [4., 8.2],
          [6., 8.8],
          [8., 8.],
          [9., 7.],
          [10., 5.5],
          [11., 4.],
          [12., 2.9],

          [0., 6.4],
          [2., 8.],
          [3.2, 9.],
          [5., 10.],
          [7., 10.],
          [9., 8.5],
          [10.1, 7.],
          [11., 5.7],
          [12., 4.1],

          [0., 7.5],
          [1., 8.5],
          [3., 10.],
          [4., 10.4],
          [6., 11.],
          [8.4, 10.],
          [9.5, 9.],
          [10.3, 8.],
          [11., 7.],
          [12., 5.5],

          [0., 8.6],
          [2., 10.3],
          [4., 11.3],
          [6., 11.8],
          [8., 11.3],
          [9.5, 10],
          [10.4, 9.],
          [12., 6.8],

          [0., 9.7],
          [2., 11.],
          [3.8, 12.],
          [8., 12.],
          [9.5, 11.],
          [10.4, 10.],
          [12., 8.],

          [0., 10.6],
          [2., 12.],
          [10., 11.5],
          [11., 10.5],
          [12., 9.]]

values = [240, 240, 240, 250, 250, 250, 250, 250, 250, 250, 250, 260, 260, 260, 260, 260, 260, 260, 260, 260, 270,
          270, 270, 270, 270, 270, 270, 270, 270, 270, 280, 280, 280, 280, 280, 280, 280, 280, 280, 290, 290, 290, 290,
          290, 290, 290, 290, 290, 290, 300, 300, 300, 300, 300, 300, 300, 300, 310, 310, 310, 310, 310, 310,
          310, 320, 320, 320, 320, 320]

Inp = griddata(points, values, (X, Y), method='cubic')
plt.contourf(X, Y, Inp)
plt.title('Anomaly at 500 ft')
plt.xlabel('X coordinates in km')
plt.ylabel('Y coordinates in km')
plt.colorbar(label='nT')
plt.show()


def continuation(h, i, j):
    h = 0.0003048 * h
    C0 = 0.5 * (1 - h / np.sqrt(h ** 2 + 1))
    C1 = 0.5 * (1 - h / np.sqrt(h ** 2 + 2))
    t0 = Inp[i, j]
    t1avg = 0.25 * (Inp[i - 10][j] + Inp[i][j + 10] + Inp[i + 10][j] + Inp[i][j - 10])
    return C0 * t0 + C1 * t1avg


points1 = []
values1 = []
values2 = []

for i in range(10, 111):
    for j in range(10, 111):
        points1.append([i / 10, j / 10])
        values1.append(continuation(6000, i, j))
        values2.append(continuation(-50, i, j))


V1 = []
P1 = []
for i in range(len(values1)):
    if values1[i] == values1[i]:
        V1.append(values1[i])
        P1.append(points1[i])

Inp2 = griddata(P1, V1, (X, Y), method='cubic')

plt.contourf(X, Y, Inp2.T)
plt.title('Upward continuation at 6000 ft')
plt.xlabel('X coordinates in km')
plt.ylabel('Y coordinates in km')
plt.colorbar(label='nT')
plt.show()

V2 = []
P2 = []

for i in range(len(values2)):
    if values2[i] == values2[i]:
        V2.append(values2[i])
        P2.append(points1[i])

Inp3 = griddata(P2, V2, (X, Y), method='cubic')

plt.contourf(X, Y, Inp3.T)
plt.title('Downward continuation at 60 ft')
plt.xlabel('X coordinates in km')
plt.ylabel('Y coordinates in km')
plt.colorbar(label='nT')
plt.show()
