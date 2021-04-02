from model.Produto import Produto
from model.CategoriaProduto import CategoriaProduto

categoria_produto = CategoriaProduto('Limpeza')

__dados_produto = {
    'nome': 'Vassoura',
    'qtd_estoque': 10,
    'marca': 'Vassouriu',
    'preco': 8.40,
    'categoria': categoria_produto
}

__fakeProduto1 = Produto(*__dados_produto.values())

# ---------------

__dados_produto = {
    'nome': 'Esparadrapo',
    'qtd_estoque': 23,
    'marca': 'Vassouriu',
    'preco': 3.40,
    'categoria': categoria_produto
}

__fakeProduto2 = Produto(*__dados_produto.values())

# ---------------

__dados_produto = {
    'nome': 'OMO',
    'qtd_estoque': 16,
    'marca': 'OMO',
    'preco': 11.40,
    'categoria': categoria_produto
}

__fakeProduto3 = Produto(*__dados_produto.values())

# ---------------

fakeProdutos = [__fakeProduto1, __fakeProduto2, __fakeProduto3]
