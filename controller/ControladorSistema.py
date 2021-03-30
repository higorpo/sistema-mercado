import utils.Log as Log
import time
from controller.ControladorCategoriasProduto import ControladorCategoriasProduto
from controller.ControladorFormasPagamento import ControladorFormasPagamento
from controller.ControladorFuncionarios import ControladorFuncionarios
from view.TelaSistema import TelaSistema
from view.TelaMensagemSistema import TelaMensagemSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_cat_produto = ControladorCategoriasProduto(self)
        self.__controlador_formas_pagamento = ControladorFormasPagamento(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__tela_sistema = TelaSistema(self)
        self.__tela_mensagem_sistema = TelaMensagemSistema(self)

    def inicializa_sistema(self):
        try:
            self.mensagem_sistema.clear()
            self.abre_tela()
        except KeyboardInterrupt:
            self.mensagem_sistema.error(
                'ERRO: Você interrompeu a entrada de dados via teclado...')
            self.mensagem_sistema.info('Fechando sistema...')
            exit(0)

    def abre_tela(self):
        lista_opcoes = {
            4: self.__controlador_cat_produto.abre_tela,
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

            try:
                lista_opcoes[opcao_selecionada]()
            except KeyError:
                self.mensagem_sistema.error(
                    'ERRO: A opção selecionada não foi implementada!')
                time.sleep(2)

    @property
    def controlador_cat_produto(self) -> ControladorCategoriasProduto:
        return self.__controlador_cat_produto

    @property
    def controlador_formas_pagamento(self) -> ControladorFormasPagamento:
        return self.__controlador_formas_pagamento

    @property
    def controlador_funcionarios(self) -> ControladorFuncionarios:
        return self.__controlador_funcionarios

    @property
    def mensagem_sistema(self) -> TelaMensagemSistema:
        return self.__tela_mensagem_sistema
