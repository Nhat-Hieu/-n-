import os.path
import pickle
import random
# a) Sinh ngẫu nhiên list các số thực trong khoảng [a, b] với độ dài n
def list(a,b,n):
  Danhsach = []
  return [random.uniform(a, b) for i in range(n)]

# b) Lưu list vào tập tin văn bản
def luulist(Danhsach, tentaptin):
  with open(tentaptin, 'w') as f:
    for x in Danhsach:
      f.write(str(x) + '\n')

# c) Sắp xếp list theo chiều giảm dần
def sapxep(Danhsach):
  Danhsach.sort(reverse=True)

# d) Lưu list ở câu (c) vào tập tin văn bản
def luulistcauc(Danhsach, tentaptin):
  with open(tentaptin, 'w') as f:
    for x in Danhsach:
      f.write(str(x) + '\n')

# e) Tìm kiếm số n trong list
def timkiem(Danhsach, n):
  if n in Danhsach:
    return True
  return False

# Chương trình chính
Danhsach = list(1,10,5)
luulist(Danhsach, 'Sinh_ngau_nhien_list.txt')
sapxep(Danhsach)
luulistcauc(Danhsach, 'Sap_xep_list.txt')
n = float(input("Nhập số cần tìm: "))
if timkiem(Danhsach, n):
  print("Số cần tìm đã tìm thấy trong danh sách")
else:
  print("Số cần tìm không tìm thấy trong danh sách")
