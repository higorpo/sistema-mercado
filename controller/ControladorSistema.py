import PySimpleGUI as sg
from controller.ControladorCategoriasProduto import ControladorCategoriasProduto
from controller.ControladorFormasPagamento import ControladorFormasPagamento
from controller.ControladorFuncionarios import ControladorFuncionarios
from controller.ControladorFornecedores import ControladorFornecedores
from controller.ControladorClientes import ControladorClientes
from controller.ControladorPedidos import ControladorPedidos
from controller.ControladorProdutos import ControladorProdutos
from view.TelaSistema import TelaSistema
from view.TelaMensagemSistema import TelaMensagemSistema
from messages.Sistema import mensagens as mensagens_sistema


class ControladorSistema:
    __instance = None

    def __init__(self):
        self.__controlador_cat_produto = ControladorCategoriasProduto(self)
        self.__controlador_formas_pagamento = ControladorFormasPagamento(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__controlador_fornecedores = ControladorFornecedores(self)
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_pedidos = ControladorPedidos(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__tela_sistema = TelaSistema(self)
        self.__tela_mensagem_sistema = TelaMensagemSistema(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    def inicializa_sistema(self):
        try:
            self.abre_tela()
        except NotImplementedError:
            exit(0)

    def abre_tela(self):
        lista_opcoes = {
            0: self.__controlador_clientes.abre_tela,
            1: self.__controlador_funcionarios.abre_tela,
            2: self.__controlador_fornecedores.abre_tela,
            3: self.__controlador_cat_produto.abre_tela,
            4: self.__controlador_formas_pagamento.abre_tela,
            5: self.__controlador_produtos.abre_tela,
            6: self.__controlador_pedidos.abre_tela,
            7: self.fechar_sistema
        }

        while True:
            opcao_selecionada = self.__tela_sistema.mostrar_opcoes([
                mensagens_sistema.get('menu_clientes'),
                mensagens_sistema.get('menu_funcionarios'),
                mensagens_sistema.get('menu_fornecedores'),
                mensagens_sistema.get('menu_cat_produto'),
                mensagens_sistema.get('menu_formas_pagamento'),
                mensagens_sistema.get('menu_produtos'),
                mensagens_sistema.get('menu_pedidos'),
                mensagens_sistema.get('menu_sair_sistema')
            ])

            try:
                self.__tela_sistema.fechar_tela()

                if opcao_selecionada == sg.WIN_CLOSED:
                    self.fechar_sistema()
                    return

                lista_opcoes[opcao_selecionada]()

            except KeyError:
                raise NotImplementedError

    def fechar_sistema(self):
        self.__controlador_cat_produto.dao.save_all()
        self.__controlador_formas_pagamento.dao.save_all()
        self.__controlador_funcionarios.dao.save_all()
        self.__controlador_fornecedores.dao.save_all()
        self.__controlador_clientes.dao.save_all()
        self.__controlador_pedidos.dao.save_all()
        self.__controlador_produtos.dao.save_all()
        exit(0)

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
    def controlador_fornecedores(self) -> ControladorFornecedores:
        return self.__controlador_fornecedores

    @property
    def controlador_clientes(self) -> ControladorClientes:
        return self.__controlador_clientes

    @property
    def controlador_pedidos(self) -> ControladorPedidos:
        return self.__controlador_pedidos

    @property
    def controlador_produtos(self) -> ControladorProdutos:
        return self.__controlador_produtos

    @property
    def mensagem_sistema(self) -> TelaMensagemSistema:
        return self.__tela_mensagem_sistema
