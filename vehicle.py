from config import get_db_connection

class VehicleModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.*, c.name as customer_name 
            FROM vehicles v
            LEFT JOIN customers c ON v.customer_id = c.id
            ORDER BY v.id DESC
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    def get_by_customer(self, customer_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vehicles WHERE customer_id = %s", (customer_id,))
        data = cursor.fetchall()
        conn.close()
        return data

    def add(self, license_plate: str, brand: str, model: str, customer_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO vehicles (license_plate, brand, model, customer_id) 
            VALUES (%s, %s, %s, %s)
        """, (license_plate, brand, model, customer_id))
        conn.commit()
        conn.close()

    def update(self, vid: int, license_plate: str, brand: str, model: str, customer_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE vehicles 
            SET license_plate = %s, brand = %s, model = %s, customer_id = %s 
            WHERE id = %s
        """, (license_plate, brand, model, customer_id, vid))
        conn.commit()
        conn.close()

    def delete(self, vid: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vehicles WHERE id = %s", (vid,))
        conn.commit()
        conn.close()