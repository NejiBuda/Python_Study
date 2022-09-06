"""
Напишите код на Python, реализующий построение графиков:
1. окружности,
2. эллипса,
# №1
3. гиперболы.
"""


%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

x = []
x_2 = []
y = []
y_2 = []

for n in range(1000):
    r = 500
    x.append(-n)
    x_2.append(n)
    y.append(np.sqrt(r ** 2 - n ** 2))
    y_2.append(-np.sqrt(r ** 2 - n ** 2))

plt.figure(figsize = (6, 6))
plt.plot(x, y, color = 'r')
plt.plot(x, y_2, color = 'r')
plt.plot(x_2, y_2, color = 'r')
plt.plot(x_2, y, color = 'r')
plt.axis("scaled")
plt.show()

#Ellipse
x = []
x_2 = []
y = []
y_2 = []

for n in range(1000):
    a = 50
    b = 25
    x.append(-n)
    x_2.append(n)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (n ** 2 / a ** 2))))
    y_2.append((-np.sqrt(b ** 2 - (b ** 2 * (n ** 2 / a ** 2)))))

plt.plot(x, y, color='b')
plt.plot(x, y_2, color='b')
plt.plot(x_2, y_2, color='b')
plt.plot(x_2, y, color='b')
plt.axis('scaled')
plt.show()

#Heperbole
x = []
x_2 = []
y = []
y_2 = []

for n in range(1000):
    a = 450
    b = 250
    x.append(-n)
    x_2.append(n)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (n ** 2 / a ** 2))))
    y_2.append((-np.sqrt(b ** 2 + (b ** 2 * (n ** 2 / a ** 2)))))

plt.plot(x, y, color='y')
plt.plot(x, y_2, color='y')
plt.plot(x_2, y_2, color='y')
plt.plot(x_2, y, color='y')
plt.axis('scaled')
plt.show()
