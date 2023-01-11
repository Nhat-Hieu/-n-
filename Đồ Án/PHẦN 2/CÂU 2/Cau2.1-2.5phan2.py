#2.1
from sympy import symbols, Eq, solve

def he_phuong_trinh():
  x, y, z = symbols('x y z')
#Hệ phương trình
  eq1 = Eq(2*x - 5*y + z,-5)
  eq2 = Eq(4*x + 2*y - 2*z, 2)
  eq3 = Eq(x + y - z, 0)
  answer = solve((eq1, eq2, eq3), (x,y,z))
  print('Nghiệm của hệ phương trình là: ', answer)

#2.2
from sympy import *

def tinh_gioi_han():
  x = symbols('x')
  f = (x**1/3*sqrt(x**3-3*x*2) + sqrt(x*2 - 2*x))
  answer = limit(f, x, oo)
  print('Kết quả giới hạn: ', answer)

#2.3
from sympy import *

def tinh_dao_ham():
  x = symbols('x')
  f = (2*x-1)/(x+2)
 #Tính đạo hàm df/dx
  answer = diff(f, x)
  print("Kết quả đạo hàm là:",answer)

#2.4
from sympy import *

def tinh_nguyen_ham():
  x = symbols('x')
  f = x/(x**2+1)
  answer = integrate(f, x)
  print("Kết quả nguyên hàm là: ", answer)

#2.5
from sympy import *

def tich_phan():
#Mô tả biến
  x = symbols('x')
#Xây dựng hàm
  f = ((1-x*tan(x))/(x*x*cos(x)+x))
#Tính tích phân có giới hạn
  answer = integrate(f, (x,(2*pi/3),pi))
  print("Kết quả tích phân là: ", answer)