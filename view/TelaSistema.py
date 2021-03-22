import utils.Log as Log
from view.AbstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_opcoes(self, opcoes=[]):
        Log.clear()
        Log.log('--------- Sistema de supermercado v1.0 ----------')
        super().mostrar_opcoes(opcoes)
