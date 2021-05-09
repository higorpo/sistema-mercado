from view.AbstractTela import AbstractTela
from messages.Cliente import mensagens
from messages.Cliente import mensagens
from messages.Sistema import mensagens as mensagens_sistema
import PySimpleGUI as sg


class TelaCliente(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Clientes')

    def init_components(self, data):
        headings = ['Código', 'Nome', 'E-mail',
                    'Telefone', 'CPF', 'Endereço', 'VIP']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='cliente')

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
            elif (event == 'btn_editar' or event == 'btn_deletar') and len(values['-TABLE-']) == 0:
                sg.popup_no_buttons(
                    'Você precisa selecionar um item da lista para\npoder realizar esta ação.',
                    title='Erro'
                )
            elif (event == 'btn_editar' or event == 'btn_deletar') and len(values['-TABLE-']) != 0:
                print(f'Event: {event}\nValues: {values}')
                return (event, data[values['-TABLE-'][0]][0])
            else:
                return (event, values)

    # TODO implementar isso
    # def listar_compras(self, lista_pedidos):
    #     if len(lista_pedidos) == 0:
    #         print(Terminal.error(self, mensagens.get('cliente_nao_possui_pedidos')))
    #     else:
    #         print(Terminal.info(self, mensagens.get('mostrando_lista_compras')))
    #         for pedido in lista_pedidos:
    #             print(mensagens.get('lista_pedidos_por_cliente')(pedido))
    #     print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
    #     input()
