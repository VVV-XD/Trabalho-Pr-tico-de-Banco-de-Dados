from flask import Flask, jsonify, request

class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

app = Flask(__name__)

usuarios = []

@app.route('/usuario', methods=['POST'])
def adicionar_usuario():
    dados_usuario = request.json
    novo_usuario = Usuario(
        cpf=dados_usuario['cpf'],
        nome=dados_usuario['nome'],
        data_nascimento=dados_usuario['data_nascimento']
    )
    usuarios.append(novo_usuario)
    return jsonify({"mensagem": "Usuário adicionado com sucesso"}), 201

@app.route('/usuario', methods=['GET'])
def obter_usuarios():
    usuarios_json = [
        {
            'cpf': usuario.cpf,
            'nome': usuario.nome,
            'data_nascimento': usuario.data_nascimento
        }
        for usuario in usuarios
    ]
    return jsonify({"usuarios": usuarios_json})

if __name__ == '__main__':
    app.run(debug=True)
