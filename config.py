import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Kết nối database MySQL (XAMPP)"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",           
            password="",         
            database="car_service_db",
            charset="utf8mb4",
            collation="utf8mb4_unicode_ci"
        )
        return conn
    except Error as e:
        print(f"Lỗi kết nối MySQL: {e}")
        return None