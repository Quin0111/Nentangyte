import sys
from PyQt6.QtWidgets import QApplication
from Giaodienchinh import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
