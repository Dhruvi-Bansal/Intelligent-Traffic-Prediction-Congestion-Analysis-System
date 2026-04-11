from src.db.db_connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic_data (
        datetime TEXT,
        traffic_volume INTEGER,
        temperature REAL,
        hour INTEGER,
        day INTEGER,
        month INTEGER
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()