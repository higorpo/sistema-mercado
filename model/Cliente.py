import itertools
from model.Pessoa import Pessoa


class Cliente(Pessoa):
    novo_codigo = itertools.count()

    def __init__(self, vip: bool, nome: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, email, telefone, cpf)
        self.__codigo = next(Cliente.novo_codigo)
        self.__vip = vip
        self.__pedidos = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def pedidos(self) -> list:
        return self.__pedidos

    @property
    def vip(self) -> str:
        return 'Sim' if self.__vip == True else 'Não'

    @vip.setter
    def vip(self, cliente_vip: bool) -> str:
        self.__vip = cliente_vip

    def adicionar_novo_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def obter_pedidos(self):
        msg = ''
        for pedido in self.__pedidos:
            msg += f'\n\tCódigo {pedido.codigo} ({pedido.data_pedido})'
        return msg
