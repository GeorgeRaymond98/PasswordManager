import getpass
import hashlib

# Dictionary to store username-password pairs
password_manager = {}

# Function to create an account
def create_account():
    username = input("Please enter your username: ")
    # Check if the username already exists
    if username in password_manager:
        print("Username already exists. Please choose a different username.")
        return
    password = getpass.getpass("Please enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Your account was created successfully!")

# Function to login
def login():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Check if the username exists and password matches
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Main function to drive the scripts
def main():
    while True:
        choice = input("Please enter 1 to create an account, 2 to login, or 3 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
