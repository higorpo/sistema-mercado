import PySimpleGUI as sg
from view.AbstractTela import AbstractTela


class TelaFormaPagamentoSelecao(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Formas de pagamento')

    def init_components(self, data):
        headings = ['Código', 'Método de pagamento',
                    '                                     ']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='forma de pagamento', btn_cadastrar_enabled=False, btn_deletar_enabled=False, btn_editar_enabled=False)

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
                return ('selecionado', data[values['-TABLE-'][0]][0])
            else:
                return (event, values)
