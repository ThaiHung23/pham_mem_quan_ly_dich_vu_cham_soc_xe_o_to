from config import get_db_connection

class InvoiceModel:
    def create(self, appointment_id: int, total_amount: float):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO invoices (appointment_id, total_amount) 
            VALUES (%s, %s)
        """, (appointment_id, total_amount))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT i.*, a.appointment_date, c.name as customer_name, v.license_plate
            FROM invoices i
            JOIN appointments a ON i.appointment_id = a.id
            JOIN customers c ON a.customer_id = c.id
            JOIN vehicles v ON a.vehicle_id = v.id
            ORDER BY i.created_at DESC
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    def update_payment(self, iid: int, status: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE invoices SET payment_status = %s WHERE id = %s", (status, iid))
        conn.commit()
        conn.close()