from flask import Flask, jsonify
import random
import json
from unidecode import unidecode

app = Flask(__name__)

# Carregar conselhos do arquivo JSON
conselhos = []
with open('conselhos.json', 'r', encoding='utf-8') as f:
    conselhos = json.load(f)

# Função para remover acentos e diacríticos (substituindo "ê" por "e")
def corrigir_conselho(conselho):
     # Remove accents and diacritics using unidecode
    conselho_sem_acentos = unidecode(conselho)

    # Specifically replace "ê" with "e"
    conselho_sem_acentos = conselho_sem_acentos.replace("ê", "e")

    return conselho_sem_acentos

# Endpoint para obter um conselho aleatório
@app.route('/', methods=['GET'])
def obter_conselho():
    # Selecionar um conselho aleatório
    conselho_aleatorio = random.choice(conselhos)

    # Corrigir o texto do conselho (substituindo "ê" por "e")
    conselho_corrigido = corrigir_conselho(conselho_aleatorio)

    # Retornar o conselho em formato JSON
    return jsonify({'conselho': conselho_corrigido})

# Executar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
