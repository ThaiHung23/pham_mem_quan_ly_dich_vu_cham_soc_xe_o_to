from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                           QPushButton, QTableWidget, QComboBox, QGroupBox)

class VehicleWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        form_group = QGroupBox("Thông tin xe")
        form_layout = QHBoxLayout()

        self.txt_plate = QLineEdit()
        self.txt_plate.setPlaceholderText("Biển số xe")
        self.txt_brand = QLineEdit()
        self.txt_brand.setPlaceholderText("Hãng xe")
        self.txt_model = QLineEdit()
        self.txt_model.setPlaceholderText("Mẫu xe")
        self.cmb_customer = QComboBox()
        self.cmb_customer.setPlaceholderText("Chọn khách hàng")

        form_layout.addWidget(QLabel("Biển số:"))
        form_layout.addWidget(self.txt_plate)
        form_layout.addWidget(QLabel("Hãng:"))
        form_layout.addWidget(self.txt_brand)
        form_layout.addWidget(QLabel("Mẫu:"))
        form_layout.addWidget(self.txt_model)
        form_layout.addWidget(QLabel("Khách hàng:"))
        form_layout.addWidget(self.cmb_customer)

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Thêm Xe")
        self.btn_update = QPushButton("Cập Nhật")
        self.btn_delete = QPushButton("Xóa")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)
        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Biển Số", "Hãng", "Mẫu", "Khách Hàng"])
        layout.addWidget(self.table)

        self.setLayout(layout)