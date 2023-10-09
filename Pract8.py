import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft


M=[98.81, 122.94, 153.05, 190.53, 236.95, 293.74, 361.53, 438.58, 517.96, 584.33, 614.68, 587.83, 497.99, 355.38, 180.59, 1.28, -151.53, -255.96, -309.94, -325.92, -318.78, -299.67, -275.49, -250.08, -225.44, -202.54, -181.74, -163.12, -146.58, -131.96,-119.05];

x = np.linspace(0,30000,31)

f_M = fft(M)

for i in range(0,len(f_M)):
    if (f_M[i]>0):
        f_M[i]=2*f_M[i];
    else: f_M[i]=0;

ans = ifft(f_M)

ansr = np.real(ans)
print(ansr)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, M, 'r-')
ax2.plot(x, ansr, 'b-')
ax1.set_xlabel('Distance x (m)')
ax1.set_ylabel('Magnetic Anomaly (nT)', color='r')
ax2.set_ylabel('Analytical Signal (nT/m²)', color='b')
plt.title('Magnetic Anomaly and its Analytical Signal')
plt.show()