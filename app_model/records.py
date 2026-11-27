
import pandas as pd

def load_csv(conn, csv_path):
    df = pd.read_csv(csv_path)
    df.to_sql("records", conn, if_exists="replace", index=False)
    print(f"Loaded {len(df)} records from {csv_path} into the database.")

def read_all_data(conn):
    df = pd.read_sql("SELECT * FROM records", conn)
    return df