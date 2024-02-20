import requests


novo_usuario = {
    "cpf": 123456789,
    "nome": "Victor Ribeiro",
    "data_nascimento": "24-01-1998"
}

url = "http://127.0.0.1:5000/usuario"


response = requests.post(url, json=novo_usuario)

if response.status_code == 201:
    print("Usuário adicionado com sucesso!")
else:
    print("Erro ao adicionar usuário:", response.status_code)
