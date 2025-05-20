import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('image_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_data BLOB NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            classification_result TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_image_data(image_binary, classification_result=None):
    conn = sqlite3.connect('image_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images (image_data, classification_result)
        VALUES (?, ?)
    ''', (image_binary, classification_result))
    conn.commit()
    conn.close()


def get_image_by_id(image_id):
    conn = sqlite3.connect('image_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT image_data FROM images WHERE id = ?', (image_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


def get_all_images():
    conn = sqlite3.connect('image_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM images')
    rows = cursor.fetchall()
    conn.close()
    return rows 