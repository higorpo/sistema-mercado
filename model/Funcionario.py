import datetime
import itertools
from model.Pessoa import Pessoa


class Funcionario(Pessoa):
    novo_codigo = itertools.count()

    def __init__(self, data_contratacao: datetime, salario: float, nome: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, email, telefone, cpf)
        self.__codigo = next(Funcionario.novo_codigo)
        self.__data_contratacao = data_contratacao
        self.__salario = salario

    @property
    def codigo(self) -> int:
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
