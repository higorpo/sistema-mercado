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

    def listar(self, pedidos):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))
        if len(pedidos) == 0:
            print(mensagens.get('nada_cadastrado'))
        else:
            for pedido in pedidos:
                print(mensagens.get('lista_valores')(pedido))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()
