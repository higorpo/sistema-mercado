from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from messages.Sistema import mensagens as mensagens_sistema


class TelaSistema(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_opcoes(self, opcoes=[]):
        Terminal.clear_all(self)
        return super().mostrar_opcoes(mensagens_sistema.get('titulo_tela_opcoes_modulo'), opcoes)
