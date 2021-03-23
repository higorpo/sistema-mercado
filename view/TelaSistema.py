import utils.Log as Log
from view.AbstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_opcoes(self, opcoes=[]):
        Log.clear()
        return super().mostrar_opcoes('Qual módulo do sistema você deseja acessar?', opcoes)
