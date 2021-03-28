class CategoriaProduto:
    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome
