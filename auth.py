from pathlib import Path

import bcrypt

USERS_FILE = Path(__file__).parent / "DATA" / "users.txt"

def generate_hash(password):
    """Turn a password into a bcrypt hash (returned as text)."""
    byte_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte_password, salt)
    return hashed.decode("utf-8")

def is_valid_hash(password, hashed):
    """True if the password matches the stored hash."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

def register_user(username, password):
    """Add a new user. Returns (True or False, a message)."""
    hash = generate_hash(password)
    with open(USERS_FILE, "a") as file:
        file.write(f"{username},{hash}\n")
    print(f"User {username} registered successfully.")

def login_user(username, password):
    """Check a username and password. Returns (True or False, a message)."""
    with open(USERS_FILE, "r") as f:
        for line in f:
            user, hash = line.strip().split(",")
            if user == username:
                if is_valid_hash(password, hash):
                    print(f"User {username} logged in successfully.")
                    return
                else:
                    print("Incorrect password")


if __name__ == "__main__":
    while True:
        choice = input("Enter (1) to Register: or (2) to Login: (3 to Exit) ")
        if choice == "1":
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(user_name, password)
            pass
        elif choice == "2":
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            login_user(user_name, password)
            pass
        elif choice == "3":
            print("Exiting the program.")
            break

