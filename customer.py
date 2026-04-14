from config import get_db_connection

class CustomerModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers ORDER BY id DESC")
        data = cursor.fetchall()
        conn.close()
        return data

    def get_by_id(self, cid: int):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers WHERE id = %s", (cid,))
        data = cursor.fetchone()
        conn.close()
        return data

    def add(self, name: str, phone: str, address: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO customers (name, phone, address) 
            VALUES (%s, %s, %s)
        """, (name, phone, address))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, cid: int, name: str, phone: str, address: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE customers 
            SET name = %s, phone = %s, address = %s 
            WHERE id = %s
        """, (name, phone, address, cid))
        conn.commit()
        conn.close()

    def delete(self, cid: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id = %s", (cid,))
        conn.commit()
        conn.close()

    def search(self, keyword: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM customers 
            WHERE name LIKE %s OR phone LIKE %s 
            ORDER BY id DESC
        """, (f"%{keyword}%", f"%{keyword}%"))
        data = cursor.fetchall()
        conn.close()
        return data