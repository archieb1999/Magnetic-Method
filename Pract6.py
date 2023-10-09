import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, ifft

X = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000,
     18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]

Y = [9.45, 11.7, 14.43, 17.68, 21.5, 25.9, 30.86, 36.43, 42.69, 49.8, 57.6, 64.4, 65.96, 57.8, 39.97, 17.09, -4.12,
     -18.47, -25.79, -28.84, -29.83, -29.76, -29, -27.71, -26.04, -24.14, -22.15, -20.18, -18.3, -16.55, -14.15]


def polyreg(X, Y, n):
    y = np.polyfit(X, Y, n)
    z = np.polyval(y, X)
    plt.plot(X, Y, X, z)
    plt.title('Polynomial regression of order {}'.format(n))
    plt.xlabel('Distance in metres')
    plt.ylabel('Magnetic anomaly in nT')
    plt.grid()
    plt.show()

    y1 = Y - z
    plt.plot(X, y1)
    plt.ylim(-60, 60)
    plt.grid()
    plt.title('Anomaly after correction')
    plt.xlabel('Distance in metres')
    plt.ylabel('Magnetic anomaly in nT')
    plt.show()


def lowpassfilter(X, Y, lmax):
    k0 = 1 / lmax
    k = np.linspace(1 / 30000, 1 / 1000, 31)
    L = np.zeros(len(Y))
    for i in range(0, len(Y)):
        if k[i] <= k0:
            L[i] = 1
        else:
            L[i] = 0

    f = fft(Y)
    LP = f * L
    lpf = ifft(LP)
    R = Y - lpf

    fig, ax = plt.subplots()
    ax.plot(X, Y, label='Observed Data')
    ax.plot(X, R, label='Low-pass filtered data')
    plt.xlabel('Distance in metres')
    plt.ylabel('Total magnetic intensity in nT')
    plt.title('Low pass filtration')
    plt.legend()
    plt.grid()
    plt.show()


def upwardcont(X, Y, h):
    F = fft(Y)
    k = np.linspace(2 * 3.14 / 30000, 2 * 3.14 / 1000, 31)
    T = np.multiply(F, np.exp(np.multiply(-k, h)))
    t = ifft(T)
    r = Y - t

    fig, ax = plt.subplots()
    ax.plot(X, Y, label='Observed Anomaly')
    ax.plot(X, t, label='Regional Anomaly')
    ax.plot(X, r, label='Residual Anomaly')
    plt.xlabel('Distance in metres')
    plt.ylabel('Total magnetic intensity in nT')
    plt.title('Upward continuation at {} metres'.format(h))
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    polyreg(X, Y, 1)
    polyreg(X, Y, 2)
    polyreg(X, Y, 3)
    lowpassfilter(X, Y, 10000)
    lowpassfilter(X, Y, 5000)
    lowpassfilter(X, Y, 20000)
    upwardcont(X, Y, 2000)
    upwardcont(X, Y, 5000)
    upwardcont(X, Y, 10000)
