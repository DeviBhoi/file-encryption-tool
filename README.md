# SecureVault File Encryption Tool

## Project Overview

SecureVault is a Python-based web application that enables users to securely encrypt and decrypt files using password-derived symmetric encryption. It provides a clean Flask interface for uploading files, entering a password, and downloading the resulting encrypted or decrypted output.

## Features

- Secure file encryption and decryption
- Password-based key derivation using SHA-256 and Fernet
- Web interface built with Flask
- Supports common file types such as DOCX, PDF, JPG, PNG, and more
- Automatic storage of temporary uploads in `uploads/`
- Outputs encrypted files into `encrypted/` and decrypted files into `decrypted/`
- User-friendly forms for encrypting and decrypting files

## Technologies Used

- Python
- Flask
- cryptography (Fernet)
- HTML/CSS/JavaScript
- Jinja2 templating

## Installation Guide

1. Clone or download the repository.
2. Navigate to the project folder:

```bash
cd c:\Users\sunit\OneDrive\Desktop\file-encryption-tool
```

3. Create and activate a Python virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Project

1. Ensure you are in the project directory.
2. Start the Flask application:

```bash
python app.py
```

3. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

4. Use the web interface to upload a file, enter a password, and encrypt or decrypt the file.

## Folder Structure

```text
file-encryption-tool/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates for the web app
│   ├── index.html
│   └── error.html
├── static/                # Static assets for styling and scripts
│   ├── style.css
│   ├── script.js
│   └── error.css
├── utils/                 # Utility functions for encryption and decryption
│   └── crypto_utils.py
├── uploads/               # Temporary uploaded files
├── encrypted/             # Encrypted output files
└── decrypted/             # Decrypted output files
```

## Encryption and Decryption Workflow

### Encryption

1. User uploads a file through the web interface.
2. User enters a password and submits the form.
3. The application saves the uploaded file into `uploads/`.
4. `utils/crypto_utils.py` derives a 32-byte key from the password using SHA-256.
5. Fernet encryption is applied to the file contents.
6. The encrypted file is written to `encrypted/` with a `.enc` extension.
7. The encrypted file is returned to the user as a download.

### Decryption

1. User uploads an encrypted `.enc` file through the web interface.
2. User enters the password used during encryption.
3. The application saves the uploaded encrypted file into `uploads/`.
4. `utils/crypto_utils.py` derives the same key from the password.
5. Fernet decrypts the uploaded file contents.
6. The decrypted file is written to `decrypted/` with its original name.
7. The decrypted file is returned to the user as a download.

## Screenshots

> Add screenshots here once available.

You can include sample images of the interface and workflow such as:

- `screenshots/home.png`
- `screenshots/encrypt-form.png`
- `screenshots/decrypt-form.png`

## Future Improvements

- Add stronger password validation and password strength feedback
- Provide user session management and file cleanup policies
- Add support for bulk encryption/decryption of multiple files
- Improve error handling and show detailed user messages
- Add secure file storage and automatic cleanup of temporary uploads
- Add support for file preview and progress indicators

## Author Information

- Author: Your Name
- Project: SecureVault File Encryption Tool
- Location: c:\Users\sunit\OneDrive\Desktop\file-encryption-tool

```