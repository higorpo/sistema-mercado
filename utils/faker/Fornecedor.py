from model.Fornecedor import Fornecedor
from model.CategoriaProduto import CategoriaProduto

__dados_fornecedor = {
    'nome': 'Djalma Tranportes',
    'cnpj': '71.487.805/0001-50',
    'email': 'djalma@gmail.com',
    'telefone': '(48) 99103-7834',
    'fornece': CategoriaProduto('Café')
}

__dados_endereco = {
    'rua': 'Rua Vereador Cyro Bacha',
    'cidade': 'Criciúma',
    'estado': 'Santa Catarina',
    'cep': '88880-320',
    'complemento': 'Casa'
}

fakeFornecedor = Fornecedor(*__dados_fornecedor.values())
fakeFornecedor.definir_endereco(*__dados_endereco.values())
