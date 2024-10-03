from flask import Flask

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    return "<h1>Página inicial</h1><p>Eu sou Maria Clara</p>"

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1><p>Bem-vindo à galeria!</p>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1><p>Entre em contato conosco!</p>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1><p>Saiba mais sobre nós!</p>"