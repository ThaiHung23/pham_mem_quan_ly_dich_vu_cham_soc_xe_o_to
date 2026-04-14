# views/invoice_window.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTableWidget, QGroupBox)

class InvoiceWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.btn_paid = QPushButton("✅ Đánh Dấu Đã Thanh Toán")
        layout.addWidget(self.btn_paid)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Khách hàng", "Tổng tiền", "Trạng thái", "Ngày tạo"])
        layout.addWidget(self.table)

        self.setLayout(layout)