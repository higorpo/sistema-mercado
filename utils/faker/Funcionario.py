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

fakeFuncionario = Funcionario(*__dados_funcionario.values())
