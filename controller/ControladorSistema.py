import utils.Log as Log
import time
from controller.ControladorFormasPagamento import ControladorFormasPagamento
from controller.ControladorFuncionarios import ControladorFuncionarios
from view.TelaSistema import TelaSistema

FAKE_BOOT_TIMER = 0  # use 1


class ControladorSistema:
    def __init__(self):
        self.__controlador_formas_pagamento = ControladorFormasPagamento(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
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
            1: self.__controlador_funcionarios.abre_tela,
            5: self.__controlador_formas_pagamento.abre_tela,
            7: exit
        }

        while True:
            opcao_selecionada = self.__tela_sistema.mostrar_opcoes([
                'Clientes',
                'Funcionários',
                'Fornecedores',
                'Produtos',
                'Categorias de produto',
                'Formas de pagamento',  # 5
                'Pedidos',
                'Sair do sistema'
            ])

            lista_opcoes[opcao_selecionada]()

    def controlador_formas_pagamento(self):
        return self.__controlador_formas_pagamento

    def controlador_funcionarios(self):
        return self.__controlador_funcionarios
