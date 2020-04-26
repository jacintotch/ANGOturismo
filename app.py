from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("auth/index.html")

@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/about')
def about():
    return render_template("auth/about.html")