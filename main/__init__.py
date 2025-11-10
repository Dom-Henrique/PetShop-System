from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
from db import db
from models import User

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

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method=="GET":
        return render_template('signup.html')
    elif request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['pasw']
        type_user = request.form['type_user']
        
        new_user = User(username=username, email=email, password=password, type_user=type_user)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST']) # methods servem para informar ao navegador quais tipos de atividades devem ser feitas com os dados enviados.
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['pasw']
        
        user_logged = db.session.query(User).filter_by(email=email, password=password).first()
        if not user_logged:
            return render_template('notlogged.html')
        
        login_user(user_logged)
        return redirect(url_for('home'))

@app.route('/home')        
def home():
    return render_template('home.html')

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