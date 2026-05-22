from cryptography.fernet import Fernet
import base64
import hashlib
import os

def generate_key(password):

    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

def encrypt_file(file_path, password):

    key = generate_key(password)

    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    encrypted_path = "encrypted/" + os.path.basename(file_path) + ".enc"

    with open(encrypted_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return encrypted_path

def decrypt_file(file_path, password):

    key = generate_key(password)

    fernet = Fernet(key)

    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    original_name = os.path.basename(file_path).replace(".enc", "")

    decrypted_path = "decrypted/" + original_name

    with open(decrypted_path, 'wb') as dec_file:
        dec_file.write(decrypted)

    return decrypted_path
