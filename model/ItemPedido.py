from model.Pedido import Pedido
from model.Produto import Produto


class ItemPedido:
    def __init__(self, pedido: Pedido, produto: Produto, quantidade: int):
        # TODO não sei o que fazer com pedido aqui
        self.__pedido = pedido
        self.__quantidade = quantidade
        self.__produto = produto

    def obter_dados_item_pedido(self) -> str:
        return f'\t{self.__quantidade} {self.__produto.nome.lower()}(s)\n'
