import utils.Log as Log
from view.TelaSistema import TelaSistema
import time

FAKE_BOOT_TIMER = 0  # use 1


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)

    def inicializa_sistema(self):
        Log.clear()
        Log.log('--------- Sistema de supermercado v1.0 ----------')
        Log.sucess('• Iniciando sistema')
        time.sleep(FAKE_BOOT_TIMER * 1)
        Log.info('• Configurando itens do sistema')
        time.sleep(FAKE_BOOT_TIMER*1)
        Log.warning('• Verificando existência de erros')
        time.sleep(FAKE_BOOT_TIMER*2)
        Log.info('• Abrindo tela inicial')
        time.sleep(FAKE_BOOT_TIMER*1)
        self.abre_tela()

    def abre_tela(self):
        self.__tela_sistema.mostrar_opcoes([
            'Teste',
            'Teste 2'
        ])
