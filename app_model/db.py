
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent.parent / "DATA" / "app.db"

def connect_db(db_file=DB_FILE):
    """Connects to SQL database"""
    conn = sqlite3.connect(db_file)
    return conn