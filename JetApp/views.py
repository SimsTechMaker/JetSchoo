from atexit import register
import re
from flask import Flask, render_template, request
from .form import ResiterForm

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('listeEtu.html')



@app.route('/register')
def register():
    form = ResiterForm()

    return render_template('regist.html',form=form,title="Inscription", )
    
    
@app.route('/submit', methods=['POST'])
def submit():
    auth_pass = request.form['auth_pass']
    auth_user = request.form['auth_user']
    
    print("le nom du user est : ", auth_user, "le mot de passe est ", auth_pass)
    return render_template('index.html')

""" if __name__ == "__main__":
    app.run() """