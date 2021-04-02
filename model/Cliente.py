from model.Pessoa import Pessoa
#from model.Pedido import Pedido


class Cliente(Pessoa):
    def __init__(self, vip: bool, nome: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, email, telefone, cpf)
        self.__vip = vip
        self.__pedidos = []

    @property
    def pedidos(self) -> list:
        return self.__pedidos

    @property
    def vip(self) -> str:
        return self.__vip

    @vip.setter
    def vip(self, cliente_vip: bool) -> str:
        self.__vip = cliente_vip

    def adicionar_novo_pedido(self):
        pass
