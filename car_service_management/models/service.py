from config import get_db_connection

class ServiceModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services ORDER BY id DESC")
        data = cursor.fetchall()
        conn.close()
        return data

    def add(self, name: str, price: float, description: str = ""):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO services (name, price, description) 
            VALUES (%s, %s, %s)
        """, (name, price, description))
        conn.commit()
        conn.close()

    def update(self, sid: int, name: str, price: float, description: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE services 
            SET name = %s, price = %s, description = %s 
            WHERE id = %s
        """, (name, price, description, sid))
        conn.commit()
        conn.close()

    def delete(self, sid: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM services WHERE id = %s", (sid,))
        conn.commit()
        conn.close()