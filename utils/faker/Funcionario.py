from datetime import date
from model.Funcionario import Funcionario

__dados_funcionario = {
    'data_atual': date.today().strftime("%d/%m/%Y"),
    'salario': 1000.0,
    'nome': 'Higor Pires Oliveira',
    'email': 'higor@teste.com',
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

fakeFuncionario = Funcionario(*__dados_funcionario.values())
fakeFuncionario.definir_endereco(*__dados_endereco.values())
