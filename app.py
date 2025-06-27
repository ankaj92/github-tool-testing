import sqlite3
import os

# Use environment variables for sensitive credentials
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_password")

def connect_to_db():
    # Mitigated SQL Injection Vulnerability
    user_input = input("Enter the username to fetch data: ")
    
    # Use parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query, (user_input,))  # Parameterized query
    results = cursor.fetchall()
    print("Results:", results)
    conn.close()

def insecure_file_access():
    # Mitigated Insecure File Access Vulnerability
    filename = input("Enter the filename to read: ")
    
    # Validate and sanitize user input
    if not os.path.exists(filename):
        print("Error: File does not exist.")
        return

    # Restrict access to specific directories
    allowed_directory = os.path.abspath("allowed_files")
    filepath = os.path.abspath(filename)

    if not filepath.startswith(allowed_directory):
        print("Error: Access to this file is not allowed.")
        return

    with open(filepath, "r") as file:
        print(file.read())

if __name__ == "__main__":
    connect_to_db()
    insecure_file_access()