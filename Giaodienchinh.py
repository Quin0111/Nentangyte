import sys
import pandas as pd
import joblib
from textblob import TextBlob
from PyQt6 import QtCore, QtWidgets, uic

# --------------------------
# Từ điển ánh xạ bệnh & thuốc
# --------------------------
# Từ điển ánh xạ bệnh sang tiếng Việt
benh_tieng_viet = {
    'Influenza': 'Cúm',
    'Common Cold': 'Cảm lạnh',
    'Eczema': 'Chàm',
    'Asthma': 'Hen suyễn',
    'Hyperthyroidism': 'Cường giáp',
    'Pneumonia': 'Viêm phổi',
    'Diabetes': 'Tiểu đường',
    'Depression': 'Trầm cảm',
    'Migraine': 'Đau nửa đầu',
    'Allergic Rhinitis': 'Viêm mũi dị ứng',
    'Anxiety Disorders': 'Rối loạn lo âu',
    'Gastroenteritis': 'Viêm dạ dày ruột',
    'Pancreatitis': 'Viêm tụy',
    'Rheumatoid Arthritis': 'Viêm khớp dạng thấp',
    'Liver Cancer': 'Ung thư gan',
    'Stroke': 'Đột quỵ',
    'Urinary Tract Infection': 'Nhiễm trùng đường tiết niệu',
    'Dengue Fever': 'Sốt xuất huyết',
    'Hepatitis': 'Viêm gan',
    'Kidney Cancer': 'Ung thư thận',
    'Muscular Dystrophy': 'Loạn dưỡng cơ',
    'Sinusitis': 'Viêm xoang',
    'Ulcerative Colitis': 'Viêm loét đại tràng',
    'Bipolar Disorder': 'Rối loạn lưỡng cực',
    'Bronchitis': 'Viêm phế quản',
    'Cerebral Palsy': 'Bại não',
    'Colorectal Cancer': 'Ung thư đại trực tràng',
    'Hypertensive Heart Disease': 'Bệnh tim tăng huyết áp',
    'Multiple Sclerosis': 'Đa xơ cứng',
    'Myocardial Infarction (Heart...)': 'Nhồi máu cơ tim',
    'Osteoporosis': 'Loãng xương',
    'Hypertension': 'Tăng huyết áp',
}

# Từ điển ánh xạ bệnh sang thuốc
benh_thuoc = {
    'Influenza': 'Thuốc kháng virus (Tamiflu), thuốc hạ sốt (Paracetamol)',
    'Common Cold': 'Thuốc giảm đau, hạ sốt (Paracetamol), thuốc trị nghẹt mũi (Phenylephrine)',
    'Eczema': 'Kem bôi corticosteroid, thuốc kháng histamine',
    'Asthma': 'Thuốc giãn phế quản (Salbutamol), thuốc corticosteroid dạng hít',
    'Hyperthyroidism': 'Thuốc kháng giáp (Methimazole), thuốc chẹn beta (Propranolol)',
    'Pneumonia': 'Kháng sinh (Amoxicillin, Azithromycin), thuốc hạ sốt (Paracetamol)',
    'Diabetes': 'Insulin, thuốc hạ đường huyết (Metformin)',
    'Depression': 'Thuốc chống trầm cảm (Fluoxetine, Sertraline)',
    'Migraine': 'Thuốc giảm đau (Ibuprofen), thuốc đặc trị migraine (Sumatriptan)',
    'Allergic Rhinitis': 'Thuốc kháng histamine (Loratadine), thuốc xịt mũi corticosteroid',
    'Anxiety Disorders': 'Thuốc chống lo âu (Benzodiazepines), thuốc chống trầm cảm',
    'Gastroenteritis': 'Thuốc chống nôn (Domperidone), thuốc bù nước và điện giải (Oresol)',
    'Pancreatitis': 'Thuốc giảm đau (Morphine), thuốc ức chế men tụy',
    'Rheumatoid Arthritis': 'Thuốc chống viêm không steroid (NSAIDs), thuốc ức chế miễn dịch (Methotrexate)',
    'Liver Cancer': 'Hóa trị liệu, thuốc nhắm mục tiêu (Sorafenib)',
    'Stroke': 'Thuốc chống đông máu (Warfarin), thuốc hạ huyết áp',
    'Urinary Tract Infection': 'Kháng sinh (Ciprofloxacin, Nitrofurantoin)',
    'Dengue Fever': 'Thuốc hạ sốt (Paracetamol), bù nước và điện giải',
    'Hepatitis': 'Thuốc kháng virus (Interferon, Ribavirin)',
    'Kidney Cancer': 'Thuốc nhắm mục tiêu (Sunitinib), hóa trị liệu',
    'Muscular Dystrophy': 'Thuốc corticosteroid, vật lý trị liệu',
    'Sinusitis': 'Thuốc kháng sinh (Amoxicillin), thuốc thông mũi',
    'Ulcerative Colitis': 'Thuốc chống viêm (Mesalamine), thuốc ức chế miễn dịch',
    'Bipolar Disorder': 'Thuốc ổn định tâm trạng (Lithium), thuốc chống loạn thần',
    'Bronchitis': 'Thuốc kháng sinh (Amoxicillin), thuốc giảm ho',
    'Cerebral Palsy': 'Vật lý trị liệu, thuốc giãn cơ',
    'Colorectal Cancer': 'Hóa trị liệu, thuốc nhắm mục tiêu (Cetuximab)',
    'Hypertensive Heart Disease': 'Thuốc hạ huyết áp, thuốc lợi tiểu',
    'Multiple Sclerosis': 'Thuốc điều trị đặc hiệu (Interferon beta), thuốc giảm triệu chứng',
    'Myocardial Infarction (Heart...)': 'Thuốc chống đông máu (Aspirin), thuốc giãn mạch (Nitroglycerin)',
    'Osteoporosis': 'Thuốc bổ sung canxi, thuốc chống loãng xương (Bisphosphonates)',
    'Hypertension': 'Thuốc hạ huyết áp (ACE inhibitors), thuốc lợi tiểu',
}

# MainWindow (Cửa sổ 1)
# --------------------------
from PyQt6.QtWidgets import QFileDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("giaodien.ui", self)  # Load giao diện

        self.data = {}  # Lưu dữ liệu nhập

        # Kết nối sự kiện nút mở cửa sổ 2
        self.btn_open_second.clicked.connect(self.open_second_window)

    def open_second_window(self):
        """Lưu dữ liệu nhập và mở cửa sổ thứ 2"""
        try:
            # Lưu thông tin nhập vào self.data
            self.data["Tên Bệnh Nhân"] = self.input_ten.text()
            self.data["Tuổi"] = self.input_tuoi.text()

            print("📁 Dữ liệu lưu trong MainWindow:", self.data)

            self.second_window = SecondWindow(self.data)  # Truyền dữ liệu
            self.second_window.show()
            self.close()
        except Exception as e:
            print("❌ Lỗi khi mở cửa sổ 2:", e)



# --------------------------
# SecondWindow (Cửa sổ 2)
# --------------------------
class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self, data=None):  # Thêm tham số `data`
        super(SecondWindow, self).__init__()
        uic.loadUi('giaodientuvan.ui', self)
        self.data = data  # Nhận dữ liệu từ cửa sổ 1
        self.input_trieuchung.setEnabled(True)  # Bật lại ô nhập
        self.input_trieuchung.setReadOnly(False)  # Cho phép nhập liệu
        self.input_trieuchung.clear()  # Xóa nội dung cũ nếu có
        self.input_trieuchung.setFocus()  # Đặt con trỏ chuột vào ô nhập


        # Kiểm tra thuộc tính của QLineEdit có objectName là symptom_input_2
        print("Enabled:", self.input_trieuchung.isEnabled())  # Nên in ra True
        print("ReadOnly:", self.input_trieuchung.isReadOnly())  # Nên in ra False

        # Các phần khởi tạo khác...

        # Tải mô hình dự đoán bệnh
        self.model = joblib.load('mo_hinh_benh.pkl')
        # Các đặc trưng mô hình yêu cầu
        self.features = ['Sốt', 'Ho', 'Mệt mỏi', 'Khó thở', 'Age', 'Giới tính', 'Huyết áp', 'Mức cholesterol']

        # Biến lưu bệnh dự đoán
        self.current_disease = None

        # Kết nối các nút:
        # - btn_predict: nút Phân Tích
        # - btn_next: nút Tiếp Tục
        self.btn_predict.clicked.connect(self.phan_tich_benh)
        self.btn_open_third.clicked.connect(self.open_third_window)
        self.btn_open_main.clicked.connect(self.open_main_window)

    def phan_tich_benh(self):
        # Lấy nội dung từ QLineEdit symptom_input_2
        van_ban = self.input_trieuchung.text().strip()
        if not van_ban:
            self.result_text.setText("Vui lòng nhập triệu chứng!")
            return
        self.data['triệu chứng'] = van_ban  # Lưu vào biến data
        # Mã hóa triệu chứng -> dict { 'Sốt':1, 'Ho':0, ...}
        trieu_chung = self.ma_hoa_trieu_chung(van_ban)
        if not trieu_chung:
            self.result_text.setText("Không nhận diện được triệu chứng nào!")
            return

        # Điền đủ cột
        for ft in self.features:
            if ft not in trieu_chung:
                trieu_chung[ft] = 0

        # Tạo DataFrame để dự đoán
        df = pd.DataFrame([trieu_chung], columns=self.features)
        benh_du_doan = self.model.predict(df)[0]

        # Lưu bệnh gốc (tiếng Anh)
        self.current_disease = benh_du_doan
        print("Bệnh dự đoán trong phan_tich_benh():", self.current_disease)  # Kiểm tra giá trị

        # Chuyển sang tiếng Việt
        benh_tv = benh_tieng_viet.get(benh_du_doan, benh_du_doan)
        self.result_text.setText(f"Bệnh dự đoán: {benh_tv}")

    def open_third_window(self):
        print("➡️ Đang chạy open_third_window()...")
        if self.current_disease is None:
            print("⚠️ current_disease đang là None, thử chạy phan_tich_benh()...")
            self.phan_tich_benh()

            if self.current_disease is None:
                print("❌ Vẫn không có bệnh, dừng lại!")
                self.result_text.setText("Hãy phân tích bệnh trước!")
                return

        print("✅ current_disease hợp lệ, mở cửa sổ 3 với bệnh:", self.current_disease)

        try:
            self.third_window = ThirdWindow(self.current_disease, self.data, self)
            print("🎉 Cửa sổ 3 được khởi tạo thành công!")

            # Kiểm tra show()

            self.third_window.show()
            self.hide()
            print("📌 Cửa sổ 3 đã hiển thị!")
        except Exception as e:
            print("❌ Lỗi khi mở cửa sổ 3:", e)  # Hiển thị lỗi nếu có

    def open_main_window(self):

        # Mở cửa sổ 3, truyền bệnh đã dự đoán
        self.main_window = MainWindow()  # Không truyền self.current_disease nếu MainWindow không hỗ trợ
        self.main_window.show()
        self.close()  # Đóng cửa sổ 2

    def ma_hoa_trieu_chung(self, text):
        blob = TextBlob(text.lower())
        trieu_chung_map = {
            'Sốt': ['sốt', 'nóng', 'bốc hỏa'],
            'Ho': ['ho', 'khục', 'ho khan'],
            'Mệt mỏi': ['mệt', 'kiệt sức'],
            'Khó thở': ['khó thở', 'thở dốc'],
        }
        result = {}
        for key, kw_list in trieu_chung_map.items():
            if any(k in text.lower() for k in kw_list):
                result[key] = 1
        return result


# --------------------------
# ThirdWindow (Cửa sổ 3)
# --------------------------


class ThirdWindow(QtWidgets.QMainWindow):
    def __init__(self, disease, data, parent=None):  # Thêm parent=None
        self.data = data  # Lưu biến data

        super(ThirdWindow, self).__init__(parent)
        print("🚀 Đang mở cửa sổ 3...")
        print("📌 Bệnh nhận được trong ThirdWindow:", disease)
        try:
            uic.loadUi('giaodiendexuatthuoc.ui', self)
            print("✅ Giao diện cửa sổ 3 đã tải thành công!")
        except Exception as e:
            print("❌ Lỗi khi tải giao diện cửa sổ 3:", e)
            return

        self.current_disease = disease
        self.btn_de_xuat.clicked.connect(self.de_xuat_thuoc)
        self.btn_open_second.clicked.connect(self.open_second_window)
        self.btn_open_fourth.clicked.connect(self.open_fourth_window)

    def open_fourth_window(self):
        print("📁 Đang mở cửa sổ lưu...")  # Kiểm tra xem hàm có chạy không
        try:
            self.fourth_window = FourthWindow(self.data)  # Truyền data
            self.fourth_window.show()
            print("✅ Cửa sổ lưu đã mở!")  # Kiểm tra xem cửa sổ có mở không
        except Exception as e:
            print(f"❌ Lỗi khi mở cửa sổ lưu: {e}")  # Hiển thị lỗi nếu có

            """Mở cửa sổ thứ 4"""
            print("➡ Dữ liệu truyền sang cửa sổ 4:")
            print("Tên bệnh nhân:", self.patient_name)
            print("Tuổi:", self.patient_age)
            print("Triệu chứng:", self.symptom_text)
            print("Bệnh:", self.current_disease)
            print("Đề xuất thuốc:", self.suggested_medicine)

    def de_xuat_thuoc(self):
        print("🛠 Đang đề xuất thuốc cho:", self.current_disease)

    def de_xuat_thuoc(self):
        if not self.current_disease:
            self.input_dexuathuoc.setText("Chưa có bệnh, vui lòng dự đoán trước!")
            return

        thuoc = benh_thuoc.get(self.current_disease, "Không có thông tin về thuốc.")
        benh_tv = benh_tieng_viet.get(self.current_disease, self.current_disease)

        self.input_dexuathuoc.setText(f"Thuốc đề xuất: {thuoc}")
        self.data['bệnh dự đoán'] = benh_tv  # Lưu bệnh vào data
        self.data['thuốc đề xuất'] = thuoc  # Lưu thuốc vào data

    def open_second_window(self):

        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()  # Đóng cửa sổ 3


# Mở cửa sổ thứ 4

class FourthWindow(QtWidgets.QMainWindow):
    def __init__(self, data, parent=None):
        super(FourthWindow, self).__init__(parent)
        self.data = data
        self.current_disease = data.get('bệnh dự đoán', 'Không có bệnh')
        try:
            uic.loadUi('giaodienluu.ui', self)
        except Exception as e:
            print(f"Lỗi khi tải giao diện lưu: {e}")
            return
        self.btn_luu_tt.clicked.connect(self.load_data_to_table)
        self.btn_open_thoat.clicked.connect(self.open_fifth_window)

    def open_fifth_window(self):
        """Mở cửa sổ thứ 5 (giao diện thoát)"""
        print("📁 Đang mở cửa sổ thoát...")
        self.fifth_window = FifthWindow(self.current_disease)
        self.fifth_window.show()
        print("✅ Cửa sổ thoát đã mở!")

    def load_data_to_table(self):
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(1)
        row_headers = ["Tên Bệnh Nhân", "Tuổi", "Triệu chứng", "Bệnh", "Đề Xuất Thuốc"]
        self.tableWidget.setVerticalHeaderLabels(row_headers)

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(self.data.get('Tên Bệnh Nhân', 'Không có')))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(self.data.get('Tuổi', 'Không có')))
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem(self.data.get('triệu chứng', 'Không có')))
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem(self.data.get('bệnh dự đoán', 'Không có')))
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem(self.data.get('thuốc đề xuất', 'Không có')))

        print("Data in FourthWindow:", self.data)
        # Tiếp tục với mã trên


# Mở cửa sổ thứ 5

class FifthWindow(QtWidgets.QWidget):
    def __init__(self, disease, parent=None):
        super(FifthWindow, self).__init__(parent)
        try:
            uic.loadUi('giaodienthoat.ui', self)
        except Exception as e:
            print(f"Lỗi khi tải giao diện thoát: {e}")
            return
        self.current_disease = disease

        # Gắn sự kiện khi nhấn nút mở giao diện thoát
        # self.btn_open_thoat.clicked.connect(self.open_exit_screen)
        self.btn_predict.clicked.connect(self.exit_application)
        self.btn_next.clicked.connect(self.cancel_exit)

    def exit_application(self):
        """Thoát hoàn toàn chương trình"""
        QtWidgets.QApplication.quit()  # Thoát toàn bộ ứng dụng

    def cancel_exit(self):
        """Đóng cửa sổ thoát mà không thoát chương trình"""
        self.close()  # Chỉ đóng cửa sổ thoát




