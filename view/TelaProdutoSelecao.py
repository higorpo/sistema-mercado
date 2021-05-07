import time
import PySimpleGUI as sg
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.Produto import Produto
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from messages.Produto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class TelaProdutoSelecao(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Produtos')

    def init_components(self, data):
        headings = ['Nome', 'Qtd. Estoque', 'Marca', 'Preço', 'Categoria']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='produto', btn_cadastrar_enabled=False, btn_deletar_enabled=False, btn_editar_enabled=False)

        super().set_tela_layout(layout, size=(430, 680))

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)
            elif event == '-TABLE-' and len(values['-TABLE-']) != 0:
                super().fechar_tela()
                return ('selecionado', values['-TABLE-'][0])
            else:
                return (event, values)
