from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    mobile = db.Column(db.Integer)
    # dob = db.Column(db.Date)
    gender=db.Column(db.String(10))
    license = db.Column(db.String(100))
    password = db.Column(db.String(100))