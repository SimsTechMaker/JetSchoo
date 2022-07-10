from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit():
    auth_pass = request.form['auth_pass']
    auth_user = request.form['auth_user']
    
    print("le nom du user est : ", auth_user, "le mot de passe est ", auth_pass)
    return render_template('index.html')

""" if __name__ == "__main__":
    app.run() """