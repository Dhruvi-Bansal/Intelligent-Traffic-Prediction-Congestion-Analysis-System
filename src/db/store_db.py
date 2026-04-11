import pandas as pd
from src.db.db_connection import get_connection

def store_to_db():
    df = pd.read_csv("../../data/processed/cleaned_data.csv")
    print("Rows in CSV:", len(df))
    conn = get_connection()

    df.to_sql("traffic_data", conn, if_exists="replace", index=False)

    conn.close()
    print("Data stored!")

if __name__ == "__main__":
    store_to_db()