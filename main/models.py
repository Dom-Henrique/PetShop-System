# Aqui só importa a classe

from db import db
from flask_login import UserMixin # Serve para identificar a classe como uma classe pelo login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    type_user = db.Column(db.Integer, nullable=False)