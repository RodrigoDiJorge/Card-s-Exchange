import string
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

id = ""
@app.route("/")
def index():             
    return render_template('index.html')

@app.route("/cards", methods=["GET"])
def cards():
    usuario = request.args.get('username')
    print(usuario)
    file = open('dados.json')
    dados = json.load(file)

    for user in dados:
        
        if user["usuario"] == usuario:      
            global id
            id = user["id"]
            return render_template('cartas.html')
        else:
            return render_template('index.html')
        
    return 'logado'

@app.route("/pay", methods=['GET'])
def pagamento():
    file = open('cartas.json')
    card = json.load(file)
    file2 = open('dados.json')
    users = json.load(file2)
    
    valor = ''

    idCarta = request.args.get('id')
    print(idCarta)
    for carta in card:
        if carta['id'] == idCarta:
            valor = carta['valor']
            for user in users:
                if user["id"] == id:
                    carteira = user["carteira"]
                    result = float(carteira) - float(valor)
                    user['carteira'] = result
                    valor = user['carteira']

    file.close()
    file2.close()
    with open("dados.json", "w") as newFile:
        json.dump(users, newFile)
    return render_template("comprovante.html", variable = valor)

@app.route("/comprovante")
def comprova():
    return render_template("cartas.html")