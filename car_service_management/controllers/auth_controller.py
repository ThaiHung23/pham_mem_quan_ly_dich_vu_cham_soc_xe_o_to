from models.user import UserModel
from views.dashboard_window import DashboardWindow
from PyQt6.QtWidgets import QMessageBox

class AuthController:
    def __init__(self, login_view):
        self.login_view = login_view
        self.model = UserModel()

    def login(self):
        username = self.login_view.username.text().strip()
        password = self.login_view.password.text().strip()

        if not username or not password:
            QMessageBox.warning(self.login_view, "Lỗi", "Vui lòng nhập đầy đủ!")
            return

        user = self.model.login(username, password)
        if user:
            self.login_view.close()
            try:
                self.dashboard = DashboardWindow(user)
                self.dashboard.show()
            except Exception as e:
                QMessageBox.critical(self.login_view, "Lỗi", f"Lỗi khi mở Dashboard:\n{str(e)}")
        else:
            QMessageBox.critical(self.login_view, "Thất bại", 
                               "Sai tài khoản hoặc mật khẩu!\n\nThử: admin / admin123")