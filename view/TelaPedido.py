from view.AbstractTela import AbstractTela
from messages.Pedido import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from datetime import date
from utils.Terminal import Terminal


class TelaPedido(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print(mensagens.get('label_observacao'))
        return super().ler_string()
