from view.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaPedidosPorCliente(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Pedidos do cliente')

    def init_components(self, data):
        headings = ['Código', 'Observação', 'Data do pedido',
                    'Forma de pagamento', 'Itens do pedido']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='pedidos_do_cliente', btn_deletar_enabled=False, btn_editar_enabled=False, btn_cadastrar_enabled=False, btn_confirmar_enabled=True)

        super().set_tela_layout(layout, size=(430, 680))

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)
