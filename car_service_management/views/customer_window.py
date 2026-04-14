from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                           QPushButton, QTableWidget, QTableWidgetItem, QTextEdit, QGroupBox)

class CustomerWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Form
        form_group = QGroupBox("Thông tin khách hàng")
        form_layout = QHBoxLayout()

        self.txt_name = QLineEdit()
        self.txt_name.setPlaceholderText("Họ tên")
        self.txt_phone = QLineEdit()
        self.txt_phone.setPlaceholderText("Số điện thoại")
        self.txt_address = QTextEdit()
        self.txt_address.setMaximumHeight(60)
        self.txt_address.setPlaceholderText("Địa chỉ")

        form_layout.addWidget(QLabel("Họ tên:"))
        form_layout.addWidget(self.txt_name)
        form_layout.addWidget(QLabel("SĐT:"))
        form_layout.addWidget(self.txt_phone)
        form_layout.addWidget(QLabel("Địa chỉ:"))
        form_layout.addWidget(self.txt_address)

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Thêm Mới")
        self.btn_update = QPushButton("Cập Nhật")
        self.btn_delete = QPushButton("Xóa")
        self.btn_clear = QPushButton("Làm Mới")

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_clear)
        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Họ Tên", "SĐT", "Địa Chỉ"])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)

        self.setLayout(layout)