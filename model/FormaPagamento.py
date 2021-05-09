import uuid


class FormaPagamento:

    def __init__(self, metodo: str):
        self.__codigo = uuid.uuid4()
        self.__metodo = metodo

    @property
    def codigo(self) -> uuid.UUID:
        return self.__codigo

    @property
    def metodo(self) -> str:
        return self.__metodo
