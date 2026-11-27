
from pathlib import Path

from app_model.db import connect_db
from app_model.users import login_user


if __name__ == "__main__":
    conn = connect_db()
    
