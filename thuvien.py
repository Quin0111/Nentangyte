import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from textblob import TextBlob

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

# Đọc và chuẩn bị dữ liệu
print("Đang đọc dữ liệu từ file 'dataset.csv'...")
du_lieu = pd.read_csv('dataset.csv')

print("Đang chuẩn bị dữ liệu...")
du_lieu = du_lieu.rename(columns={
    'Fever': 'Sốt',
    'Cough': 'Ho',
    'Fatigue': 'Mệt mỏi',
    'Difficulty Breathing': 'Khó thở',
    'Gender': 'Giới tính',
    'Blood Pressure': 'Huyết áp',
    'Cholesterol Level': 'Mức cholesterol'
})

for cot in ['Sốt', 'Ho', 'Mệt mỏi', 'Khó thở']:
    du_lieu[cot] = du_lieu[cot].map({'Yes': 1, 'No': 0})
du_lieu['Giới tính'] = du_lieu['Giới tính'].map({'Male': 0, 'Female': 1})
du_lieu['Huyết áp'] = du_lieu['Huyết áp'].map({'Low': 0, 'Normal': 1, 'High': 2})
du_lieu['Mức cholesterol'] = du_lieu['Mức cholesterol'].map({'Low': 0, 'Normal': 1, 'High': 2})
du_lieu = du_lieu.dropna()

dac_trung = du_lieu.drop(columns=['Disease', 'Outcome Variable'])
nhan = du_lieu['Disease']

tap_huan_luyen, tap_kiem_tra, nhan_huan_luyen, nhan_kiem_tra = train_test_split(
    dac_trung, nhan, test_size=0.2, random_state=42
)

print("Đang huấn luyện mô hình...")
mo_hinh = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)
mo_hinh.fit(tap_huan_luyen, nhan_huan_luyen)
do_chinh_xac = accuracy_score(nhan_kiem_tra, mo_hinh.predict(tap_kiem_tra))
print(f"Độ chính xác của mô hình: {do_chinh_xac * 100:.2f}%")
joblib.dump(mo_hinh, 'mo_hinh_benh.pkl')

# Hàm dự đoán bệnh và đề xuất thuốc
def du_doan_benh_va_thuoc(thong_tin_nguoi_dung, mo_hinh):
    for cot in dac_trung.columns:
        if cot not in thong_tin_nguoi_dung:
            thong_tin_nguoi_dung[cot] = 0
    bang_du_lieu = pd.DataFrame([thong_tin_nguoi_dung], columns=dac_trung.columns)
    benh_du_doan = mo_hinh.predict(bang_du_lieu)[0]
    benh_tieng_viet_du_doan = benh_tieng_viet.get(benh_du_doan, benh_du_doan)
    thuoc_de_xuat = benh_thuoc.get(benh_du_doan, "Không có thông tin về thuốc cho bệnh này.")
    return benh_tieng_viet_du_doan, thuoc_de_xuat

# Hàm mã hóa văn bản tự nhiên bằng TextBlob
def ma_hoa_trieu_chung_van_ban(van_ban):
    trieu_chung = {}
    blob = TextBlob(van_ban.lower())

    # Danh sách triệu chứng và từ khóa liên quan
    trieu_chung_keywords = {
        'Sốt': ['sốt', 'nóng', 'sốt cao', 'bốc hỏa', 'tăng nhiệt', 'phát sốt', 'sốt nhẹ', 'sốt rét'],
        'Ho': ['ho', 'khục', 'ho khan', 'ho đờm', 'ho dai dẳng', 'ho dữ dội', 'ho rát họng'],
        'Mệt mỏi': ['mệt', 'mệt mỏi', 'kiệt sức', 'đuối sức', 'yếu ớt', 'rã rời', 'uể oải', 'hụt hơi'],
        'Khó thở': ['khó thở', 'thở khó', 'ngạt thở', 'tức thở', 'khó hít thở', 'thở dốc'],
        'Đau đầu': ['đau đầu', 'nhức đầu', 'choáng đầu', 'đau nặng đầu', 'đau nhói đầu'],
        'Buồn nôn': ['buồn nôn', 'nôn nao', 'cồn cào', 'muốn ói', 'khó chịu dạ dày'],
        'Nôn': ['nôn', 'ói', 'mửa', 'thổ tả', 'tống thức ăn'],
        'Tiêu chảy': ['tiêu chảy', 'đi ngoài', 'đi tướt', 'phân lỏng', 'đi phân nước'],
        'Đau ngực': ['đau ngực', 'tức ngực', 'đè nặng ngực', 'đau nhói ngực', 'đau thắt ngực'],
        'Chóng mặt': ['chóng mặt', 'hoa mắt', 'quay cuồng', 'xây xẩm', 'lảo đảo', 'mất thăng bằng']
    }

    # Từ khóa thông tin bổ sung
    gioi_tinh_keywords = {'nam': 0, 'nữ': 1}
    huyet_ap_keywords = {'thấp': 0, 'bình thường': 1, 'cao': 2}
    cholesterol_keywords = {'thấp': 0, 'bình thường': 1, 'cao': 2}

    # Xử lý văn bản
    words = blob.words  # Chia nhỏ văn bản thành các từ
    van_ban_lower = van_ban.lower()

    # Kiểm tra triệu chứng
    for trieu_chung_key, keywords in trieu_chung_keywords.items():
        if any(keyword in van_ban_lower for keyword in keywords):
            trieu_chung[trieu_chung_key] = 1

    # Kiểm tra tuổi
    for word in words:
        if word.isdigit():
            tuoi = int(word)
            if 0 <= tuoi <= 120:
                trieu_chung['Age'] = tuoi

    # Kiểm tra giới tính
    for key, value in gioi_tinh_keywords.items():
        if key in van_ban_lower:
            trieu_chung['Giới tính'] = value

    # Kiểm tra huyết áp
    for key, value in huyet_ap_keywords.items():
        if key in van_ban_lower:
            trieu_chung['Huyết áp'] = value

    # Kiểm tra mức cholesterol
    for key, value in cholesterol_keywords.items():
        if key in van_ban_lower:
            trieu_chung['Mức cholesterol'] = value

    return trieu_chung

# Hàm nhập triệu chứng tự nhiên
def nhap_trieu_chung_tu_nhien():
    print("\nNhập các triệu chứng và thông tin của bạn (dưới dạng văn bản tự nhiên):")
    print("Ví dụ: 'Tôi bị sốt, ho, khó thở, 30 tuổi, nam, huyết áp cao'")

    while True:
        van_ban = input("Nhập triệu chứng và thông tin của bạn: ").strip()
        if not van_ban:
            print("Vui lòng nhập ít nhất một triệu chứng hoặc thông tin!")
            continue

        trieu_chung = ma_hoa_trieu_chung_van_ban(van_ban)
        if trieu_chung:
            break
        else:
            print("Không nhận diện được triệu chứng hoặc thông tin nào. Vui lòng thử lại!")

    return trieu_chung

# Chạy chương trình
while True:
    trieu_chung = nhap_trieu_chung_tu_nhien()
    benh, thuoc = du_doan_benh_va_thuoc(trieu_chung, mo_hinh)
    print(f"\nBệnh dự đoán: {benh}")
    print(f"Thuốc đề xuất: {thuoc}")

    tiep_tuc = input("Bạn muốn tiếp tục chẩn đoán không? (c/k): ").lower()
    if tiep_tuc != 'c':
        break

print("Cảm ơn bạn đã sử dụng chương trình!")