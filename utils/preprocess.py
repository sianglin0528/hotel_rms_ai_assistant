# utils/preprocess.py
import pandas as pd
import sqlite3

def load_and_process_data():
    conn = sqlite3.connect("data/hotel_data.db")
    df = pd.read_sql("SELECT * FROM hotel_data ORDER BY date", conn)
    conn.close()
    
    # Prophet 專用格式
    df['date'] = pd.to_datetime(df['date'])
    prophet_df = df[['date', 'occupancy_rate']].rename(columns={'date':'ds','occupancy_rate':'y'})
    return df, prophet_df
