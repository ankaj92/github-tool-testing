# Python Vulnerable Application

This repository contains a deliberately vulnerable Python application designed for testing GitHub Advanced Security (GHAS) features. The application includes common vulnerabilities such as SQL Injection, Insecure File Access, and Hardcoded Secrets. The purpose of this repository is to demonstrate how to enable and interpret security scans using GitHub's security tools.

---

## Vulnerabilities in the Application

### 1. **SQL Injection**

- **Location**: `connect_to_db()` function in `app.py`
- **Description**: The application constructs SQL queries using unsanitized user input, making it vulnerable to SQL Injection attacks.
- **Impact**: An attacker can execute arbitrary SQL commands, potentially exposing or modifying sensitive data.

### 2. **Insecure File Access**

- **Location**: `insecure_file_access()` function in `app.py`
- **Description**: The application allows users to specify filenames without validation, enabling unauthorized access to sensitive files.
- **Impact**: An attacker can read arbitrary files on the system.

### 3. **Hardcoded Secrets**

- **Location**: `DB_PASSWORD` in `app.py`
- **Description**: The application stores sensitive credentials directly in the source code.
- **Impact**: Hardcoded secrets can be easily exposed, leading to unauthorized access to databases or other services.

---

## Scans to Perform

### 1. **Code Scanning**

- **Tool**: CodeQL
- **Purpose**: Detect vulnerabilities in the source code, such as SQL Injection and Insecure File Access.
- **How to Interpret**:
  - Navigate to the **Security > Code scanning alerts** tab in the GitHub repository.
  - Review the alerts for vulnerabilities, including their severity and location in the code.

### 2. **Dependency Scanning**

- **Tool**: Dependabot
- **Purpose**: Identify outdated or vulnerable dependencies in the project.
- **How to Interpret**:
  - Navigate to the **Security > Dependabot alerts** tab in the GitHub repository.
  - Review the list of vulnerable dependencies and their suggested updates.

### 3. **Secret Detection**

- **Tool**: GitHub Secret Scanning
- **Purpose**: Detect hardcoded secrets in the source code.
- **How to Interpret**:
  - Navigate to the **Security > Secret scanning alerts** tab in the GitHub repository.
  - Review the detected secrets and take action to secure them.

### 4. **Security Alerts**

- **Tool**: GitHub Security Advisories
- **Purpose**: Monitor and manage vulnerabilities in the repository.
- **How to Interpret**:
  - Navigate to the **Security > Security advisories** tab in the GitHub repository.
  - Review advisories for vulnerabilities and their resolutions.

---

## How to Run the Scans

### 1. **Code Scanning**

- Ensure the `CodeQL` workflow is enabled in `.github/workflows/`.
- Push the code to the repository to trigger the scan.
- View results in the **Security > Code scanning alerts** tab.

### 2. **Dependency Scanning**

- Enable Dependabot alerts in the repository settings.
- Dependabot will automatically scan for vulnerable dependencies.
- View results in the **Security > Dependabot alerts** tab.

### 3. **Secret Detection**

- Enable Secret Scanning in the repository settings.
- Push the code to trigger the scan.
- View results in the **Security > Secret scanning alerts** tab.

### 4. **Security Alerts**

- Enable Security Advisories in the repository settings.
- Monitor the **Security > Security advisories** tab for alerts.

---

## Summary of Results

| Vulnerability Type   | Severity | Location in Code         | Suggested Mitigation                            |
| -------------------- | -------- | ------------------------ | ----------------------------------------------- |
| SQL Injection        | Critical | `connect_to_db()`        | Use parameterized queries to sanitize input.    |
| Insecure File Access | High     | `insecure_file_access()` | Validate and sanitize user input.               |
| Hardcoded Secrets    | High     | `DB_PASSWORD`            | Use environment variables or a secrets manager. |

---

## How to Mitigate Vulnerabilities

### 1. **SQL Injection**

- Replace the vulnerable query with a parameterized query:
  ```python
  query = "SELECT * FROM users WHERE username = ?"
  cursor.execute(query, (user_input,))
  ```

### 2. **Insecure File Access**

- Validate the filename before accessing it:
  ```python
  if not os.path.exists(filename):
      print("File does not exist.")
      return
  ```

### 3. **Hardcoded Secrets**

- Use environment variables to store sensitive information:
  ```python
  DB_PASSWORD = os.getenv("DB_PASSWORD")
  ```

---

## Additional Notes

- This repository is for educational purposes only. Do not deploy this application in a production environment.
- Always follow secure coding practices and regularly scan your codebase for vulnerabilities.

---

Let me know if you need further assistance!
