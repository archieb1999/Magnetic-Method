import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests as rq
import datetime

DATE = datetime.date(2022, 1, 24)

# CASE 1
BASE_READING_1 = 47217.73
BASE_READING_2 = 47229.3675
Num_of_10mins_Between_Readings = 27
Change_per_10mins = (BASE_READING_2 - BASE_READING_1) / Num_of_10mins_Between_Readings

D1 = {
    'Station': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'Lon': [76.2751, 76.2760, 76.2770, 76.27775, 76.27875, 76.2797, 76.28075, 76.2817, 76.2837, 76.28475, 76.2858,
            76.2867, 76.2877, 76.2887, 76.2897, 76.29075, 76.2917, 76.2927, 76.2937, 76.29475, 76.29575, 76.2967,
            76.29775, 76.29875],
    'Lat': [27.36647, 27.3662, 27.36611, 27.36602, 27.36586, 27.3656, 27.3655, 27.365305, 27.364972, 27.364805,
            27.364638, 27.36447, 27.36427, 27.36411, 27.36394, 27.36377, 27.36361, 27.36338, 27.36327, 27.36308,
            27.36291, 27.36277, 27.36258, 27.36241],
    'Reading': [47289.25, 47311.375, 47328.11, 47333.13, 47327.16, 47290.785, 47286.93, 47278.147, 47302.61, 47311.645,
                47309.25, 47383.11, 47287.73, 47272.125, 47276.19, 47270.635, 47275.67, 47284.21, 47288.365, 47311.965,
                47281.695, 47309.33, 47288.935, 47296.3]
}

D1 = pd.DataFrame(D1)


# Function for calculating IGRF
def IGRF(lat, lon, alt, date):
    params = {'latitude': lat, 'longitude': lon, 'altitude': alt, 'date': date, 'format': 'json'}
    response = rq.get("http://geomag.bgs.ac.uk/web_service/GMModels/igrf/13/", params=params).json()
    return response['geomagnetic-field-model-result']['field-value']['total-intensity']['value']


# Applying Diurnal and IGRF correction in CASE 1
C1 = []

for i in D1['Station']:
    C1.append(D1['Reading'][i - 1] - Change_per_10mins * D1['Station'][i - 1]
              - IGRF(D1['Lat'][i - 1], D1['Lon'][i - 1], 0, DATE))

D1['Processed-values'] = C1

print(D1)

plt.plot(D1['Station'], D1['Reading'], label='raw values', c='orange')
plt.xlabel('Station Number')
plt.ylabel('Magnetic field in nT')
plt.title('Raw magnetic field in Case 1')
plt.legend()
plt.show()

plt.plot(D1['Station'], D1['Processed-values'], label='processed values', c='green')
plt.xlabel('Station Number')
plt.ylabel('Magnetic field in nT')
plt.title('Processed magnetic field in Case 1')
plt.legend()
plt.show()





# CASE 2

BASE_READING = 48512.75

D2 = {
    'Station': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'Lon': [-116.26094, -116.25974, -116.25828, -116.25774, -116.25736, -116.25611, -116.25505, -116.25351, -116.25474,
            -116.2561, -116.25721, -116.25849, -116.25987, -116.26206, -116.26089, -116.25938, -116.25883, -116.25939,
            -116.25865, -116.26067, -116.26236, -116.2635, -116.26435, -116.26354],
    'Lat': [35.90388, 35.90464, 35.90575, 35.90635, 35.90665, 35.90767, 35.90829, 35.90742, 35.90641, 35.90551,
            35.90481, 35.90934, 35.90303, 35.90515, 35.90598, 35.90685, 35.90713, 35.90852, 35.90876, 35.90784,
            35.90727, 35.90673, 35.90814, 35.90866],
    'Reading': [48627.4, 48642, 48644.1, 48637.8, 48642.7, 48652.5, 48645.4, 48659.3, 48657.3, 48647, 48654.3, 48624.2,
                48631.7, 48621.8, 48621.1, 48621.2, 48619.6, 48622.3, 48621.3, 48621, 48618.9, 48611.9, 48602.6,
                48608.2],
    'Time': [10, 16, 23, 28, 33, 45, 50, 57, 62, 67, 71, 76, 81, 93, 97, 103, 108, 114, 118, 124, 130, 136, 187, 191]
}

D2 = pd.DataFrame(D2)

D3 = {
    'Mins': [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125,
             130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230],
    'Reading': [48512.75, 48512.577, 48512.49, 48512.649, 48516.97, 48513.287, 48515.77, 48516.675, 48517.12, 48520.725,
                48515.25, 48518.354, 48512.31, 48512.206, 48512.35, 48512.492, 48512.09, 48512.884, 48513.57, 48513.966,
                48513.49, 48513.368, 48513.64, 48512.882, 48514.61, 48515.171, 48514.24, 48513.542, 48511.55, 48513.457,
                48512.56, 48512.702, 48512.28, 48511.982, 48511.76, 48511.671, 48511.93, 48511.849, 48512.01, 48512.731,
                48513.33, 48514.497, 48514.59, 48514.77, 48515.01, 48513.264, 48513.42]
}


def diurnal_correction_CASE2(t):
    m = (t // 5)
    return D3['Reading'][m] + (D3['Reading'][m + 1] - D3['Reading'][m]) * 0.2 * (t % 5) - D3['Reading'][0]

d = []
for i in range(len(D3['Mins'])):
    d.append([D3['Reading'][0]])

plt.plot(D3['Mins'], D3['Reading'], label='Diurnal curve')
plt.plot(D3['Mins'], d, label='Magnetic datum', c='red')
plt.xlabel('Time in minutes from 8:57')
plt.ylabel('Magnetic field in nT')
plt.title('Plot showing diurnal magnetic fluctuations in Case 2')
plt.legend()
plt.show()

# Applying diurnal and IGRF correction in CASE 2

C2 = []

for i in D2['Station']:
    C2.append(D2['Reading'][i - 1] - diurnal_correction_CASE2(D2['Time'][i - 1])
              - IGRF(D2['Lat'][i - 1], D2['Lon'][i - 1], 0, DATE))

D2['Processed-values'] = C2

print(D2)

plt.plot(D2['Time'], D2['Reading'], label='raw values', c='orange')
plt.xlabel('Time in minutes from first recording')
plt.ylabel('Magnetic field in nT')
plt.title('Raw magnetic field in Case 2')
plt.legend()
plt.show()

plt.plot(D2['Time'], D2['Processed-values'], label='processed values', c='green')
plt.xlabel('Time in minutes from first recording')
plt.ylabel('Magnetic field in nT')
plt.title('Processed magnetic field in Case 2')
plt.legend()
plt.show()
