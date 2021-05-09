import uuid

from dao.AbstractDAO import DAO
from model.Produto import Produto


class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/produto.pkl')

    def add(self, produto: Produto):
        if ((produto is not None) and isinstance(produto, Produto) and isinstance(produto.codigo, uuid.UUID)):
            super().add(produto.codigo, produto)

    def remove(self, produto: Produto):
        if ((produto is not None) and isinstance(produto, Produto) and isinstance(produto.codigo, uuid.UUID)):
            super().remove(produto.codigo)
