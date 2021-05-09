import PySimpleGUI as sg
from messages.Sistema import mensagens as mensagens_sistema
from view.AbstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

        # Tela
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        lista_botoes = map(lambda x: [sg.Button(x[1], key=x[0], button_color='#52b1eb' if mensagens_sistema.get('menu_sair_sistema') != x[1] else '#f03737', auto_size_button=False, size=(30, 2))], enumerate([
            mensagens_sistema.get('menu_clientes'),
            mensagens_sistema.get('menu_funcionarios'),
            mensagens_sistema.get('menu_fornecedores'),
            mensagens_sistema.get('menu_cat_produto'),
            mensagens_sistema.get('menu_formas_pagamento'),
            mensagens_sistema.get('menu_produtos'),
            mensagens_sistema.get('menu_pedidos'),
            mensagens_sistema.get('menu_sair_sistema')
        ]))

        layout = [
            [sg.Text('Selecione uma das opções abaixo..'), ],
            lista_botoes
        ]

        w, h = sg.Window.get_screen_size()
        self.__window = sg.Window(
            'Sistema Supermacado 2.0',
            location=(w/4 - 100, h/4)
        ).Layout(layout)

    def mostrar_opcoes(self, opcoes=[]):
        self.init_components()
        botao, values = self.__window.Read()
        return botao

    def fechar_tela(self):
        self.__window.close()
