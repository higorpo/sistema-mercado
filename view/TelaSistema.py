from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_opcoes(self, opcoes=[]):
        Terminal.clear_all(self)
        return super().mostrar_opcoes('Qual módulo do sistema você deseja acessar?', opcoes)
