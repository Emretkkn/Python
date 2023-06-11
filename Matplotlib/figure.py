import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-9,10,20)
y = x**3
z = x**2
'''
figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"r")
axes_cube.set_xlabel("X Label")
axes_cube.set_ylabel("Y Label")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.2,0.2])
axes_square.plot(x,z,"o--b")
axes_square.set_xlabel("X Label")
axes_square.set_ylabel("Y Label")
axes_square.set_title("Square")
plt.tight_layout()
plt.show()
'''
'''
figure = plt.figure()
axes = figure.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=4)
axes.set_title("Grafik Başlığı")
plt.tight_layout()
plt.show()
'''
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(10,10))
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")
plt.tight_layout()
# plt.show()
fig.savefig("Figure1.png")