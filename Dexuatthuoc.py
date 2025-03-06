from CBenh import *
class Thuoc:
    def __init__(self, ten, cong_dung, tac_dung_phu, dieu_tri):
        self.ten = ten
        self.cong_dung = cong_dung
        self.tac_dung_phu = tac_dung_phu
        self.dieu_tri = dieu_tri  # Danh sách bệnh mà thuốc có thể điều trị

    def __str__(self):
        return f"{self.ten}: {self.cong_dung} (Tác dụng phụ: {', '.join(self.tac_dung_phu)})"

class NhaThuoc:
    def __init__(self):
        self.ds_thuoc = []

    def them_thuoc(self, thuoc):
        self.ds_thuoc.append(thuoc)

    def de_xuat_thuoc(self, benh):
        thuoc_de_xuat = [thuoc for thuoc in self.ds_thuoc if benh.ten in thuoc.dieu_tri]

        if thuoc_de_xuat:
            print(f"\nĐề xuất thuốc cho bệnh {benh.ten}:")
            for thuoc in thuoc_de_xuat:
                print(thuoc)
        else:
            print(f"\nKhông có thuốc phù hợp cho bệnh {benh.ten}.")

# Thêm dữ liệu thuốc
'''nha_thuoc = NhaThuoc()
nha_thuoc.them_thuoc(Thuoc("Paracetamol", "Giảm đau, hạ sốt", ["Buồn nôn", "Dị ứng"], ["Cảm cúm", "Sốt"]))
nha_thuoc.them_thuoc(Thuoc("Ibuprofen", "Giảm đau, chống viêm", ["Đau dạ dày", "Chóng mặt"], ["Viêm khớp", "Đau đầu"]))
nha_thuoc.them_thuoc(Thuoc("Loratadine", "Giảm dị ứng", ["Buồn ngủ", "Khô miệng"], ["Dị ứng"]))

# Kiểm tra với bệnh nhân nhập bệnh
benh1 = Benh("Cảm cúm", ["Sốt", "Ho", "Đau đầu", "Mệt mỏi"])
benh2 = Benh("Dị ứng", ["Ngứa", "Phát ban", "Hắt hơi"])

nha_thuoc.de_xuat_thuoc(benh1)
nha_thuoc.de_xuat_thuoc(benh2)'''