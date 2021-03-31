from abc import ABC, abstractmethod
from model.Endereco import Endereco


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, email: str, telefone: str, cpf: str):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__cpf = cpf
        self.__endereco = None

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    def definir_endereco(self, rua: str, cidade: str, estado: str, cep: str, complemento: str):
        self.__endereco = Endereco(rua, cidade, estado, cep, complemento)

    @property
    def endereco(self):
        return self.__endereco.pegar_endereco()
