from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
from sqlalchemy.exc import IntegrityError
from db import db
from models import *

app = Flask(__name__) # Serve para localizar o nome do arquivo
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///usersdata.db"
db.init_app(app) # Sempre iniciar o app
app.secret_key = 'manager'
log_man = LoginManager(app)
log_man.login_view = 'login'

@log_man.user_loader # Vai acessar um método especial da flask_login
def user_loader(id): # Busca usuário pelo id
    user = db.session.query(User).filter_by(id=id).first()
    return user

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="GET":
        return render_template('signup.html')
    elif request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['pasw']
        type_user = request.form['type_user']
        
        new_user = User(username=username, email=email, password=password, type_user=type_user)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            return render_template('error.html')
        
        login_user(new_user)
        
        return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST']) # methods servem para informar ao navegador quais tipos de atividades devem ser feitas com os dados enviados.
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = db.session.query(User).filter_by(email=email, password=password).first()
        if not user:
            return render_template('notlogged.html')
        
        login_user(user)
        return redirect(url_for('home'))

@app.route('/register_products', methods=['GET', 'POST'])
def reg_products():
    if request.method=='GET':
        return render_template('adm_pages/reg-prod.html')
    elif request.method=='POST':
        product_name = request.method['product_name']
        product_desc = request.method['product_desc']
        prod_category = request.method['category']
        product_price = request.method['product-price']
        quantity = request.method['quantity']
        
        new_product = Products(product_name=product_name, product_desc=product_desc, prod_category=prod_category, product_price=product_price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        
@app.route('/register_services', methods=['GET', 'POST'])
def reg_services():
    if request.method=='GET':
        return render_template('adm_pages/reg-serv.html')
    elif request.method=='POST':
        service_name = request.method['service_name']
        service_desc = request.method['service_desc']
        serv_category = request.method['category']
        professional = request.method['professional']
        service_price = request.method['service_price']
        
        new_service = Services(service_name=service_name, service_desc=service_desc, serv_category=serv_category, professional=professional, service_price=service_price)
        db.session.add(new_service)
        db.session.commit()

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5152)