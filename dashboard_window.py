from PyQt6.QtWidgets import (QMainWindow, QTabWidget, QWidget, QVBoxLayout, 
                           QLabel, QPushButton, QHBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# Import các window (sẽ import sau khi định nghĩa class)
from views.customer_window import CustomerWindow
from views.vehicle_window import VehicleWindow
from views.service_window import ServiceWindow
from views.appointment_window import AppointmentWindow
from views.invoice_window import InvoiceWindow

class DashboardWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        
        try:
            self.setWindowTitle(f"Dashboard - {user.get('full_name', user.get('username', 'User'))}")
            self.resize(1250, 720)
            
            # Tạo tab widget
            self.tabs = QTabWidget()
            self.setCentralWidget(self.tabs)

            # Thêm các tab
            self.tabs.addTab(CustomerWindow(), "👥 Khách Hàng")
            self.tabs.addTab(VehicleWindow(), "🚗 Xe")
            self.tabs.addTab(ServiceWindow(), "🛠 Dịch Vụ")
            self.tabs.addTab(AppointmentWindow(), "📅 Lịch Hẹn")
            self.tabs.addTab(InvoiceWindow(), "💰 Hóa Đơn")

            # Status bar
            self.statusBar().showMessage(f"Đăng nhập thành công | Vai trò: {user.get('role', 'staff')}")
            
            print("✅ Dashboard loaded successfully!")   # Debug

        except Exception as e:
            QMessageBox.critical(self, "Lỗi Dashboard", f"Có lỗi khi mở giao diện chính:\n{str(e)}")
            self.close()