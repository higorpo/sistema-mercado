import PySimpleGUI as sg

from view.AbstractTela import AbstractTela
from messages.Sistema import mensagens as mensagens_sistema
from messages.Fornecedor import mensagens


class TelaFornecedor(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Fornecedores')

    def init_components(self, data):
        headings = ['Código', 'Nome', 'E-mail',
                    'Telefone', 'CNPJ', 'Fornece', 'Endereço']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='fornecedor')

        super().set_tela_layout(layout)

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)
            if event == '-TABLE-' and len(values['-TABLE-']) != 0:
                column_editar_deletar = super()._window.FindElement(
                    'column_editar_deletar'
                )
                column_editar_deletar.Update(visible=True)
            elif (event == 'btn_editar' or event == 'btn_deletar') and len(values['-TABLE-']) != 0:
                return (event, data[values['-TABLE-'][0]][0])
            else:
                return (event, values)
