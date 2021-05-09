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
        headings = ['Código', 'Nome', 'Qtd. Estoque',
                    'Marca', 'Preço', 'Categoria']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='produto', btn_cadastrar_enabled=False, btn_deletar_enabled=False, btn_editar_enabled=False, btn_confirmar_enabled=True)

        super().set_tela_layout(layout, size=(430, 680))

    def abrir_tela(self, data):
        self.init_components(data)

        produtos_selecionados = []
        while True:
            event, values = super().abrir_tela()
            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            if event == '-TABLE-':
                # Pega o index da linha clicada
                linha_selecionada = values[event][0]
                # Add em uma lista se ainda n estiver ali
                if linha_selecionada not in produtos_selecionados:
                    produtos_selecionados.append(linha_selecionada)
                # Remove da lista se já estiver ali
                else:
                    produtos_selecionados.remove(linha_selecionada)
                    # Resolve um problema de cor, pois por algum motivo quando se clica nas linhas ímpares (cor banca) de novo elas não perdem a cor verde
                    if linha_selecionada % 2 != 0:
                        tabela_atual.Update(
                            row_colors=[(linha_selecionada, 'white')])

            column_editar_deletar = super()._window.FindElement(
                'column_editar_deletar'
            )
            column_editar_deletar.Update(
                visible=True if len(produtos_selecionados) != 0 else False)

            # Muda a cor se a linha tiver sido selecioanda
            tabela_atual = super()._window.FindElement('-TABLE-')
            tabela_atual.Update(row_colors=tuple(
                [(x, '#62f35b') for x in produtos_selecionados]))

            if event == 'btn_confirmar':
                super().fechar_tela()
                return ('selecionado', produtos_selecionados)
            # else:
                # return (event, values)
