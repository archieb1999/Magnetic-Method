import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

X = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000,
     18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]

Y = [98.81, 122.94, 153.05, 190.53, 236.95, 293.74, 361.53, 438.58, 517.96, 584.33, 614.58, 587.83, 497.99, 355.38,
     180.59, 1.28, -151.53, -255.96, -309.94, -325.92, -318.78, -299.67, -275.49, -250.08, -225.44, -202.54, -181.74,
     -163.12, -146.58, -131.96, -119.05]

# plotting the magnetic anomaly profile data
plt.plot(X, Y)
plt.title('Magnetic Anomaly Curve')
plt.xlabel('Distance in metres')
plt.ylabel('Magnetic Anomaly in nT')
plt.show()

L = 30000
dk = 1/L
dx = np.linspace(0, L, 31)
k = dk*dx
f = fft(Y)
fvd = f*(-k)
svd = f*(-k)**2
fvd1 = ifft(fvd)
svd1 = ifft(svd)

# plotting the first & second vertical derivative of magnetic profile data
plt.plot(X, fvd1)
plt.title('First Vertical Derivative')
plt.xlabel('Distance in metres')
plt.ylabel('FVD in nT/m')
plt.show()

plt.plot(X, svd1)
plt.title('Second Vertical Derivative')
plt.xlabel('Distance in metres')
plt.ylabel('SVD in nT/m')
plt.show()


plt.plot(X, Y, X, fvd1, X, svd1)
plt.legend(['Anomaly', 'FVD', 'SVD'])
plt.show()
