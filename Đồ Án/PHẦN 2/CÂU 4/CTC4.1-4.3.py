import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
#4.1
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

#4.2
def hyperbolic_top(x,y):
  z1 = (((x/3)**2 + (y/5)**2 -1)*4)**1/2
  return z1
def hyperbolic_bot(x,y):
  z2 = -(((x/3)**2 + (y/5)**2 - 1)*4)**1/2
  return z2
def hyperbolic_draw():
  x = np.linspace(-10, 10, 500)
  y = np.linspace(-10, 10, 500)
  x,y = np.meshgrid(x,y)
  z1 = hyperbolic_top(x,y)
  z2 = hyperbolic_bot(x,y)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  mat_hyperbolic1 = ax.plot_surface(x, y, z1,cmap = 'Purples')
  mat_hyperbolic2 = ax.plot_surface(x, y, z2,cmap = 'Purples')
  ax.set_title("Đồ thị mặt Hyperbolic",size = 25, font = "Times New Roman")
  plt.show()

#4.3
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

#4.4
def main():
    surface_draw()
    hyperbolic_draw()
    spheres_draw()
if __name__ == '__main__':
  main()




