import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

D = [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
G = {
    'g10': [-29873, -29775, -29692, -29619.4, -29554.63, -29496.57, -29441.46, -29404.8],

    'g11': [-1905, -1848, -1784, -1728.2, -1669.05, -1586.42, -1501.77, -1450.9],

    'h11': [5500, 5406, 5306, 5186.1, 5077.99, 4944.26, 4795.99, 4652.5],

    'g20': [-2072, -2131, -2200, -2267.7, -2337.24, -2396.06, -2445.88, -2499.6],

    'g21': [3044, 3059, 3070, 3068.4, 3047.69, 3026.34, 3012.2, 2982.0],

    'h21': [-2197, -2279, -2366, -2481.6, -2594.50, -2708.54, -2845.41, -2991.6],

    'g22': [1687, 1686, 1681, 1670.9, 1657.76, 1668.17, 1676.35, 1677.0],

    'h22': [-306, -373, -413, -458.0, -515.43, -575.73, -642.17, -734.6]
}

G = pd.DataFrame(G)

# Now, we'll find the root mean square intensity
Rd = []
Rnd = []
for i in range(len(D)):
    Rd.append(np.sqrt(2 * (G['g10'][i] ** 2 + G['g11'][i] ** 2 + G['h11'][i] ** 2)))
    Rnd.append(np.sqrt(3 * (G['g20'][i] ** 2 + G['g21'][i] ** 2 + G['h21'][i] ** 2)
                       + G['g22'][i] ** 2 + G['h22'][i] ** 2))

# Now, we'll find the line with minimum square error using numpy.polyfit and then plot the graphs
R1 = np.polyfit(D, Rd, 1)
plt.plot(D, np.polyval(R1, D), c='orange', label='linear regression: y = {0:.2f}x + {1:.2f}'.format(R1[0], R1[1]))
plt.scatter(D, Rd, c='none', edgecolors='black')
plt.xlabel('IGRF Model Year')
plt.ylabel('RMS Intensity in nT')
plt.title('RMS Intensity vs Time for Dipole field')
plt.legend()
plt.show()

R2 = np.polyfit(D, Rnd, 1)
plt.plot(D, np.polyval(R2, D), c='green', label='linear regression: y = {0:.2f}x + {1:.2f}'.format(R2[0], R2[1]))
plt.scatter(D, Rnd, c='none', edgecolors='red')
plt.xlabel('IGRF Model Year')
plt.ylabel('RMS Intensity in nT')
plt.title('RMS Intensity vs Time for Non-Dipole field')
plt.legend()
plt.show()

# Now we'll repeat the things done before with added 5% random error to each Gauss coefficient
G1 = {}
for i in G:
    G1[i] = G[i] + np.random.choice([-1, 1]) * np.random.ranf() * 0.05 * G[i]

G1 = pd.DataFrame(G1)
print('The new Gauss coefficients are:')
print(G1)

Rd1 = []
Rnd1 = []
for i in range(len(D)):
    Rd1.append(np.sqrt(2 * (G1['g10'][i] ** 2 + G1['g11'][i] ** 2 + G1['h11'][i] ** 2)))
    Rnd1.append(np.sqrt(3 * (G1['g20'][i] ** 2 + G1['g21'][i] ** 2 + G1['h21'][i] ** 2
                             + G1['g22'][i] ** 2 + G1['h22'][i] ** 2)))

R3 = np.polyfit(D, Rd1, 1)
plt.plot(D, np.polyval(R3, D), c='orange', label='linear regression y: = {0:.2f}x + {1:.2f}'.format(R3[0], R3[1]))
plt.scatter(D, Rd1, c='none', edgecolors='black')
plt.xlabel('IGRF Model Year')
plt.ylabel('RMS Intensity in nT')
plt.title('RMS Intensity vs Time for Dipole field with added noise')
plt.legend()
plt.show()

R4 = np.polyfit(D, Rnd1, 1)
plt.plot(D, np.polyval(R4, D), c='green', label='linear regression: y = {0:.2f}x + {1:.2f}'.format(R4[0], R4[1]))
plt.scatter(D, Rnd1, c='none', edgecolors='red')
plt.xlabel('IGRF Model Year')
plt.ylabel('RMS Intensity in nT')
plt.title('RMS Intensity vs Time for Non-Dipole field with added noise')
plt.legend()
plt.show()
