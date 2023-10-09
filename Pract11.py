import numpy as np
import matplotlib.pyplot as plt

cf = 100  # amplitude coefficient
x = np.linspace(-100, 100, 21)  # distance of the observation from the origin (interval of 10 units).
z = [5, 10]  # depth to the centre of the body
theta = [0, np.pi / 2, np.pi / 6, np.pi / 3]  # arbitrary magnetization angle
del_f = np.zeros((len(z), len(theta), len(x)))
t = 10  # width of the dyke

for i in range(0, len(z)):
    for j in range(0, len(theta)):
        for k in range(0, len(x)):
            A = np.arctan((x[k] + t) / z[i]) - np.arctan((x[k] - t) / z[i])
            B = np.log(((x[k] + t) * (x[k] + t) + z[i] * z[i]) / ((x[k] - t) * (x[k] - t) + z[i] * z[i]))
            del_f[i][j][k] = 100 * (A * np.cos(theta[j]) + B * np.sin(theta[j]))

theta = np.multiply(theta, (180 / np.pi))
theta = np.round(theta)

for i in range(len(z)):
    plt.figure(figsize=(5, 5))
    plt.subplot(1, 2, i + 1)
    plt.title('z = {h}m, t = 10m'.format(h=z[i]))
    leg = []
    for j in range(len(theta)):
        plt.plot(x, del_f[i][j])
        plt.xlabel('Position (m)')
        plt.ylabel('Magnetic Anomaly (T)')
        leg.append('\u03B8 = {t}'.format(t=(theta[j])))
    plt.legend(leg)
plt.show()

t = 50;  # width of the dyke
theta = [0, np.pi / 2, np.pi / 6, np.pi / 3]  # arbitrary magnetization angle
for i in range(0, len(z)):
    for j in range(0, len(theta)):
        for k in range(0, len(x)):
            A = np.arctan((x[k] + t) / z[i]) - np.arctan((x[k] - t) / z[i])
            B = np.log(((x[k] + t) * (x[k] + t) + z[i] * z[i]) / ((x[k] - t) * (x[k] - t) + z[i] * z[i]))
            del_f[i][j][k] = 100 * (A * np.cos(theta[j]) + B * np.sin(theta[j]))
theta = np.multiply(theta, (180 / np.pi))
theta = np.round(theta)

for i in range(len(z)):
    plt.figure(figsize=(5, 5))
    plt.subplot(1, 2, i + 1)
    plt.title('z = {h}m, t = 50m'.format(h=z[i]))
    leg = []
    for j in range(len(theta)):
        plt.plot(x, del_f[i][j])
        plt.xlabel('Position (m)')
        plt.ylabel('Magnetic Anomaly (T)')
        leg.append('\u03B8 = {t}'.format(t=(theta[j])))
    plt.legend(leg)
plt.show()
