from model.Pedido import Pedido
from model.Produto import Produto


class ItemPedido:
    def __init__(self, pedido: Pedido, produto: Produto, quantidade: int):
        self.__pedido = pedido
        self.__quantidade = quantidade
        self.__produto = produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @property
    def produto(self) -> Produto:
        return self.__produto

    def obter_dados_item_pedido(self) -> str:
        return f'{self.__quantidade} {self.__produto.nome.lower()}(s)\n'
