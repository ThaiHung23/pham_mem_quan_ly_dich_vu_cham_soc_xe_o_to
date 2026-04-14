from models.appointment import AppointmentModel
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from datetime import datetime

class AppointmentController:
    def __init__(self, view):
        self.view = view
        self.model = AppointmentModel()
        self.load_data()

    def load_data(self):
        data = self.model.get_all()
        self.view.table.setRowCount(len(data))
        for row, a in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(a['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(a['customer_name']))
            self.view.table.setItem(row, 2, QTableWidgetItem(a['license_plate']))
            self.view.table.setItem(row, 3, QTableWidgetItem(a['service_name']))
            self.view.table.setItem(row, 4, QTableWidgetItem(str(a['appointment_date'])))
            self.view.table.setItem(row, 5, QTableWidgetItem(a['status']))

    def add_appointment(self):
        customer_id = self.view.cmb_customer.currentData()
        vehicle_id = self.view.cmb_vehicle.currentData()
        service_id = self.view.cmb_service.currentData()
        date_str = self.view.date_appointment.text()

        if not all([customer_id, vehicle_id, service_id]):
            QMessageBox.warning(self.view, "Lỗi", "Vui lòng chọn đầy đủ thông tin!")
            return

        try:
            self.model.add(customer_id, vehicle_id, service_id, date_str)
            QMessageBox.information(self.view, "Thành công", "Đặt lịch thành công!")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self.view, "Lỗi", str(e))