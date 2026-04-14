from models.service import ServiceModel
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

class ServiceController:
    def __init__(self, view):
        self.view = view
        self.model = ServiceModel()
        self.load_data()

    def load_data(self):
        data = self.model.get_all()
        self.view.table.setRowCount(len(data))
        for row, s in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(s['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(s['name']))
            self.view.table.setItem(row, 2, QTableWidgetItem(f"{float(s['price']):,.0f}"))
            self.view.table.setItem(row, 3, QTableWidgetItem(s.get('description', '')))

    def add_service(self):
        name = self.view.txt_name.text().strip()
        try:
            price = float(self.view.txt_price.text().strip())
        except:
            QMessageBox.warning(self.view, "Lỗi", "Giá phải là số!")
            return
        desc = self.view.txt_desc.toPlainText().strip()

        if not name or price <= 0:
            QMessageBox.warning(self.view, "Lỗi", "Tên dịch vụ và giá không hợp lệ!")
            return

        self.model.add(name, price, desc)
        QMessageBox.information(self.view, "Thành công", "Thêm dịch vụ thành công!")
        self.clear_form()
        self.load_data()

    def update_service(self):
        row = self.view.table.currentRow()
        if row < 0:
            QMessageBox.warning(self.view, "Chưa chọn", "Vui lòng chọn dịch vụ!")
            return
        sid = int(self.view.table.item(row, 0).text())
        name = self.view.txt_name.text().strip()
        price = float(self.view.txt_price.text())
        desc = self.view.txt_desc.toPlainText().strip()

        self.model.update(sid, name, price, desc)
        QMessageBox.information(self.view, "Thành công", "Cập nhật thành công!")
        self.load_data()

    def delete_service(self):
        row = self.view.table.currentRow()
        if row < 0:
            return
        sid = int(self.view.table.item(row, 0).text())
        self.model.delete(sid)
        self.load_data()

    def clear_form(self):
        self.view.txt_name.clear()
        self.view.txt_price.clear()
        self.view.txt_desc.clear()