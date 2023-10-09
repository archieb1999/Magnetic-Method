import numpy as np
import matplotlib.pyplot as plt

cf = 100
x = np.linspace(-20, 20, 21)  # distance of the observation from the origin
h = np.linspace(5, 20, 4)  # depth to the top of the body
theta = [0, np.pi / 2, np.pi / 4, np.pi / 6, np.pi / 3]
del_f = np.zeros((len(h), len(theta), len(x)))

for i in range(0, len(h)):
    for j in range(0, len(theta)):
        for k in range(0, len(x)):
            A = np.arctan(x[k] / h[i]) + (np.pi / 2)
            B = 0.5 * (np.log((x[k]) * x[k] + h[i] * h[i]))
            del_f[i][j][k] = 100 * (A * np.cos(theta[j]) + B * np.sin(theta[j]))

theta = np.multiply(theta, (180 / np.pi))

theta = np.round(theta)

for i in range(len(h)):
    plt.figure(figsize=(5, 5))
    plt.subplot(1, 4, i + 1)
    plt.title('H = {h}km'.format(h=h[i]))
    leg = []
    for j in range(len(theta)):
        plt.plot(x, del_f[i][j])
        plt.xlabel('Position (km)')
        plt.ylabel('Magnetic Anomaly (T)')
        leg.append('\u03B8 = {t}'.format(t=(theta[j])))
    plt.legend(leg)
plt.show()
