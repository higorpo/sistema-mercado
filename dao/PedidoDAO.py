from dao.AbstractDAO import DAO
from model.Pedido import Pedido


class PedidoDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/pedido.pkl')

    def add(self, pedido: Pedido):
        if ((pedido is not None) and isinstance(pedido, Pedido) and isinstance(pedido.codigo, int)):
            super().add(pedido.codigo, pedido)

    def remove(self, pedido: Pedido):
        if ((pedido is not None) and isinstance(pedido, Pedido) and isinstance(pedido.codigo, int)):
            super().remove(pedido.codigo)
