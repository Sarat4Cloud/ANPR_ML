# ANPR_ML

**Recommended Folder Structure**
ANPR-Project/

│── anpr_env/                  # virtual environment

│── static/                  # Stores images, CSS, JS files

│── templates/               # HTML templates for Flask UI (Index.html and Records.html)

│── yolov8n.pt/                  # Stores trained YOLO model files

│── dataset/                 # Training dataset for YOLO

│── instance/                 # container for SQLLite Database

│── app.py                  # Main Flask application

│── database.py              # Database handling file (SQLite)

│── README.md                # Project documentation


****Step - By - Step Installation Guide****

**Step 1: Install Required Software**
Before we begin, make sure you have the following installed:
Python 3.8+ → Download from Python Official Site
pip (Package Manager) → Comes with Python installation
Git 

**Step 2: Setup Project Folder**
Create a new folder for your project: 
mkdir ANPR_Project
cd ANPR_Project

**Step 3: Create & Activate Virtual Environment**
1.	Create Virtual Environment (Run in CMD)
--python -m venv anpr_env
This will create a folder anpr_env inside your project directory.
2.	Activate Virtual Environment (Run in CMD)
•	Windows:
--anpr_env\Scripts\activate

**Step 4: Install Required Libraries**
Open Command Prompt (Windows)) and run:
--pip install torch torchvision torchaudio ultralytics easyocr opencv-python flask flask-cors flask-sqlalchemy numpy

**Explanation:**
•	Ultralytics → Runs YOLOv8
•	EasyOCR → Reads text from images
•	OpenCV → Image processing
•	Flask → Web framework
•	SQLite (via SQLAlchemy) → Database integration

**Step 5: Download YOLOv8 Pretrained Model**
Since YOLOv8 is used for plate detection, you need to download its model.
Run the following command:
--yolo task=detect mode=predict model=yolov8n.pt source="bus.jpg"
If you don’t have yolov8n.pt, it will automatically download the model.


**Step 6: Create SQLite Database & Flask Backend**
1.	Create database.py
This file sets up the SQLite database to store recognized plates. File available in Git.
2.	Create app.py (Main Flask Application)
This script handles file uploads, processes images using YOLOv8 and EasyOCR, and stores results in SQLite.

**Step 7: Create Index.html & Records.html**
1.	Create Index.html
Creates the main HTML Home Page for Upload and Detect feature.
2.	Create Records.html
Creates Records.html page to display records in SQL Lite Database
(Refer to the files in the Git)

**Step 8: Running the ANPR System**
1.	Start the Flask Server
Run the command :
--python app.py
You should see output like:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

**🎯 Summary of Steps**
•	Installed Python libraries
•	Created Flask App with SQLite Database
•	Integrated YOLOv8 for License Plate Detection
•	Used EasyOCR for Text Recognition
•	HTML for Home Page and Records.HTML for Database Records.




**Video Link** : - https://www.youtube.com/watch?v=wKiy-yxHEBU&t=31s 
