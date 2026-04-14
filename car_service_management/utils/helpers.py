import hashlib
from datetime import datetime

def hash_password(password: str) -> str:
    """Mã hóa mật khẩu bằng SHA256"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def format_currency(amount) -> str:
    """Định dạng tiền Việt Nam"""
    try:
        return f"{int(float(amount)):,} VNĐ"
    except:
        return "0 VNĐ"

def get_current_datetime():
    """Lấy thời gian hiện tại"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")