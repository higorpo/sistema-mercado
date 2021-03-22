import utils.Log as Log
import time
from controller.ControladorFormasPagamento import ControladorFormasPagamento
from view.TelaSistema import TelaSistema

FAKE_BOOT_TIMER = 0  # use 1


class ControladorSistema:
    def __init__(self):
        self.__controlador_formas_pagamento = ControladorFormasPagamento(self)
        self.__tela_sistema = TelaSistema(self)

    def inicializa_sistema(self):
        try:
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
        except KeyboardInterrupt:
            Log.error('ERRO: Algo deu errado...')
            exit(0)

    def abre_tela(self):
        lista_opcoes = {
            5: self.__controlador_formas_pagamento.abre_tela
        }

        opcao_selecionada = self.__tela_sistema.mostrar_opcoes([
            'Clientes',
            'Funcionários',
            'Fornecedores',
            'Produtos',
            'Categorias de produto',
            'Formas de pagamento',
            'Pedidos'
        ])

        lista_opcoes[opcao_selecionada]()
