class BenhNhan:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def __str__(self):
        return f"Bệnh nhân {self.ten}, {self.tuoi} tuổi"

# Ví dụ sử dụng:
bn1 = BenhNhan("Nguyễn Văn A", 30)
bn2 = BenhNhan("Trần Thị B", 25)

print(bn1)
print(bn2)
