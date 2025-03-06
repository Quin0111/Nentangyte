class BenhNhan:
    def __init__(self, ten, trieu_chung):
        self.ten = ten
        self.trieu_chung = trieu_chung  # Danh sách triệu chứng

    def __str__(self):
        return f"Bệnh nhân {self.ten} có triệu chứng: {', '.join(self.trieu_chung)}"