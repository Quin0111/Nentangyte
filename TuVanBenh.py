from CTrieuchung import *
from CBenhNhan import *
class TuVanBenh:
    def __init__(self):
        self.ds_benh = []
        self.kho_thuoc = {
            "Cảm cúm": ["Paracetamol", "Vitamin C"],
            "Dị ứng": ["Loratadine", "Cetirizine"],
            "Viêm họng": ["Strepsils", "Kháng sinh (nếu cần)"],

            # Thêm thuốc cho các bệnh mới
            "Viêm phổi": ["Kháng sinh (theo chỉ định bác sĩ)", "Paracetamol"],
            "Đau dạ dày": ["Omeprazole", "Antacid"],
            "Tiêu chảy": ["ORS (Oresol)", "Loperamide"],
            "Sốt xuất huyết": ["Bù nước (Oresol)", "Paracetamol"],
            "Covid-19": ["Hạ sốt (Paracetamol)", "Vitamin tổng hợp", "Thuốc ho"],
            "Viêm xoang": ["Thuốc xịt mũi (Natri clorid 0.9%)", "Kháng histamin"],
            "Đau thần kinh tọa": ["Paracetamol", "Ibuprofen", "Thuốc giãn cơ"],
            "Thiếu máu": ["Sắt (Ferrous sulfate)", "Vitamin B12", "Acid folic"],
            "Sỏi thận": ["Thuốc giảm đau (Ibuprofen)", "Thuốc lợi tiểu", "Tăng uống nước"],
            "Gout": ["Colchicine", "Allopurinol", "Thuốc kháng viêm"],
            "Viêm da cơ địa": ["Thuốc bôi corticoid", "Kem dưỡng ẩm", "Thuốc kháng histamin"],
            "Bệnh trào ngược dạ dày": ["Omeprazole", "Esomeprazole", "Thuốc trung hòa axit"],
            "Huyết áp cao": ["Amlodipine", "Losartan", "Thuốc lợi tiểu"]
        }

    def them_benh(self, benh):
        self.ds_benh.append(benh)

    def tu_van_benh(self, trieu_chung_nhap):
        benh_de_xuat = []
        thuoc_de_xuat = []

        for benh in self.ds_benh:
            if any(trieu_chung in benh.trieu_chung for trieu_chung in trieu_chung_nhap):
                benh_de_xuat.append(benh.ten)
                if benh.ten in self.kho_thuoc:
                    thuoc_de_xuat.extend(self.kho_thuoc[benh.ten])

        if benh_de_xuat:
            return benh_de_xuat, list(set(thuoc_de_xuat))  # Trả về danh sách bệnh & thuốc (loại bỏ trùng)
        else:
            return ["Không xác định được bệnh"], []
