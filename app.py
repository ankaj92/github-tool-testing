import sqlite3
import os

# ----------------------------------------
# ✅ GOOD PRACTICE (Using Environment Variable)
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_password")

def connect_to_db():
    # ✅ Mitigated SQL Injection Vulnerability
    user_input = input("Enter the username to fetch data: ")

    # Use parameterized queries
    query = "SELECT * FROM users WHERE username = ?"

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query, (user_input,))  # Secure
    results = cursor.fetchall()
    print("Results:", results)
    conn.close()


def insecure_file_access():
    # ✅ Secure File Access
    filename = input("Enter the filename to read: ")

    if not os.path.exists(filename):
        print("Error: File does not exist.")
        return

    allowed_directory = os.path.abspath("allowed_files")
    filepath = os.path.abspath(filename)

    if not filepath.startswith(allowed_directory):
        print("Error: Access to this file is not allowed.")
        return

    with open(filepath, "r") as file:
        print(file.read())


# ----------------------------------------
# ⚠️ INTENTIONAL VULNERABILITIES FOR TESTING


# 🚨 Secret Scanning Test (hardcoded token)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"  # Fake AWS Key
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrs"  # Fake GitHub Token

def vulnerable_sql():
    # 🚨 SQL Injection Vulnerability (for CodeQL)
    user_input = input("Enter username (vulnerable): ")
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # 🚨 Vulnerable
    cursor.execute(query)
    results = cursor.fetchall()
    print("Results (vulnerable):", results)
    conn.close()


def vulnerable_file_access():
    # 🚨 Path Traversal Vulnerability (for CodeQL)
    filename = input("Enter any filename: ")
    with open(filename, "r") as file:  # 🚨 No checks
        print(file.read())


# ----------------------------------------
# 🔽 Entry point
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Secure DB Query")
    print("2. Secure File Access")
    print("3. Vulnerable SQL (for CodeQL test)")
    print("4. Vulnerable File Access (for CodeQL test)")

    choice = input("Enter choice: ")

    if choice == "1":
        connect_to_db()
    elif choice == "2":
        insecure_file_access()
    elif choice == "3":
        vulnerable_sql()
    elif choice == "4":
        vulnerable_file_access()
    else:
        print("Invalid choice.")
