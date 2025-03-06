from PyQt6 import QtWidgets, uic
import sys
from CBenh import *
from CBenhNhan import *
from Tuvanbenh import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('giaodien.ui', self)

        # Liên kết nút mở cửa sổ thứ hai
        self.pushButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()  # Đóng cửa sổ hiện tại

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        uic.loadUi('giaodientuvan.ui', self)

        self.analyze_button_3.clicked.connect(self.open_third_window)

    def open_third_window(self):
        self.third_window = ThirdWindow()  # Không cần truyền tham số
        self.third_window.show()
        self.close()

class ThirdWindow(QtWidgets.QMainWindow):
    def __init__(self):  # Xóa tham số main_window và second_window
        super(ThirdWindow, self).__init__()
        uic.loadUi('giaodiendexuatthuoc.ui', self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
