from datetime import datetime
from app import db

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    origin = db.Column(db.String(100))
    course = db.Column(db.String(1000), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, firstname, lastname, course, origin):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.origin = origin
