# Form implementation generated from reading ui file 'giaodienluu.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(170, 255, 255)\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 410, 111, 91))
        self.label_6.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Pictures/19.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 410, 101, 91))
        self.label_5.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Pictures/18.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-30, 10, 441, 41))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 410, 121, 91))
        self.label_4.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Pictures/17.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 410, 121, 91))
        self.label.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Pictures/15.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 410, 121, 91))
        self.label_2.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Pictures/16.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 751, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 280, 531, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_de_xuat_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_de_xuat_2.setEnabled(True)
        self.btn_de_xuat_2.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_de_xuat_2.setObjectName("btn_de_xuat_2")
        self.horizontalLayout.addWidget(self.btn_de_xuat_2)
        self.btn_de_xuat = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_de_xuat.setEnabled(True)
        self.btn_de_xuat.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_de_xuat.setObjectName("btn_de_xuat")
        self.horizontalLayout.addWidget(self.btn_de_xuat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#48006d;\">TÓM LƯỢC THÔNG TIN</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tên Bệnh Nhân :"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tuổi:"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Triệu chứng:"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bệnh:"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Đề Xuất Thuốc"))
        self.btn_de_xuat_2.setText(_translate("MainWindow", "Đề xuất thuốc"))
        self.btn_de_xuat.setText(_translate("MainWindow", "Thoát"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
