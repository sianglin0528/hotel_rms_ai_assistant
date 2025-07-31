# etl_pipeline.py
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random

DB_PATH = "data/hotel_data.db"

def generate_new_data():
    today = datetime.today().date()
    occupancy = round(random.uniform(0.5, 0.9), 2)
    price = random.randint(100, 150)
    source = random.choice(["OTA", "Direct"])
    return pd.DataFrame([[today, occupancy, price, source]], 
                        columns=["date", "occupancy_rate", "avg_price", "booking_source"])

def update_database():
    conn = sqlite3.connect(DB_PATH)
    # 如果沒有資料就用 sample_data 初始化
    try:
        existing = pd.read_sql("SELECT * FROM hotel_data", conn)
    except:
        df = pd.read_csv("data/sample_data.csv")
        df.to_sql("hotel_data", conn, if_exists="replace", index=False)
        existing = df

    # 新增今天的模擬資料
    new_df = generate_new_data()
    new_df.to_sql("hotel_data", conn, if_exists="append", index=False)
    conn.close()
    print(f"✅ 新增資料：{new_df.values.tolist()}")

if __name__ == "__main__":
    update_database()
