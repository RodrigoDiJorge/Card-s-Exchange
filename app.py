from flask import Flask, render_template, request
import json

app = Flask(__name__)

pronto = {}

@app.route("/")
def index():

    pronto['cartas'] = [{},{}]
    pronto['carteira'] = 500
    with open('dados.json','w') as arq:
        arq.write(json.dumps(pronto))

    return render_template('index.html')


@app.route("/pay", methods=['GET'])
def pagamento():
    nome = request.args.get('card')
    valor = request.args.get('valor')
    print(valor)
    print(nome)
    return 'i'