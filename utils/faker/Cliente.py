from datetime import date
from model.Cliente import Cliente

# Cadastra o primeiro cliente
__dados_cliente = {
    'vip': True,
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

__fakeCliente1 = Cliente(*__dados_cliente.values())
__fakeCliente1.definir_endereco(*__dados_endereco.values())

# Cadastra o segundo cliente
__dados_cliente = {
    'vip': False,
    'nome': 'Pedro Pedroso',
    'email': 'pedro@email.com',
    'telefone': '(48) 99645-3859',
    'cpf': '222.222.222-22'
}

__dados_endereco = {
    'rua': 'Rua Vereador Celso Ramos',
    'cidade': 'Imbituba',
    'estado': 'Santa Catarina',
    'cep': '99999-320',
    'complemento': 'Casa'
}

__fakeCliente2 = Cliente(*__dados_cliente.values())
__fakeCliente2.definir_endereco(*__dados_endereco.values())

# Cadastra o terceiro cliente
__dados_cliente = {
    'vip': True,
    'nome': 'João Augusto',
    'email': 'joao.augusto@email.com',
    'telefone': '(48) 94456-4992',
    'cpf': '333.333.333-33'
}

__dados_endereco = {
    'rua': 'Rua Garibalde',
    'cidade': 'Imbituba',
    'estado': 'Santa Catarina',
    'cep': '93399-320',
    'complemento': 'Casa'
}

__fakeCliente3 = Cliente(*__dados_cliente.values())
__fakeCliente3.definir_endereco(*__dados_endereco.values())

fakeClientes = [__fakeCliente1, __fakeCliente2, __fakeCliente3]
