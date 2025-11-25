# Aqui só importa a classe

from db import db
from flask_login import UserMixin # Serve para identificar a classe como uma classe pelo login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True) # Preencher automaticamente
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    #type_user = db.Column(db.Integer, nullable=False)
    
class Products(db.Model):
    __tablename__ = "products"
    prod_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    product_desc = db.Column(db.String, nullable=False)
    prod_category = db.Column(db.Sting, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
class Services(db.Model):
    __tablename__ = "services"
    serv_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String, nullable=False)
    service_desc = db.Column(db.String, nullable=False)
    serv_category = db.Column(db.String, nullable=False)
    professional = db.Column(db.ForeignKey())
    service_price = db.Column(db.Integer, nullable=False)
    
class Professional(db.Model):
    __tablename__ = "professionals"
    prof_id = db.Column(db.Integer, primary_key=True)
    prof_name = db.Column(db.String, nullable=False)
    prof_ocupation = db.Column(db.String, nullable=False)