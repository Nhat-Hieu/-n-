import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
def spheres1(x, y):
  z1 =(4-(x+2)**2-(y-1)**2)**(1/2)+4
  return z1
def spheres2(x, y):
  z2 =-(4-(x+2)**2-(y-1)**2)**(1/2)+4
  return z2
def spheres_draw():
  x = np.linspace(-4, 0, 2000)
  y = np.linspace(-1, 3, 2000)
  x, y = np.meshgrid(x, y)
  z1 = spheres1(x, y)
  z2 = spheres2(x, y)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  mat_cau1 = ax.plot_surface(x, y, z1, cmap = 'Purples')
  mat_cau2 = ax.plot_surface(x, y, z2, cmap = 'Purples')
  ax.set_title("Đồ thị mặt cầu", size = 25, font = "Times New Roman")
  plt.show()
def main():
  spheres_draw()
if __name__ == '__main__':
  main()

