import numpy as np
import matplotlib.pyplot as plt

cf = 100  # amplitude coefficient
x = np.linspace(-60, 60, 25)  # distance of the observation from the origin
h2 = np.linspace(20, 30, 3)  # depth to the top of the body
theta = [0, np.pi / 2, np.pi / 4, np.pi / 6, np.pi / 3]  # arbitrary magnetization angle
del_f = np.zeros((len(h2), len(theta), len(x)))
h1 = 5
for i in range(0, len(h2)):
    for j in range(0, len(theta)):
        for k in range(0, len(x)):
            A = np.arctan(x[k] / h1) - np.arctan(x[k] / h2[i])
            B = 0.5 * (np.log((x[k]) * x[k] + h2[i] * h2[i]) / (np.log((x[k]) * x[k] + h1 * h1)))
            del_f[i][j][k] = 100 * (A * np.cos(theta[j]) + B * np.sin(theta[j]))

theta = np.multiply(theta, (180 / np.pi))

theta = np.round(theta)

for i in range(len(h2)):
    plt.figure(figsize=(5, 5))
    plt.subplot(1, 4, i + 1)
    plt.title('H2 = {h}km'.format(h=h2[i]))
    leg = []
    for j in range(len(theta)):
        plt.plot(x, del_f[i][j])
        plt.xlabel('Position (km)')
        plt.ylabel('Magnetic Anomaly (T)')
        leg.append('\u03B8 = {t}'.format(t=(theta[j])))
    plt.legend(leg)
plt.show()
