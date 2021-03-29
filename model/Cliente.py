from model.Pessoa import Pessoa
from model.Pedido import Pedido


class Cliente(Pessoa):
    def __init__(self, vip: bool, nome: str, email: str, telefone: int, cpf: int):
        super().__init__(nome, email, telefone, cpf)
        self.__vip = vip
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def vip(self):
        return self.__vip

    @vip.setter
    def vip(self, cliente_vip: bool):
        self.__vip = cliente_vip
