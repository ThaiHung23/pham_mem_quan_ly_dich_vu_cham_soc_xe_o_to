from models.vehicle import VehicleModel
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

class VehicleController:
    def __init__(self, view):
        self.view = view
        self.model = VehicleModel()
        self.load_data()

    def load_data(self):
        data = self.model.get_all()
        self.view.table.setRowCount(len(data))
        for row, v in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(v['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(v['license_plate']))
            self.view.table.setItem(row, 2, QTableWidgetItem(v['brand'] or ""))
            self.view.table.setItem(row, 3, QTableWidgetItem(v['model'] or ""))
            self.view.table.setItem(row, 4, QTableWidgetItem(v.get('customer_name', '')))

    def add_vehicle(self):
        plate = self.view.txt_plate.text().strip()
        brand = self.view.txt_brand.text().strip()
        model = self.view.txt_model.text().strip()
        customer_id = self.view.cmb_customer.currentData()

        if not plate or not customer_id:
            QMessageBox.warning(self.view, "Lỗi", "Biển số và Khách hàng là bắt buộc!")
            return

        try:
            self.model.add(plate, brand, model, customer_id)
            QMessageBox.information(self.view, "Thành công", "Thêm xe thành công!")
            self.clear_form()
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self.view, "Lỗi", str(e))

    def update_vehicle(self):
        row = self.view.table.currentRow()
        if row < 0:
            QMessageBox.warning(self.view, "Chưa chọn", "Vui lòng chọn xe để sửa!")
            return
        vid = int(self.view.table.item(row, 0).text())
        plate = self.view.txt_plate.text().strip()
        brand = self.view.txt_brand.text().strip()
        model = self.view.txt_model.text().strip()
        customer_id = self.view.cmb_customer.currentData()

        try:
            self.model.update(vid, plate, brand, model, customer_id)
            QMessageBox.information(self.view, "Thành công", "Cập nhật xe thành công!")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self.view, "Lỗi", str(e))

    def delete_vehicle(self):
        row = self.view.table.currentRow()
        if row < 0:
            QMessageBox.warning(self.view, "Chưa chọn", "Vui lòng chọn xe để xóa!")
            return

        reply = QMessageBox.question(self.view, "Xác nhận", "Xóa xe này?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            vid = int(self.view.table.item(row, 0).text())
            self.model.delete(vid)
            QMessageBox.information(self.view, "Thành công", "Đã xóa xe!")
            self.load_data()
            self.clear_form()

    def clear_form(self):
        self.view.txt_plate.clear()
        self.view.txt_brand.clear()
        self.view.txt_model.clear()