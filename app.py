from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variáveis globais para senha e guichê
senha_atual = 0
guiche_atual = 0

@app.route('/')
def index():
    return render_template('painel.html', senha=senha_atual, guiche=guiche_atual)

@app.route('/chamar', methods=['POST'])
def chamar():
    global senha_atual, guiche_atual
    senha_atual += 1
    guiche_atual = request.json.get('guiche', 1)
    return jsonify({"senha": senha_atual, "guiche": guiche_atual})

@app.route('/controle')
def controle():
    return render_template('chamar.html')

@app.route('/atualizar', methods=['GET'])
def atualizar():
    return jsonify({"senha": senha_atual, "guiche": guiche_atual})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
