from flask import Flask, render_template, request
import cv2
import numpy as np
import easyocr
from ultralytics import YOLO
import os
import sqlite3

app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load EasyOCR reader
reader = easyocr.Reader(['en'])

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# SQLite Database Configuration
DB_FILE = "instance/anpr.db"

def init_db():
    """Create database table if not exists."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS anpr_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_name TEXT NOT NULL,
                plate_number TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

init_db()  # Initialize database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return upload()  # Call upload function when POST request is received
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read image using OpenCV
    img = cv2.imread(filepath)
   
    # Run YOLO for plate detection
    results = model(img)
    
    plate_number = "No plate detected"
     
    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()  # Get bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate_img = img[y1:y2, x1:x2]

            # Run OCR to extract text
            plate_text = reader.readtext(plate_img, detail=0)
            plate_number = " ".join(plate_text)
            break  # Stop after detecting the first plate

    # Store detected plate in database
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO anpr_records (image_name, plate_number) VALUES (?, ?)",
            (file.filename, plate_number)
        )
        conn.commit()

    return render_template('index.html', uploaded_image=file.filename, plate_number=plate_number)

@app.route('/records')
def show_records():
    """Fetch and display stored records."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM anpr_records ORDER BY timestamp DESC")
        records = cursor.fetchall()

    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
