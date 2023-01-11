import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
def surface(x,y):
  z = (x/3)**2 - (y/2)**2
  return z
def surface_draw():
  x = np.linspace(-5,5,100)
  y = np.linspace(-5,5,100)
  x, y = np.meshgrid(x, y)
  z = surface(x, y)
  fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
  surface2 = ax.plot_surface(x, y, z, cmap = 'Purples')
  ax.set_title("Đồ thị mặt yên ngựa", size = 25, font = "Times New Roman")
  plt.show()
def main():
  surface_draw()
if __name__ == '__main__':
  main()

