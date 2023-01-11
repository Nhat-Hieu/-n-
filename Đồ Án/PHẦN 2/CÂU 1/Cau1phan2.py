#1.1
import numpy as np

def cau11(A,x):
  return np.dot(A,x)

#Thay giá trị
  A = np.array([[3, 5], [2, 4]])
  x = np.array([2, 5])
  tich = cau11(A,x)
  print("Kết quả tính tích x.A là: ")
  print(tich)

#1.2
import numpy as np

def cau12(A, B):
# Tính tích ma trận A^o B
  tich_ma_tran = np.dot(A, B)

def phep_nhan_hadamard(A,B):
  return np.multiply(A,B)

def nhan_chuyen_vi(A, B):
  A_chuyen_vi = A.T
  return np.dot(A_chuyen_vi,B)


