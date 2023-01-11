import os.path
import pickle
import random
#1.1
def list(a,b,n):
  # Sinh ngẫu nhiên list số thực trong khoảng [a, b] với độ dài n
  return [random.uniform(a, b) for i in range(n)]

  # Sinh ngẫu nhiên list số thực trong khoảng [1, 10] với độ dài là 5
list_moi = list(1,10,5)
print("List số thực là:",list_moi)

#1.2
def sort_list(numbers, reverse=False):
  # Sắp xếp danh sách các số theo chiều tăng dần hoặc giảm dần
  return sorted(numbers, reverse=reverse)
list_so_thuc = (list_moi)

# Sắp xếp theo chiều tăng dần
tang_dan = sort_list(list_so_thuc, reverse=False)
print("Sắp xếp theo chiều tăng dần là: ",tang_dan)
# Sắp xếp theo chiều giảm dần
giam_dan = sort_list(list_so_thuc, reverse=True)
print("Sắp xếp theo chiều giảm dần là: ",giam_dan)

#1.3
def timkiem(list, n):
  # Tìm số n trong danh sách list
  if n in list:
    # Nếu tìm thấy, lấy tất cả các vị trí có giá trị bằng với n
    vitri = [i for i, x in enumerate(list) if x == n]
    # In ra các vị trí tìm thấy
    print(f"Số {n} tìm thấy tại vị trí {vitri} trong list.")
  else:
    # Nếu không tìm thấy, in ra thông báo
    print(f"Không tìm thấy số {n} trong list.")

list = [2,4,6,6,8,8,10]
timkiem(list, 6)
timkiem(list, 8)
timkiem(list, 1)

#1.4
def luutaptin (kieutaptin, thumuc, tentaptin):
    if kieutaptin == 'vanban':
        try:
            with open(os.path.join(thumuc,tentaptin), 'w') as f:
                pickle.dump(list_moi,f)
            print("Done!")
        except Exception as e:
            print("Error!")
    else:
        try:
            with open(os.path.join(thumuc,tentaptin), 'wb') as f:
                pickle.dump(list_moi,f)
            print("Done!")
        except Exception as e:
            print("Error!")


