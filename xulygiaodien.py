import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from giaodien import Ui_MainWindow
from CTuvanbenh import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        #Khởi tạo hệ thống tư vấn bệnh
        self.he_thong_tu_van = TuVanBenh()
        self.khoi_tao_du_lieu()

        self.dinhnghianutlenh()

    def khoi_tao_du_lieu(self):
        """Thêm các bệnh và triệu chứng vào hệ thống"""
        self.he_thong_tu_van.them_benh(Benh("Cảm cúm", ["Sốt", "Ho", "Đau đầu", "Mệt mỏi"]))
        self.he_thong_tu_van.them_benh(Benh("Dị ứng", ["Ngứa", "Phát ban", "Hắt hơi"]))
        self.he_thong_tu_van.them_benh(Benh("Viêm họng", ["Đau họng", "Sốt", "Ho"]))

    def dinhnghianutlenh(self):
        self.uic.pushButton.clicked.connect(self.Du_doan)

    def Ho_ten(self):
        ho_ten = self.uic.lineEdit.text().strip()
        if ho_ten:
            print(f"Họ tên: {ho_ten}")
        else:
            print("Vui lòng nhập họ tên")

    def Trieu_chung(self):
        trieu_chung = self.uic.lineEdit_2.text().strip()
        if trieu_chung:
            print(f"Triệu chứng: {trieu_chung}")
        else:
            print("Vui lòng nhập triệu chứng")

    def Du_doan(self):
        trieu_chung_nhap = self.uic.lineEdit_2.text().split(",")
        trieu_chung_nhap = [tc.strip() for tc in trieu_chung_nhap]
        ket_qua = self.he_thong_tu_van.tu_van_benh(trieu_chung_nhap)
        self.uic.lineEdit_3.setText("\n".join(ket_qua))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
