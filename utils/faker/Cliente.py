from datetime import date
from model.Cliente import Cliente

__dados_cliente = {
    'vip': 'sim',
    'nome': 'John Lennon',
    'email': 'john@beatles.com',
    'telefone': '(48) 99645-3859',
    'cpf': '111.111.111-11'
}

__dados_endereco = {
    'rua': 'Rua Vereador Cyro Bacha',
    'cidade': 'Criciúma',
    'estado': 'Santa Catarina',
    'cep': '88880-320',
    'complemento': 'Casa'
}

fakeCliente = Cliente(*__dados_cliente.values())
fakeCliente.definir_endereco(*__dados_endereco.values())
