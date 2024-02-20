import requests


url = "http://127.0.0.1:5000/usuario"


response = requests.get(url)


if response.status_code == 200:
    usuarios = response.json()["usuarios"]
    for usuario in usuarios:
        print("CPF:", usuario["cpf"])
        print("Nome:", usuario["nome"])
        print("Data de Nascimento:", usuario["data_nascimento"])
        print("------------------------")
else:
    print("Erro ao obter usuários:", response.status_code)
