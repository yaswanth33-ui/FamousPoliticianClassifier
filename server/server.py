from flask import Flask, request, jsonify
from utils import classify_image, convert_base64_to_image
from flask_cors import CORS
from database import save_image_data, init_db, get_image_by_id
import sqlite3

app = Flask(__name__)
CORS(app)


init_db()

@app.route('/api/classify', methods=['POST'])
def classify():
    image_data = request.json.get('image_data')
    image_binary = convert_base64_to_image(image_data)
    save_image_data(image_binary)  
    latest_id = get_latest_image_id()  
    stored_image = get_image_by_id(latest_id) 
    classification_result = classify_image(stored_image) 
    return jsonify(classification_result)

def get_latest_image_id():
    conn = sqlite3.connect('image_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM images')
    latest_id = cursor.fetchone()[0]
    conn.close()
    return latest_id

if __name__ == '__main__':
    app.run(port=5000, debug=True)