import sqlite3
import os

# Hardcoded credentials (Secret Detection Vulnerability)
DB_PASSWORD = "SuperSecret123"

def connect_to_db():
    # SQL Injection Vulnerability
    user_input = input("Enter the username to fetch data: ")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)  # Vulnerable to SQL Injection
    results = cursor.fetchall()
    print("Results:", results)
    conn.close()

def insecure_file_access():
    # Insecure File Access Vulnerability
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        print(file.read())

if __name__ == "__main__":
    connect_to_db()
    insecure_file_access()

    