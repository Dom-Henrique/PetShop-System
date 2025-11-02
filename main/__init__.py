from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__) # Serve para localizar o nome do arquivo

@app.route('/index')
def register():
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST']) # methods servem para informar ao navegador quais tipos de atividades devem ser feitas com os dados enviados.
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5152)