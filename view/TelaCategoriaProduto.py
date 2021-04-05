import time
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

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
