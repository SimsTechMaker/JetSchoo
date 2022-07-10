from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/index')
def index():
    return render_template('index.html')




""" if __name__ == "__main__":
    app.run() """