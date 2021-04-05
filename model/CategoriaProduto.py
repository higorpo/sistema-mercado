import itertools


class CategoriaProduto:
    novo_codigo = itertools.count()

    def __init__(self, nome: str):
        self.__codigo = next(CategoriaProduto.novo_codigo)
        self.__nome = nome
        self.__produtos = []

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def produtos(self) -> list:
        return self.__produtos

    def adicionar_produto(self, produto):
        if produto not in self.__produtos:
            self.__produtos.append(produto)
