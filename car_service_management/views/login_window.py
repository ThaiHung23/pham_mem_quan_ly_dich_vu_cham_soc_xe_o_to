from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, 
                           QPushButton, QMessageBox, QHBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from controllers.auth_controller import AuthController

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng Nhập - Quản Lý Chăm Sóc Xe Ô Tô")
        self.setFixedSize(420, 340)
        self.setStyleSheet("background-color: #f0f0f0;")

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Title
        title = QLabel("🚗 QUẢN LÝ CHĂM SÓC XE")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        layout.addSpacing(20)

        # Form
        self.username = QLineEdit()
        self.username.setPlaceholderText("Tên đăng nhập")
        self.username.setFixedHeight(40)

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Mật khẩu")
        self.password.setFixedHeight(40)

        layout.addWidget(QLabel("Tên đăng nhập:"))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("Mật khẩu:"))
        layout.addWidget(self.password)

        # Button
        self.btn_login = QPushButton("ĐĂNG NHẬP")
        self.btn_login.setFixedHeight(45)
        self.btn_login.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: #0078d4; 
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)

        layout.addWidget(self.btn_login)
        layout.addSpacing(10)

        self.setLayout(layout)

        # ==================== QUAN TRỌNG ====================
        # Kết nối nút bấm với Controller
        self.controller = AuthController(self)
        self.btn_login.clicked.connect(self.controller.login)
        # ===================================================