from config import get_db_connection
from datetime import datetime

class AppointmentModel:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT a.*, c.name as customer_name, v.license_plate, s.name as service_name
            FROM appointments a
            JOIN customers c ON a.customer_id = c.id
            JOIN vehicles v ON a.vehicle_id = v.id
            JOIN services s ON a.service_id = s.id
            ORDER BY a.appointment_date DESC
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    def add(self, customer_id: int, vehicle_id: int, service_id: int, appointment_date: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (customer_id, vehicle_id, service_id, appointment_date) 
            VALUES (%s, %s, %s, %s)
        """, (customer_id, vehicle_id, service_id, appointment_date))
        conn.commit()
        conn.close()

    def update_status(self, aid: int, status: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE appointments SET status = %s WHERE id = %s", (status, aid))
        conn.commit()
        conn.close()

    def delete(self, aid: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM appointments WHERE id = %s", (aid,))
        conn.close()