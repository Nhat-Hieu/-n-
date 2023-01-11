import numpy as np
from sympy import *
import matplotlib.pyplot as plt

# Đạo hàm y
x = symbols('x')
y = x**4 - 2*x**2 - 3
y_phay = diff(y,x)
print("Đạo hàm của y là:",y_phay)

# Đạo hàm y'
x = symbols('x')
y_phay = 4*x**3 - 4*x
y_phay_phay = diff(y_phay,x)
print("Đạo hàm của y' là:",y_phay_phay)

# Đạo hàm y''
x = symbols('x')
y_phay_phay = 12*x**2 - 4
y_phay_phay_phay = diff(y_phay_phay,x)
print("Đạo hàm của y'' là:",y_phay_phay_phay)

def ve_do_thi_ham_so(a,b,c,d,x):
  y = x**4 - 2*x**2 - 3
  return y

x = np.linspace(start=-10.0,stop=10.0, num=200)
y0 = x**4 - 2*x**2 - 3
y1 = 4*x**3 - 4*x
y2 = 12*x**2 - 4
y3 = 24*x

fig, ax = plt.subplots()
ax.plot(x,y0,marker = '+',label=r"$y = x^{4}-2x^{2}-3$")
ax.plot(x,y1,marker = '.',label=r"$y' = 4x^{3}-4x$")
ax.plot(x,y2,marker = 'x',label=r"$y'' = 12x^{2}-4$")
ax.plot(x,y3,marker = '*',label=r"$y''' = 24x$")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
ax.set_title("Đồ thị hàm số y,y',y'',y'''")
ax.legend()
plt.show()
