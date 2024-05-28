#api
from flask import Flask, request, jsonify

app = Flask(__name__)

# Armazenamento em memória
usuarios = []

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    email = data.get('email')
    telefone = data.get('telefone')
    
    # Adiciona o usuário à lista
    usuarios.append({
        'email': email,
        'telefone': telefone
    })
    
    # Aqui você pode adicionar o código para se comunicar com o webhook da Hook0
    
    return jsonify({'status': 'Usuário cadastrado com sucesso!'}), 201

@app.route('/listagem', methods=['GET'])
def listagem():
    return jsonify(usuarios), 200

if __name__ == '__main__':
    app.run(debug=True)
