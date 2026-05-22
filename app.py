from flask import Flask, render_template, request, send_file, redirect, url_for
import os

from utils.crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('encrypted', exist_ok=True)
os.makedirs('decrypted', exist_ok=True)

# HOME PAGE

@app.route('/')
def home():

    success = request.args.get('success')

    return render_template(
        'index.html',
        success=success
    )

# ENCRYPT

@app.route('/encrypt', methods=['POST'])
def encrypt():

    file = request.files['file']

    password = request.form['password']

    if file.filename == '':
        return redirect(url_for('home'))

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(file_path)

    encrypted_path = encrypt_file(
        file_path,
        password
    )

    return send_file(
        encrypted_path,
        as_attachment=True
    )

# DECRYPT

@app.route('/decrypt', methods=['POST'])
def decrypt():

    file = request.files['file']

    password = request.form['password']

    if file.filename == '':
        return redirect(url_for('home'))

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(file_path)

    try:

        decrypted_path = decrypt_file(
            file_path,
            password
        )

        return send_file(
            decrypted_path,
            as_attachment=True
        )

    except Exception:

        return render_template('error.html')

if __name__ == '__main__':

    app.run(debug=True)