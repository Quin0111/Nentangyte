# Form implementation generated from reading ui file 'giaodienthoat.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 400)
        Form.setStyleSheet("background-color:rgb(170, 255, 255)\n"
"\n"
"")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 571, 71))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 140, 401, 80))
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
        self.btn_next = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_next.setEnabled(True)
        self.btn_next.setStyleSheet("font: 87 italic 10pt \"Segoe UI Black\";\n"
"\n"
"background: rgb(85, 255, 255)")
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(140, 230, 191, 121))
        self.label_2.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Pictures/6.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(340, 230, 191, 121))
        self.label_3.setStyleSheet("border: 3px solid rgb(12, 38, 127); /* Viền màu đỏ dày 3px */\n"
"border-radius: 9px;    /* Bo tròn góc */\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Pictures/7.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#48006d;\">Bạn có chắc chắn muốn thoát hệ thống không?</span></p></body></html>"))
        self.btn_predict.setText(_translate("Form", "Thoát"))
        self.btn_next.setText(_translate("Form", "Huỷ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
