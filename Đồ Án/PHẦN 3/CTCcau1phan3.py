import pickle
import os
#3.1
class NhanVien:
  def __init__(self, hoten, tuoi, luong):
    self.hoten = hoten
    self.tuoi = tuoi
    self.luong = luong

  def __str__(self):
      message = '[Họ tên:' + self.hoten + ';tuổi:' \
                + str(self.tuoi) + ';lương:' \
                + str(self.luong) + ']'
      return message

  def __gt__(self, obj):
      return (self.tuoi > obj.tuoi)

#3.2
def nhap_danh_sach_nhan_vien(ds):
  while True:
    hoten = input("Nhập họ tên nhân viên (nhập 'End' để kết thúc): ")
    if hoten == 'End':
      break

    tuoi = int(input("Nhập tuổi nhân viên: "))
    luong = int(input("Nhập lương nhân viên: "))
    nhanvien = NhanVien(hoten, tuoi, luong)
    ds.append(nhanvien)

#3.3
def hien_thi_danh_sach_nhan_vien(ds):
  for i, nhanvien in enumerate(ds):
    print(f"Nhân viên thứ {i+1}:")
    print(f" - Họ tên: {nhanvien.hoten}")
    print(f" - Tuổi: {nhanvien.tuoi}")
    print(f" - Lương: {nhanvien.luong}")

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
        with open(os.path.join(path, filename), 'ab') as f:
            pickle.dump(ds, f)
        print('Hoàn thành quá trình lưu dữ liệu vào tập tin')
    except Exception as e:
        print('\nXảy ra lỗi trong quá trình lưu dữ liệu:', e)

#3.6
def doc_sinhvien(path: str, filename: str):
    try:
        with open(os.path.join(path, filename), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None


def main():
  danh_sach_nhan_vien = []
  nhap_danh_sach_nhan_vien(danh_sach_nhan_vien)
  print("Danh sách nhân viên:")
  hien_thi_danh_sach_nhan_vien(danh_sach_nhan_vien)
  print("Sắp xếp nhân viên theo chiều giảm dần của độ tuổi:")
  sap_xep_danh_sach_nhan_vien(danh_sach_nhan_vien)
  print("Lưu danh sách nhân viên:")
  path = "D:/data2"
  filename = "nhanvien.txt"
  luu_sinhvien(path,filename,danh_sach_nhan_vien)
  print("Đọc danh sách nhân viên:")
  print(doc_sinhvien(path,filename))

if __name__ == '__main__':
  main()