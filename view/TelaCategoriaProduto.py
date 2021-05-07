import time
import PySimpleGUI as sg
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar

# TODO quando clica numa categoria de produto, ele abre a mesma tela (talvez não tenha sido implementado ainda)


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Categorias de produto')

    def init_components(self, data):
        headings = ['Código', 'Nome da categoria', 'Produtos cadastrados']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='categoria', btn_deletar_enabled=False, btn_editar_enabled=False)

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

    def adicionar(self):
        print(mensagens.get('label_nome_categoria'))
        return super().ler_string()

    def listar_produtos_por_categoria(self, categoria: CategoriaProduto):
        if len(categoria.produtos) == 0:
            print(Terminal.error(self, mensagens.get('nenhum_produto_cadastrado')))
        else:
            print(Terminal.info(self, mensagens.get(
                'mostrando_produtos_categoria')(categoria)))
            for produto in categoria.produtos:
                print(mensagens.get('lista_produtos_por_cateogria')(produto))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()
