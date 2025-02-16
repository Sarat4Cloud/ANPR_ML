from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anpr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define License Plate Model
class LicensePlate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Function to Create Tables
def create_tables():
    with app.app_context():  # ✅ Ensure Flask app context is active
        db.create_all()
        print("Database tables created successfully!")

if __name__ == "__main__":
    create_tables()
