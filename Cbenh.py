class Benh:
    def __init__(self, ten, trieu_chung, dieu_tri="Chưa có thông tin"):
        self.ten = ten
        self.trieu_chung = trieu_chung  # Danh sách triệu chứng
        self.dieu_tri = dieu_tri  # Phương pháp điều trị

    def __str__(self):
        return f"{self.ten}: Triệu chứng: {', '.join(self.trieu_chung)} | Điều trị: {self.dieu_tri}"