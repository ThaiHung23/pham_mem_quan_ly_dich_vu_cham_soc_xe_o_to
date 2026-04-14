# views/appointment_window.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, 
                           QPushButton, QTableWidget, QComboBox, QGroupBox)
from PyQt6.QtCore import QDate

class AppointmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        form = QGroupBox("Đặt lịch")
        fl = QHBoxLayout()
        self.cmb_customer = QComboBox()
        self.cmb_vehicle = QComboBox()
        self.cmb_service = QComboBox()
        self.date_appointment = QDateEdit()
        self.date_appointment.setDate(QDate.currentDate())

        fl.addWidget(QLabel("Khách:"))
        fl.addWidget(self.cmb_customer)
        fl.addWidget(QLabel("Xe:"))
        fl.addWidget(self.cmb_vehicle)
        fl.addWidget(QLabel("Dịch vụ:"))
        fl.addWidget(self.cmb_service)
        fl.addWidget(QLabel("Ngày:"))
        fl.addWidget(self.date_appointment)

        form.setLayout(fl)
        layout.addWidget(form)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Đặt Lịch")
        btn_layout.addWidget(self.btn_add)
        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Khách", "Xe", "Dịch vụ", "Thời gian", "Trạng thái"])
        layout.addWidget(self.table)

        self.setLayout(layout)