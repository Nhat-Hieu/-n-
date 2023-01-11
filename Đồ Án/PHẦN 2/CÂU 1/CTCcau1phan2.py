from Cau1phan2 import *
A = np.array([[3, 5], [2, 4]])
B = np.array([[1, 3], [5, 7]])
x = np.array([2, 5])
tich = cau11(A,x)
b = phep_nhan_hadamard(A,B)
print("Phép nhân hadamard của A và B là:\n", b)

c = nhan_chuyen_vi(A,B)
print("Phép nhân ma trận chuyển vị A và B là:\n", c)

