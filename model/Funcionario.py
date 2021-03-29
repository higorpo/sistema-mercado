from model.Pessoa import Pessoa
import datetime


class Funcionario(Pessoa):
    def __init__(self, data_contratacao: datetime, salario: float, nome: str, email: str, telefone: int, cpf: int):
        super().__init__(nome, email, telefone, cpf)
        self.__data_contratacao = data_contratacao
        self.__salario = salario

    @property
    def data_contratacao(self):
        return self.__data_contratacao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario
