import time
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print(mensagens.get('label_nome_categoria'))
        return super().ler_string()

    def listar(self, categorias_produto):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))

        if len(categorias_produto) == 0:
            print(mensagens.get('nada_cadastrado'))
        else:
            for categoria_produto in categorias_produto:
                print(mensagens.get('lista_valores')(categoria_produto))

        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, categorias_produto, titulo_tela) -> CategoriaProduto:
        if len(categorias_produto) == 0:
            print(Terminal.error(
                self,
                mensagens.get('nada_cadastrado_busca')
            ))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoParaSelecionar

        return super().encontrar_opcao(categorias_produto, titulo_tela)
