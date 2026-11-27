
import bcrypt
import sqlite3

def generate_hash(password):
    """Turn a password into a bcrypt hash (returned as text)."""
    byte_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte_password, salt)
    return hashed.decode("utf-8")

def is_valid_hash(password, hashed):
    """True if the password matches the stored hash."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def add_user_to_db(conn, username, hash):
    curr = conn.cursor()
    curr.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hash))
    conn.commit()
    print(f"User {username} added to database.")

def register_user(conn, username, password):
    hash = generate_hash(password)
    add_user_to_db(conn, username, hash)
    return True, "Registered. You can login now."

def get_user_from_db(conn, username):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users WHERE username = ?", (username,))
    return curr.fetchone()

def login_user(conn, username, password):
    """Check a username and password. Returns (True or False, a message)."""
    _, user_name, user_hash = get_user_from_db(conn, username)
    if user_name is not None and is_valid_hash(password, user_hash):
        return True, "Welcome back!"
    return False, "Incorrect username or password"