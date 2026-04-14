from models.customer import CustomerModel
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

class CustomerController:
    def __init__(self, view):
        self.view = view
        self.model = CustomerModel()
        self.load_data()

    def load_data(self):
        data = self.model.get_all()
        self.view.table.setRowCount(len(data))
        for row, c in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(c['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(c['name']))
            self.view.table.setItem(row, 2, QTableWidgetItem(c['phone'] or ""))
            self.view.table.setItem(row, 3, QTableWidgetItem(c['address'] or ""))

    def add_customer(self):
        name = self.view.txt_name.text().strip()
        phone = self.view.txt_phone.text().strip()
        address = self.view.txt_address.toPlainText().strip()

        if not name or not phone:
            QMessageBox.warning(self.view, "Lỗi", "Tên và Số điện thoại không được để trống!")
            return

        try:
            self.model.add(name, phone, address)
            QMessageBox.information(self.view, "Thành công", "Thêm khách hàng thành công!")
            self.clear_form()
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self.view, "Lỗi", f"Không thể thêm: {str(e)}")

    def update_customer(self):
        row = self.view.table.currentRow()
        if row < 0:
            QMessageBox.warning(self.view, "Chưa chọn", "Vui lòng chọn khách hàng để sửa!")
            return

        try:
            cid = int(self.view.table.item(row, 0).text())
            name = self.view.txt_name.text().strip()
            phone = self.view.txt_phone.text().strip()
            address = self.view.txt_address.toPlainText().strip()

            self.model.update(cid, name, phone, address)
            QMessageBox.information(self.view, "Thành công", "Cập nhật khách hàng thành công!")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self.view, "Lỗi", str(e))

    def delete_customer(self):
        row = self.view.table.currentRow()
        if row < 0:
            QMessageBox.warning(self.view, "Chưa chọn", "Vui lòng chọn khách hàng để xóa!")
            return

        reply = QMessageBox.question(self.view, "Xác nhận xóa", 
                                     "Bạn có chắc chắn muốn xóa khách hàng này?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            cid = int(self.view.table.item(row, 0).text())
            self.model.delete(cid)
            QMessageBox.information(self.view, "Thành công", "Đã xóa khách hàng!")
            self.load_data()
            self.clear_form()

    def search_customer(self):
        keyword = self.view.txt_search.text().strip()
        if not keyword:
            self.load_data()
            return

        data = self.model.search(keyword)
        self.view.table.setRowCount(len(data))
        for row, c in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(c['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(c['name']))
            self.view.table.setItem(row, 2, QTableWidgetItem(c['phone'] or ""))
            self.view.table.setItem(row, 3, QTableWidgetItem(c['address'] or ""))

    def clear_form(self):
        self.view.txt_name.clear()
        self.view.txt_phone.clear()
        self.view.txt_address.clear()
        self.view.txt_search.clear()