from src.db.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM traffic_data")
print(cursor.fetchone())

cursor.execute("SELECT * FROM traffic_data LIMIT 5;")
print(cursor.fetchone())

cursor.execute("SELECT * FROM traffic_data WHERE hour = 8 LIMIT 10;")
print(cursor.fetchone())

cursor.execute("SELECT holiday, AVG(traffic_volume) FROM traffic_data GROUP BY holiday;")
print(cursor.fetchone())

conn.close()