from flask import (Flask, render_template, request)

app = Flask(__name__) 

@app.route("/", methods=('GET',)) 
def index(): 
    nome= request.args.get('nome')
    return f"""<h1>Página inicial</h1>
    <p>Olá {nome}, que nome bonito!
    """ 

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1><p>Bem-vindo à nossa galeria!</p>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1><p>Entre em contato conosco!</p>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1><p>Saiba mais sobre nós!</p>"


from flask import (Flask, request)
app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): 
  nome= request.args.get('nome') #use o seu nome
  #HTML retornado
  return f"""<h1>Página Inicial</h1>
   <p>Olá {nome}, que nome bonito!
   """# função responsável pela página

 # HTML retornado|

@app.route("/outra_pagina", methods =('GET',))
def outra():
  return "<h1>Outra página</h1>"

@app.route("/galeria", methods =('GET',))
def galeria():
  return "<h1>galeria</h1>"

@app.route("/contato", methods =('GET',))
def contato():
  return "<h1>contato</h1>" 

@app.route("/sobre", methods =('GET',))
def sobre():
  return "<h1>sobre</h1>"

def index(): # função responsável pela página
  nome='Rodrigo' #use o seu nome
  #HTML retornado
  return f"""<h1>Página Inicial</h1>
   <p>Olá {nome}, que nome bonito!
   """

@app.route("/area/<float:largura>/<float:altura>")
def area(largura: float, altura:float):
  return f""" 
<h1> A área informada> L={largura}* A={altura} Area={largura*altura}</h1>"""

@app.route("/par_ou_impar/<float:numero>", methods=('GET',))
def par_ou_impar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(sobrenome, nome):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:numero>/<float:elevado>")
def potencia(numero: float, elevado:float):
  return f""" 
<h1> A área informada> n={numero}** e={elevado} Volume={numero**elevado} </h1>"""

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):
   
    if 'numero' in request.args:
        numero =int (request.args.get('numero'))
    return render_template('tabuada.html', numero=numero)