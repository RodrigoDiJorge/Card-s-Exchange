from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

id = 0

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
            print('foi')
            id = user["id"]
            print(user["usuario"])
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
       
    idCarta = request.args.get('id')
    
    for carta in card:
        if carta['id'] == idCarta:
            valor = carta['valor']
            for user in users:
                if user["id"] == id:
                    carteira = user["carteira"]
                    print(carteira)
                    carteira -= valor

    print(id)

