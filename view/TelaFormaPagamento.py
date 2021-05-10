from view.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Formas de pagamento')

    def init_components(self, data):
        headings = ['Código', 'Método',
                    '                                     ']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='forma de pagamento', btn_deletar_enabled=False, btn_editar_enabled=False)

        super().set_tela_layout(layout, size=(430, 680))

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)
            if event == 'btn_cadastrar':
                return ('btn_cadastrar', None)
            else:
                continue
