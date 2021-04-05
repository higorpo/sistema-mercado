import itertools


class FormaPagamento:
    novo_codigo = itertools.count()

    def __init__(self, metodo: str):
        self.__codigo = next(FormaPagamento.novo_codigo)
        self.__metodo = metodo

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def metodo(self) -> str:
        return self.__metodo
