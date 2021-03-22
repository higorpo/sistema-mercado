class FormaPagamento:
    def __init__(self, metodo: str):
        self.__metodo = metodo

    @property
    def metodo(self) -> str:
        return self.__metodo
