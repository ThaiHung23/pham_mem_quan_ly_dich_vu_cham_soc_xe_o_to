from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                           QPushButton, QTableWidget, QTextEdit, QGroupBox)

class ServiceWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        form_group = QGroupBox("Dịch vụ")
        form_layout = QHBoxLayout()

        self.txt_name = QLineEdit()
        self.txt_price = QLineEdit()
        self.txt_desc = QTextEdit()
        self.txt_desc.setMaximumHeight(60)

        form_layout.addWidget(QLabel("Tên DV:"))
        form_layout.addWidget(self.txt_name)
        form_layout.addWidget(QLabel("Giá:"))
        form_layout.addWidget(self.txt_price)
        form_layout.addWidget(QLabel("Mô tả:"))
        form_layout.addWidget(self.txt_desc)

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Thêm Dịch Vụ")
        self.btn_update = QPushButton("Cập Nhật")
        self.btn_delete = QPushButton("Xóa")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)
        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tên Dịch Vụ", "Giá", "Mô Tả"])
        layout.addWidget(self.table)

        self.setLayout(layout)