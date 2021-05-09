import uuid
from model.CategoriaProduto import CategoriaProduto


class Produto:

    def __init__(self, nome: str, qtd_estoque: int, marca: str, preco: float, categoria: CategoriaProduto):
        self.__codigo = uuid.uuid4()
        self.__qtd_estoque = qtd_estoque
        self.__nome = nome
        self.__marca = marca
        self.__preco = preco
        self.__categoria = categoria

    @property
    def codigo(self) -> uuid.UUID:
        return self.__codigo

    @property
    def qtd_estoque(self) -> int:
        return self.__qtd_estoque

    @qtd_estoque.setter
    def qtd_estoque(self, qtd_estoque: int):
        self.__qtd_estoque = qtd_estoque

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco

    @property
    def marca(self) -> float:
        return self.__marca

    @property
    def categoria(self) -> CategoriaProduto:
        return self.__categoria
