import utils.Log as Log
from view.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):

        pass

    def inicializa_sistema(self):
        Log.clear()
        Log.log('--------- Sistema de supermercado v1.0 ----------')
        Log.sucess('• Iniciando sistema')
        self.abre_tela()

    def abre_tela(self):
        pass
