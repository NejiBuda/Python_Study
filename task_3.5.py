"""
5. Задание (в программе)
1) Нарисуйте трехмерный график двух параллельных плоскостей.
2) Нарисуйте трехмерный график двух любых поверхностей второго порядка.
"""

#Задание 5
#а)Нарисуйте трехмерный график двух параллельных плоскостей
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
x = np.arange(-17, 17, 2)
y = np.arange(-17, 17, 2)

x, y = np.meshgrid(x,y)

z = 9 * x + 150
z_2 = 9 * x + 10
ax.plot_wireframe(x, y , z, linestyle = '--', linewidth = 1)
ax.plot_wireframe(x, y, z_2, colors = 'orange')

show()

