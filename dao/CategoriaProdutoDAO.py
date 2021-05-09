import uuid

from dao.AbstractDAO import DAO
from model.CategoriaProduto import CategoriaProduto


class CategoriaProdutoDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/categoria_produto.pkl')

    def add(self, categoria_produto: CategoriaProduto):
        if ((categoria_produto is not None) and isinstance(categoria_produto, CategoriaProduto) and isinstance(categoria_produto.codigo, uuid.UUID)):
            super().add(categoria_produto.codigo, categoria_produto)

    def remove(self, categoria_produto: CategoriaProduto):
        if ((categoria_produto is not None) and isinstance(categoria_produto, CategoriaProduto) and isinstance(categoria_produto.codigo, uuid.UUID)):
            super().remove(cateogira_produto.codigo)
