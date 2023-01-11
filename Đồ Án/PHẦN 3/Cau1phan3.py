import os
import pickle
#3.1
class NhanVien:
    def __init__(self, hoten:str, tuoi:int, luong:int):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong
    def __str__(self) -> str:
        message = "[Họ tên: " + self.hoten + ";tuổi: " + str(self.tuoi) + ";lương:" + str(self.luong)
        return message

#3.2
def nhap_danh_sach_nhan_vien(ds):
    while True:
        hoten = input("Nhập họ tên nhân viên (nhập 'k' để kết thúc): ")
        if hoten == "k":
            break
        tuoi = int(input("Nhập tuổi: "))
        luong = int(input("Nhập lương: "))
        nv = NhanVien(hoten, tuoi, luong)
        ds.append(nv)

#3.3
def hien_thi_danh_sach_nhan_vien(ds):
    for i, nv in enumerate(ds):
        print(f"Nhân viên thứ {i+1}:")
        print(f" - Họ tên: {nv.hoten}")
        print(f" - Tuổi: {nv.tuoi}")
        print(f" - Lương: {nv.luong}")

#3.4
def sap_xep_danh_sach_nhan_vien(ds):
  sx = sorted(ds,reverse=True)
  print(sx)
  for item in sx:
    print(item)

#3.5
def luu_sinhvien(path: str, filename: str, ds):
    try:
        # mo file che do ghi tiep o dang nhi phan
        with open(os.path.join("D:/data2", "nhanvien.txt"), 'ab') as f:
            pickle.dump(ds, f)
        print('Hoàn thành quá trình lưu dữ liệu vào tập tin')
    except Exception as e:
        print('\nXảy ra lỗi trong quá trình lưu dữ liệu:', e)

#3.6
def doc_sinhvien(path: str, filename: str):
    try:
        with open(os.path.join(path = "D:/data2", filename = "nhanvien.txt"), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None


