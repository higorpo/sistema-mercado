import PySimpleGUI as sg
from view.AbstractTela import AbstractTela


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Categorias de produto')

    def init_components(self, data):
        headings = ['Código', 'Nome da categoria', 'Produtos cadastrados']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='categoria', btn_deletar_enabled=False, btn_editar_enabled=False, btn_visualizar_enabled=True)

        super().set_tela_layout(layout, size=(430, 680))

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
            if event == 'btn_visualizar':
                return (event, data[values['-TABLE-'][0]][0])
            if event == 'btn_cadastrar':
                return ('btn_cadastrar', None)
            else:
                continue
