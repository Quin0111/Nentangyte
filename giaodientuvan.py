# Form implementation generated from reading ui file 'giaodientuvan.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 374)
        MainWindow.setStyleSheet("background-color:rgb(170, 255, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(200, 180, 531, 41))
        self.result_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid royalblack; /* Viền màu xanh dương đậm */\n"
"border-radius: 10px;    /* Bo tròn góc */")
        self.result_text.setReadOnly(True)
        self.result_text.setObjectName("result_text")
        self.trieuchung = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.trieuchung.setGeometry(QtCore.QRect(200, 100, 531, 31))
        self.trieuchung.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.trieuchung.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid royalblack; /* Viền màu xanh dương đậm */\n"
"border-radius: 10px;    /* Bo tròn góc */")
        self.trieuchung.setObjectName("trieuchung")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 50, 131, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 140, 161, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 131, 111))
        self.label_5.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Pictures/14.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 131, 111))
        self.label_6.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Pictures/19.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 240, 521, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_predict = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_predict.setEnabled(True)
        self.btn_predict.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_predict.setObjectName("btn_predict")
        self.horizontalLayout.addWidget(self.btn_predict)
        self.btn_open_third = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_open_third.setEnabled(True)
        self.btn_open_third.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_open_third.setObjectName("btn_open_third")
        self.horizontalLayout.addWidget(self.btn_open_third)
        self.btn_open_main = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_open_main.setEnabled(True)
        self.btn_open_main.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_open_main.setObjectName("btn_open_main")
        self.horizontalLayout.addWidget(self.btn_open_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tư Vấn Y Tế"))
        self.result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#48006d;\">TƯ VẤN THUỐC </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#48006d;\">Triệu chứng:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#48006d;\">Chẩn đoán bệnh:</span></p></body></html>"))
        self.btn_predict.setText(_translate("MainWindow", "Phân tích"))
        self.btn_open_third.setText(_translate("MainWindow", "Đề xuất"))
        self.btn_open_main.setText(_translate("MainWindow", "Quay Lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
