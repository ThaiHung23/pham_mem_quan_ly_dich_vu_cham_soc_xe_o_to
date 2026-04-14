from config import get_db_connection
from utils.helpers import hash_password

class UserModel:
    def login(self, username: str, password: str):
        conn = get_db_connection()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        hashed = hash_password(password)
        cursor.execute("""
            SELECT id, username, role, full_name 
            FROM users 
            WHERE username = %s AND password = %s
        """, (username, hashed))
        user = cursor.fetchone()
        conn.close()
        return user

    def change_password(self, user_id: int, new_password: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        hashed = hash_password(new_password)
        cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed, user_id))
        conn.commit()
        conn.close()