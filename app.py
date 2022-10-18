from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

pronto = {}

@app.route("/")
def index():



    return render_template('index.html')


@app.route("/pay", methods=['GET'])
def pagamento():
    file = open('dados.json')
    dados = json.load(file)
       
    id = request.args.get('id')
    

    print(id)

    with open('dados.json','w') as arq:
        arq.write(json.dumps(pronto))
    return 'i'