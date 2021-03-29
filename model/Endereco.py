class Endereco:
    def __init__(self, rua: str, cidade: str, estado: str, cep: int, complemento: str):
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep
        self.__complemento = complemento

    def pegar_endereco(self) -> str:
        return f"{self.__rua}, {self.__complemento}, {self.__cep}, {self.__cidade}, {self.__estado}"
