from ..database.db import db
from uuid import uuid4

# def get_uuid():
#     return uuid4().hex

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(345), unique=True)
    # password = db.Column(db.Text, nullable=False)
