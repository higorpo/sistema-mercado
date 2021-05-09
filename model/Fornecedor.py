import uuid
from model.Endereco import Endereco
from model.CategoriaProduto import CategoriaProduto
from utils.Formatters import Formatters


class Fornecedor:

    def __init__(self, nome: str, cnpj: str, email: str, telefone: str, fornece: CategoriaProduto):
        self.__codigo = uuid.uuid4()
        self.__nome = nome
        self.__cnpj = Formatters.formatar_cnpj(cnpj)
        self.__email = email
        self.__telefone = Formatters.formatar_telefone(telefone)
        self.__fornece = fornece
        self.__endereco = None

    @property
    def codigo(self) -> uuid.UUID:
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

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
    def endereco(self):
        return self.__endereco.pegar_endereco()

    def definir_endereco(self, rua: str, cidade: str, estado: str, cep: str, complemento: str):
        self.__endereco = Endereco(rua, cidade, estado, cep, complemento)

    @property
    def fornece(self) -> CategoriaProduto:
        return self.__fornece
