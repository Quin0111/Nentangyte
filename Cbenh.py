class TrieuChung:
    def __init__(self, ten, phan_tich="Chưa có thông tin"):
        self.ten = ten
        self.phan_tich = phan_tich  # Phân tích về triệu chứng

    def __str__(self):
        return f"Triệu chứng: {self.ten} | Phân tích: {self.phan_tich}"


# Ví dụ sử dụng:
tc1 = TrieuChung("Sốt", "Có thể do nhiễm trùng hoặc cảm cúm")
tc2 = TrieuChung("Ho", "Có thể do viêm họng hoặc bệnh về phổi")

print(tc1)
print(tc2)
