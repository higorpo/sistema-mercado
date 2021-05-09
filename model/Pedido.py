from model.FormaPagamento import FormaPagamento
from model.Cliente import Cliente
from model.Funcionario import Funcionario
import datetime
import itertools


class Pedido:
    novo_codigo = itertools.count()

    def __init__(self, observacao: str, data_pedido: datetime, cliente: Cliente, funcionario: Funcionario, forma_pagamento: FormaPagamento):
        self.__codigo = next(Pedido.novo_codigo)
        self.__observacao = observacao
        self.__data_pedido = data_pedido
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__forma_pagamento = forma_pagamento
        self.__itens_pedido = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def observacao(self) -> str:
        return self.__observacao

    @property
    def data_pedido(self) -> datetime:
        return self.__data_pedido

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def funcionario(self) -> Funcionario:
        return self.__funcionario

    @property
    def forma_pagamento(self) -> FormaPagamento:
        return self.__forma_pagamento

    def obter_dados_faturamento(self) -> str:
        cliente_vip = self.__cliente.vip
        total_compra = 0.0

        for itens_pedido in self.__itens_pedido:
            total_compra += int(itens_pedido.produto.preco) * \
                int(itens_pedido.quantidade)

        if cliente_vip:
            total_compra = total_compra * 0.9

        return round(total_compra)

    def adicionar_item_pedido(self, item_pedido):
        self.__itens_pedido.append(item_pedido)

    def obter_itens_pedido(self) -> list:
        msg = ''
        for item_pedido in self.__itens_pedido:
            msg += item_pedido.obter_dados_item_pedido()
        return msg
