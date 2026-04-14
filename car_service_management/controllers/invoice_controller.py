from models.invoice import InvoiceModel
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from utils.helpers import format_currency

class InvoiceController:
    def __init__(self, view):
        self.view = view
        self.model = InvoiceModel()
        self.load_data()

    def load_data(self):
        data = self.model.get_all()
        self.view.table.setRowCount(len(data))
        for row, inv in enumerate(data):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(inv['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(inv['customer_name']))
            self.view.table.setItem(row, 2, QTableWidgetItem(format_currency(inv['total_amount'])))
            self.view.table.setItem(row, 3, QTableWidgetItem(inv['payment_status']))
            self.view.table.setItem(row, 4, QTableWidgetItem(str(inv['created_at'])))

    def mark_as_paid(self):
        row = self.view.table.currentRow()
        if row < 0:
            return
        iid = int(self.view.table.item(row, 0).text())
        self.model.update_payment(iid, "paid")
        QMessageBox.information(self.view, "Thành công", "Đã thanh toán!")
        self.load_data()