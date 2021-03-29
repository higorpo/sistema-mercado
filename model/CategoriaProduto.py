import itertools


class CategoriaProduto:
    novo_codigo = itertools.count()

    def __init__(self, nome: str):
        self.__codigo = next(CategoriaProduto.novo_codigo)
        self.__nome = nome

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
