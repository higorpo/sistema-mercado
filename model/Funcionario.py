import datetime
import uuid
from model.Pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, data_contratacao: datetime, salario: float, nome: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, email, telefone, cpf)
        self.__codigo = uuid.uuid4()
        self.__data_contratacao = data_contratacao
        self.__salario = salario

    @property
    def codigo(self) -> uuid.UUID:
        return self.__codigo

    @property
    def data_contratacao(self):
        return self.__data_contratacao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario
