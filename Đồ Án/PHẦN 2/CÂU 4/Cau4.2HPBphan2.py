import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
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
def main():
  hyperbolic_draw()
if __name__ == '__main__':
  main()