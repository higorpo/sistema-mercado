from model.FormaPagamento import FormaPagamento
from model.ItemPedido import ItemPedido
from model.Cliente import Cliente
import datetime
import itertools


class Pedido:
    novo_codigo = itertools.count()

    def __init__(self, observacao: str, data_pedido: datetime, cliente: Cliente, forma_pagamento: FormaPagamento):
        self.__codigo = next(Pedido.novo_codigo)
        self.__observacao = observacao
        self.__data_pedido = data_pedido
        self.__cliente = cliente
        self.__forma_pagamento = forma_pagamento

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
    def forma_pagamento(self) -> FormaPagamento:
        return self.__forma_pagamento

    def obter_dados_faturamento(self) -> str:
        # Implementar o resto antes
        pass

    def adicionar_item_pedido(self, item_pedido: ItemPedido) -> ItemPedido:
        # Implementar o resto antes
        pass

    def obter_itens_pedido(self):
        # Implementr o resto antes
        pass
