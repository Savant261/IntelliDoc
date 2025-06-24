from flask import Flask, request, jsonify
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize SQLite database
conn = sqlite3.connect('documents.db')
conn.execute('CREATE TABLE IF NOT EXISTS docs (id INTEGER PRIMARY KEY, filename TEXT, upload_date TEXT)')
conn.commit()
conn.close()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and (file.filename.endswith('.pdf') or file.filename.endswith(('.png', '.jpg', '.jpeg'))):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        conn = sqlite3.connect('documents.db')
        conn.execute('INSERT INTO docs (filename, upload_date) VALUES (?, ?)', 
                    (file.filename, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)