from model.Pedido import Pedido
from model.Produto import Produto


class ItemPedido:
    def __init__(self, pedido: Pedido, produto: Produto, quantidade: int):
        self.__pedido = pedido
        self.__quantidade = quantidade
        self.__produto = produto

    # def adicionar_item_pedido(self, item_pedido: ItemPedido):
        # Ver se isso aqui tá correto mesmo
        # pass
