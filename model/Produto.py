import itertools
from model.CategoriaProduto import CategoriaProduto


class Produto:
    novo_codigo = itertools.count()

    def __init__(self, nome: str, qtd_estoque: int, marca: str, preco: float, categoria: CategoriaProduto):
        self.__codigo = next(Produto.novo_codigo)
        self.__qtd_estoque = qtd_estoque
        self.__nome = nome
        self.__marca = marca
        self.__preco = preco
        self.__categoria = categoria

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def qtd_estoque(self) -> int:
        return self.__qtd_estoque

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float) -> float:
        self.__preco = preco

    @property
    def marca(self) -> float:
        return self.__marca

    @property
    def categoria(self) -> CategoriaProduto:
        return self.__categoria
