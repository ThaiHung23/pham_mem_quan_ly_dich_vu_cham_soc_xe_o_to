import sys
from PyQt6.QtWidgets import QApplication
from views.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)
    
    # Thiết lập style chung cho toàn bộ ứng dụng
    app.setStyle("Fusion")
    
    # Khởi tạo cửa sổ đăng nhập
    login_window = LoginWindow()
    
    # Kết nối nút Đăng nhập với controller (đã làm trong LoginWindow)
    login_window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()