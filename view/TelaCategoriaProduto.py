import time
import PySimpleGUI as sg
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema


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

    # TODO: Implementar
    # def listar_produtos_por_categoria(self, categoria: CategoriaProduto):
    #     if len(categoria.produtos) == 0:
    #         print(Terminal.error(self, mensagens.get('nenhum_produto_cadastrado')))
    #     else:
    #         print(Terminal.info(self, mensagens.get(
    #             'mostrando_produtos_categoria')(categoria)))
    #         for produto in categoria.produtos:
    #             print(mensagens.get('lista_produtos_por_cateogria')(produto))
    #     print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
    #     input()
