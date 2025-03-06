from CBenh import *
from CBenhNhan import *
class TuVanBenh:
    def __init__(self):
        self.ds_benh = []

    def them_benh(self, benh):
        self.ds_benh.append(benh)

    def tu_van_benh(self, benh_nhan):
        benh_de_xuat = []
        for benh in self.ds_benh:
            if any(trieu_chung in benh.trieu_chung for trieu_chung in benh_nhan.trieu_chung):
                benh_de_xuat.append(benh)

        if benh_de_xuat:
            print(f"\nChẩn đoán bệnh cho {benh_nhan.ten}:")
            for benh in benh_de_xuat:
                print(benh)
        else:
            print(f"\nKhông xác định được bệnh cho {benh_nhan.ten}.")
