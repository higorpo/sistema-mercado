import PySimpleGUI as sg
from view.AbstractTela import AbstractTela
from model.Pedido import Pedido
from messages.Pedido import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from datetime import date
from utils.Terminal import Terminal


class TelaPedido(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Pedidos')

    def init_components(self, data):
        headings = ['Código', 'Observação', 'Data do pedido', 'Cliente',
                    'Funcionário', 'Forma de pagamento', 'Itens dos pedidos']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='pedido', btn_deletar_enabled=False, btn_editar_enabled=False)

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

    def exibir_preco_final(self, total: float):
        sg.popup_ok(f'O preço total é de {total} reais')
