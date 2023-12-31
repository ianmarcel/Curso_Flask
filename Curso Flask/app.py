from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    nome = "ian"
    esporte = "tenis"
    return render_template("index.html",nome=nome,esporte2=esporte)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")