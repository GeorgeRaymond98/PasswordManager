# 🔐 Simple Python Password Manager

This Python script provides a basic username and password management system using secure SHA-256 hashing. It allows users to create accounts and log in, ensuring that passwords are stored securely.

## 🚀 Features

- **Account Creation:** Users can create accounts with unique usernames and securely hashed passwords.
- **Secure Password Handling:** Passwords are hashed using SHA-256 before storage, ensuring that plaintext passwords are never saved.
- **Login Verification:** Users can log in by providing their username and password, which are verified against the stored hashed password.
- **User-Friendly Interface:** Simple command-line interface to create accounts, log in, and exit the program.

## 📄 Requirements

- Python 3.x

## 🛠️ Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/python-password-manager.git
    cd python-password-manager
    ```

2. Run the script:
    ```bash
    python password_manager.py
    ```

3. Follow the prompts to create an account, log in, or exit the program.

## 📝 Example Interaction

Here's an example of how the program works:


## 🧩 How It Works

1. **Account Creation:**
    - The user is prompted to enter a username and password.
    - If the username is unique, the password is hashed using SHA-256 and stored.
    - If the username already exists, the user is asked to choose a different one.

2. **Login:**
    - The user provides their username and password.
    - The entered password is hashed and compared with the stored hash.
    - If the username exists and the hashed password matches, the login is successful; otherwise, an error message is displayed.

3. **Main Menu:**
    - The main loop presents options to create an account, log in, or exit.

## 🔒 Security Notes

- Passwords are never stored in plaintext; they are securely hashed using SHA-256.
- This script uses an in-memory dictionary to store usernames and hashed passwords, meaning all data is lost when the program ends. For persistent storage, consider using a database or file system.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/python-password-manager/issues) or submit a pull request.

---

Made with ❤️ by [George Raymond]([https://github.com/your-username](https://github.com/GeorgeRaymond98))
